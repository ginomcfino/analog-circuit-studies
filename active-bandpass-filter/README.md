# Active Bandpass Filter

Open `ActiveBandpassFilter.sch` in Qucs-S with its ngspice backend. The files record Qucs 25.2.0. `ActiveBandpassFilter.dat.ngspice` is the saved dataset for that schematic name. The `_final.sch` copy contains the same circuit with different view and output-file settings; regenerate its results rather than assuming it loads the other dataset automatically.

The schematic uses Qucs-S's `SpiceOpamp` / `LM324` library. The exported `netlist.cir` embeds an LM324 model but retains a Windows-specific absolute include for `ngspice_mathfunc.inc`. That helper is not bundled here. Regenerate the netlist in your Qucs-S installation or point the include to that installation's matching helper file before running it directly.

Saved simulation data is preserved unchanged. Results have not been rerun or checked against physical measurements for this collection.
