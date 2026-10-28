# Opening and Reproduction

## Qucs-S projects

Use Qucs-S 26.1.1 or a compatible later version with **ngspice selected**. The files originated in Qucs-S 25.2.0. On macOS, `.sch` may be associated with KiCad; open these files from Qucs-S's **File → Open** command.

1. Open `<study>-qucs-s/project/<study>.sch`.
2. Keep its matching `.dat.ngspice` file and `models/` folder in place.
3. Use **View All** to see the circuit and embedded results. Open the neighboring `<study>.dpl` for a separate, arranged plot view.

Opening saved results does not require a simulation run. The data displays retain the circuit's original trace expressions and axis settings; the README figures provide selected responses with explicit units and interpretation.

To run a new simulation, copy the entire `project/` directory first, then use Qucs-S's simulation command with ngspice configured. This preserves the recorded showcase dataset. The bandpass sweep takes longer than the Qucs-S CLI's short internal `--run` wait; use the GUI or run its generated netlist directly from the copied project directory.

The band's 20-setting, high-resolution dataset is about 95 MB and intentionally remains uncompressed so it opens directly.

## Native ngspice projects

Each study has a canonical `.cir` in `source/`, with required models in `source/models/`. Its README gives the run command. Saved results stay under `results/`, separate from new outputs.

To inspect saved numerical data in ngspice **without rerunning a circuit**, run from this collection's root:

```sh
python3 tools/prepare-ngspice-view.py
cd 555-two-tone-siren-ngspice/viewer
ngspice -n load-saved-data.spice
```

Substitute another study's folder as needed. The helper converts existing DAT/CSV values to ngspice's ASCII raw format, preserving their numeric tokens. It supplies load/display commands and a separate SVG hardcopy deck. It does not run a circuit, interpolate data or fit curves. Generated `viewer/` directories can be recreated and are excluded by `.gitignore`.

For an automated saved-data load and SVG check:

```sh
python3 tools/prepare-ngspice-view.py --validate --ngspice /path/to/ngspice
```

The original BJT evidence is a printed console log, so its extracted data retain that printed precision. Hartley has numerical startup data; its supplied steady-state result is an SVG rather than a raw vector file. Linkwitz magnitude/phase columns remain real dB/radian values in the viewer, without reconstructing unsupplied complex data.
