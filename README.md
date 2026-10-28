# Analog Circuit Studies

Seven analog engineering studies covering filters, oscillators, audio modulation, amplification, equalization and power-supply behavior. Original circuit/simulation work was manually developed; component models and reference material retain their attribution. These are simulations, not hardware measurements.

## Study index

| Study | Open with | What it demonstrates | Evidence |
| --- | --- | --- | --- |
| [Active bandpass filter](active-bandpass-filter-qucs-s/) | Qucs-S + ngspice | Cascaded LM324 filtering, multitone response and diode limiting | Verified AC and corrected 20-setting amplitude sweep |
| [Guitar phase-shift / modulation](guitar-vibrato-qucs-s/) | Qucs-S + ngspice | JFET phase control and dry/wet blending | Verified 5 Hz gate modulation and changing wet-path phase |
| [Dual ±12 V supply](dual-rail-12v-supply-qucs-s/) | Qucs-S + ngspice | Rectification, reservoir filtering and behavioral regulation | Saved startup and output-rail data reviewed |
| [555 two-tone siren](555-two-tone-siren-ngspice/) | ngspice | Slow timing control and alternating audio-frequency oscillation | Saved waveforms and frequency/duty measurements |
| [Hartley LC oscillator](hartley-oscillator-ngspice/) | ngspice | Tank resonance, startup and amplitude limiting | Saved startup data and steady-state plots |
| [Two-stage BJT amplifier](bjt-amplifier-ngspice/) | ngspice | Bias, gain, drive level and coupling-capacitor response | Saved console results and extracted plots |
| [Linkwitz transform equalizer](linkwitz-transform-ngspice/) | ngspice | Equalization and a sealed-box speaker equivalent | Saved AC and transient data and plots |

Folders ending in `-qucs-s` contain graphical Qucs-S projects **using the ngspice simulation engine**. Folders ending in `-ngspice` contain native text-netlist projects. The distinction is the editing/viewing workflow; all seven studies use ngspice models/results.

Start with the [visual gallery](docs/visuals.md), then each study's README for its stimulus, analyses, results and model limits. See [opening and reproduction](docs/opening-and-reproduction.md) for saved-data viewing, and [verification](docs/verification.md) for what was checked.

The two corrected Qucs-S studies include fresh matching datasets. The supply and four native ngspice studies retain their supplied results without rerunning their circuits. Supporting models are bundled where required; duplicate working copies and obsolete outputs are excluded from this showcase.

[Model and reference attribution](docs/third-party-material.md).
