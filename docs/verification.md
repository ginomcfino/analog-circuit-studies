# Verification Record

Reviewed on 2026-10-28 using Qucs-S 26.1.1 and ngspice 47. These checks concern source portability, saved-data integrity and the explicitly tested simulation behavior. They do not establish physical performance.

| Study | Verification performed |
| --- | --- |
| Active bandpass | Corrected sine-amplitude sweep parameter and transient sampling; completed 20 distinct runs with 20,001 samples each. Qucs-format data compared exactly against the completed raw results. |
| Guitar phase-shift | Corrected control-node connections; fresh AC/transient run verifies 5 Hz at both gates and changing wet-path phase. Dataset lengths, finite values and diagram references checked; no simulator warnings. |
| Dual supply | Original dataset retained byte-for-byte; model paths made relative. Native source/netlist loading and saved plot display checked; no simulation rerun. |
| 555 siren | Saved time grids, waveforms and constant measurement columns checked. Native ngspice load-only viewing verified; no simulation rerun. |
| Hartley | Saved startup values and existing plots reviewed. Native ngspice load-only viewing verified; no simulation rerun. |
| BJT amplifier | Saved log completion and numerical tables reviewed; charts extracted with source-line provenance. Native ngspice load-only viewing verified; no simulation rerun. |
| Linkwitz | Saved AC/transient arrays and reference attribution checked. Native ngspice load-only viewing verified; no simulation rerun. |

The native ngspice viewing helper successfully loaded eight saved datasets and produced 15 SVG views without analysis commands. It preserves the precision of the supplied numbers.

Qucs schematics were checked through its native ngspice netlister; matching `.dpl` plot views were loaded and exported by Qucs itself. Native exports are labeled as exports, not screenshots. Window automation was unreliable, including after restarting the app. The command-line printer selects Qucsator and cannot directly render SPICE-only schematic components; separate data displays avoid that printer limitation without changing circuit symbols.

Current source, result and plot files are identified in [the file manifest](files-sha256.json). Each study's metrics/logs identify the numerical evidence where available. Original working copies and superseded outputs are retained outside this showcase in the portfolio archive.
