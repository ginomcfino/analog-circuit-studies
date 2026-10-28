#!/usr/bin/env python3
"""Prepare ngspice views from saved numeric results, without running a simulation.

Run from any directory: python3 tools/prepare-ngspice-view.py
Optional verification: add --validate --ngspice /path/to/ngspice
Generated ngspice/<study>/viewer/ files are disposable and ignored by Git.
Run ngspice interactively from that viewer directory with:
    ngspice -n load-saved-data.spice
The generated hardcopy deck loads the same data and exports SVGs, then quits.
No circuit sources, models, analysis commands, interpolation, or fitting are used.
The ASCII raw files retain every numeric token in the saved DAT/CSV columns;
BJT CSV precision remains limited to the original printed simulation log.
"""
from pathlib import Path
import argparse
import csv
from decimal import Decimal
import hashlib
import json
import math
import subprocess


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table(path, columns):
    if path.suffix == '.csv':
        with path.open(newline='') as f:
            reader = csv.reader(f)
            next(reader)
            rows = [tuple(row[:columns]) for row in reader if row]
    else:
        rows = [tuple(line.split()) for line in path.read_text().splitlines() if line.strip()]
    assert rows and all(len(row) == columns for row in rows), path
    assert all(math.isfinite(float(v)) for row in rows for v in row), path
    return rows


def join_tables(*tables):
    assert len({len(t) for t in tables}) == 1, 'Cannot join different saved grids'
    rows = []
    for samples in zip(*tables):
        assert len({Decimal(s[0]) for s in samples}) == 1, 'Saved scale columns differ'
        rows.append((samples[0][0], *(v for sample in samples for v in sample[1:])))
    return rows


def write_raw(path, title, variables, rows, ac=False):
    assert len(variables) == len(rows[0])
    with path.open('w') as f:
        f.write(f'Title: {title}; imported saved values, no simulation rerun\n')
        f.write('Date: saved source values\n')
        f.write('Plotname: ' + ('AC Analysis' if ac else 'Transient Analysis') + '\n')
        f.write(f'Flags: real\nNo. Variables: {len(variables)}\nNo. Points: {len(rows)}\nVariables:\n')
        for i, (name, kind) in enumerate(variables):
            f.write(f'\t{i}\t{name}\t{kind}\n')
        f.write('Values:\n')
        for i, row in enumerate(rows):
            f.write(f'{i}\t{row[0]}\n')
            f.writelines(f'\t{v}\n' for v in row[1:])
    # Formatting audit: every token survives unchanged and in original row order.
    with path.open() as f:
        while next(f).strip() != 'Values:':
            pass
        for i, row in enumerate(rows):
            index, scale = next(f).split()
            recovered = (scale, *(next(f).strip() for _ in row[1:]))
            assert int(index) == i and recovered == row
        assert not f.read().strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--validate', action='store_true', help='ngspice load/display/SVG only; no simulations')
    ap.add_argument('--ngspice', default='ngspice')
    ap.add_argument('--study', action='append', choices=['linkwitz-transform', 'hartley-oscillator',
                    '555-two-tone-siren', 'bjt-amplifier'], help='Limit to a study; may be repeated')
    args = ap.parse_args()
    report = []
    for slug in ['linkwitz-transform', 'hartley-oscillator', '555-two-tone-siren', 'bjt-amplifier']:
        if args.study and slug not in args.study:
            continue
        study = args.root / 'ngspice' / slug
        data = study / 'results/data'
        viewer = study / 'viewer'
        viewer.mkdir(exist_ok=True)
        (viewer / '.gitignore').write_text('*\n')
        sources = {}
        batches = []

        def read(name, n):
            p = data / name
            sources[name] = sha(p)
            return table(p, n)

        def add(name, variables, rows, plots, ac=False):
            raw = viewer / (name + '.raw')
            write_raw(raw, slug + ' / ' + name, variables, rows, ac)
            batches.append({'raw':raw.name, 'points':len(rows), 'variables':variables,
                            'plots':plots, 'sha256':sha(raw), 'exact_token_roundtrip':True})

        if slug == 'linkwitz-transform':
            for port in ['eq', 'out', 'ratio']:
                add('ac-' + port, [('frequency', 'frequency'), ('mag_db', 'notype'), ('phase_rad', 'notype')],
                    read('linkwitz_ac_' + port + '.dat', 3),
                    [(f'ac-{port}-magnitude', 'mag_db', 'xlog', 'Frequency (Hz)', 'Saved magnitude (dB)'),
                     (f'ac-{port}-phase', 'phase_rad', 'xlog', 'Frequency (Hz)', 'Saved phase (rad)')], True)
            rows = join_tables(*(read('linkwitz_tran_' + port + '.dat', 2) for port in ['vin', 'eq', 'out', 'ratio']))
            add('transient', [('time','time'), ('vin','voltage'), ('veq','voltage'),
                              ('vout','voltage'), ('ratio','notype')], rows,
                [('transient-waveforms', 'vin veq vout', '', 'Time (s)', 'Voltage (V)'),
                 ('transient-ratio', 'ratio', '', 'Time (s)', 'Saved Vout / Veq')])
        elif slug == 'hartley-oscillator':
            add('startup', [('time','time'), ('vout','voltage')],
                read('Hartley_startup_transient.dat', 2),
                [('startup', 'vout', '', 'Time (s)', 'Output (V)')])
        elif slug == '555-two-tone-siren':
            rows = join_tables(read('siren_modulation.dat', 2), read('siren_speaker.dat', 2))
            add('transient', [('time','time'), ('modulation','voltage'), ('speaker','voltage')], rows,
                [('modulation', 'modulation', '', 'Time (s)', 'Modulation (V)'),
                 ('speaker', 'speaker', '', 'Time (s)', 'Speaker (V)'),
                 ('speaker-dee', 'speaker', 'xlimit 1.45 1.48', 'Time (s)', 'Speaker (V)'),
                 ('speaker-dah', 'speaker', 'xlimit 1.90 1.93', 'Time (s)', 'Speaker (V)')])
        else:
            rows = join_tables(read('nominal-ac-from-log.csv', 2), read('reduced-coupling-ac-from-log.csv', 2))
            add('ac-from-log', [('frequency','frequency'), ('nominal_db','notype'), ('reduced_coupling_db','notype')], rows,
                [('ac-from-log', 'nominal_db reduced_coupling_db', 'xlog', 'Frequency (Hz)', 'Printed gain (dB)')], True)
            rows = join_tables(read('nominal-transient-from-log.csv', 2), read('increased-drive-transient-from-log.csv', 2))
            add('transient-from-log', [('time','time'), ('nominal','voltage'), ('increased_drive','voltage')], rows,
                [('transient-from-log', 'nominal increased_drive', '', 'Time (s)', 'Printed output (V)')])
        load = ['* Saved result viewer; no circuit or simulation commands', '.control',
                'set noaskquit', 'set hcopydevtype=svg', 'set xbrushwidth=2']
        hardcopy = load.copy()
        for batch in batches:
            for lines in [load, hardcopy]:
                lines.extend(['load ' + batch['raw'], 'display'])
            for name, vectors, options, xlab, ylab in batch['plots']:
                hardcopy.append(f'hardcopy {name}.svg {vectors} {options} xlabel "{xlab}" ylabel "{ylab}" title "Saved data: {slug}"')
            # Leave all loaded datasets accessible; list vector names on opening.
        load.extend(['echo Saved data loaded. Use setplot to select a dataset, then plot a vector.', '.endc', '.end'])
        hardcopy.extend(['quit', '.endc', '.end'])
        (viewer / 'load-saved-data.spice').write_text('\n'.join(load) + '\n')
        deck = viewer / 'hardcopy-saved-data.spice'
        deck.write_text('\n'.join(hardcopy) + '\n')
        row = {'study':slug, 'sources':sources, 'datasets':batches, 'simulation_executed':False,
               'method':'saved numeric columns copied unchanged into real ASCII raw vectors',
               'limitations': 'No new precision beyond saved data; no inferred complex AC vectors. Hartley includes startup only.'}
        if args.validate:
            command = [args.ngspice, '-n', '-b', deck.name]
            p = subprocess.run(command, cwd=viewer, capture_output=True, text=True, timeout=50)
            log = p.stdout + '\n' + p.stderr
            (viewer / 'native-load-display-hardcopy.log').write_text(log)
            expected = [name + '.svg' for batch in batches for name, *_ in batch['plots']]
            assert p.returncode == 0 and all((viewer / name).stat().st_size > 200 for name in expected), log
            assert not any(word in log.lower() for word in ['error:', 'no such vector', 'failed']), log
            row.update(native_command=command, native_cwd=str(viewer.resolve()),
                       native_returncode=p.returncode, svg_outputs=expected)
        assert all(sha(data / name) == digest for name, digest in sources.items())
        (viewer / 'manifest.json').write_text(json.dumps(row, indent=2) + '\n')
        report.append(row)
        print(f'{slug}: {len(batches)} raw datasets, all original numeric tokens preserved')
    print('Generated viewer directories are disposable. No source or saved result files were changed.')


if __name__ == '__main__':
    main()
