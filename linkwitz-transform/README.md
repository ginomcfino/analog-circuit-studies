# Linkwitz Transform

Open `linkwitz_circuit_final.cir` in ngspice, with this directory as the working directory. The relative include requires the bundled `Tl072.mod`; keep its original model header. The netlist writes the included `.dat` and `.svg` filenames, so use a separate working copy if preserving the saved results.

[reference-schematic.png](reference-schematic.png) is the supplied educational reference. Its original annotations identify an educational example associated with a 2015 seminar; they are retained in the image. The reference topology and bundled amplifier model are third-party material.

The [visual gallery](../docs/visuals.md) labels the EQ-stage response, combined output, and OUT/EQ ratio separately. The transient OUT/EQ ratio is retained as a diagnostic because division near zero produces spikes.

The numeric data and plots are existing simulation outputs. No rerun or physical measurement is claimed.
