# Hartley LC Oscillator

A nominal 100 kHz oscillator study using a tapped LC tank, a generic op-amp macromodel, and diode amplitude limiting. It examines tank resonance, startup, and steady-state behavior.

## Circuit and analyses

The [netlist](source/hartley-oscillator.cir) includes its models and uses ±15 V supplies, 100 µH and 153 µH inductors, and a 10 nF tank capacitor. It performs a 70–130 kHz passive-tank AC sweep, an 80 µs startup transient, and a 5 ms transient with a 4.80–4.85 ms detail window.

## Saved evidence

- [Tank impedance](results/plots/hartley_tank_ac_response.svg): magnitude in ohms, not oscillator gain.
- [Startup waveform](results/plots/hartley_startup_transient.svg) and [original startup data](results/data/Hartley_startup_transient.dat): 8,016 finite samples over approximately 0–80 µs, ranging from −2.17058723 to +2.04872229 V.
- [Steady-state detail](results/plots/hartley_steady_state_zoom.svg): the final 4.80–4.85 ms window.

![Saved steady-state waveform](results/plots/hartley_steady_state_zoom.svg)

100 kHz is the design target. The source requests frequency and amplitude measurements, but no corresponding console log or steady-state numeric dataset was supplied; an exact measured frequency is therefore not asserted here. The generic op-amp is a model rather than a selected, hardware-tested part. Original data and plots are unchanged; no simulation was rerun during packaging.

## Open or run manually

Open the `.cir` file in a text editor. With ngspice installed, run from this project folder:

```sh
cd source
ngspice -b hartley-oscillator.cir > run.log 2>&1
```

No external model files are required. New outputs are written to `source/`; supplied evidence stays under `results/`. The source writes `Hartley_` output names, while the supplied SVGs use lowercase `hartley_`. Circuit content is unchanged; the canonical source was renamed, so use the command above rather than its historical filename comment.

Saved numerical results can also be loaded in ngspice without rerunning the circuit; see the [collection viewing guide](../../docs/opening-and-reproduction.md).
