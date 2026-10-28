# 555 Two-Tone Siren

A pair of bipolar 555 timers produces slow modulation and alternating audio tones. A transistor switches the audio timer's control voltage, and a coupling capacitor drives a modeled 8 Ω load.

## Circuit and analyses

The [netlist](source/555-two-tone-siren.cir) uses a 9 V supply and a 5.2 s transient analysis. It measures modulation period/duty cycle and the two audio frequencies. The [555 model](source/models/BIP-555.lib) is bundled with its original header.

## Saved evidence

| Measurement | Saved result |
| --- | ---: |
| Modulation period | 1.03715767 s |
| Duty cycle | 73.352139% |
| Dee tone | 709.018718 Hz |
| Dah tone | 575.175429 Hz |

Values come from [measurement-summary.csv](results/data/measurement-summary.csv), extracted from the first row of [siren_measurements.dat](results/data/siren_measurements.dat). All four scalar columns were verified constant across its 290,375 rows. The original 37.7 MB file is retained unchanged, along with [modulation data](results/data/siren_modulation.dat) and [speaker-load data](results/data/siren_speaker.dat).

![Saved modulation output](results/plots/siren_modulation.svg)

[Speaker-load voltage](results/plots/siren_speaker.svg) · [Dee detail, 1.45–1.48 s](results/plots/siren_speaker_dee.svg) · [Dah detail, 1.90–1.93 s](results/plots/siren_speaker_dah.svg)

These are simulated electrical results, not a sound recording or hardware validation. The saved values differ from approximate calculations in the source comments. The source notes that a physical speaker driver may require an output buffer. No simulation was rerun during packaging.

## Open or run manually

Open the `.cir` file in a text editor. With ngspice installed, run from this project folder:

```sh
cd source
ngspice -b 555-two-tone-siren.cir > run.log 2>&1
```

Keep `models/` beside the netlist. A new run writes its fixed output filenames into `source/`; the supplied evidence remains separately preserved under `results/`. Only the relative model include was changed for this organization.

Saved numerical results can also be loaded in ngspice without rerunning the circuit; see the [collection viewing guide](../../docs/opening-and-reproduction.md).
