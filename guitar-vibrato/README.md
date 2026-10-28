# Guitar Vibrato

Open `Guitar_Vibrato_Unit_final.sch` in Qucs-S with its ngspice backend. The files record Qucs 25.2.0. The exported `netlist_final.cir` retains a Windows-specific absolute include for `ngspice_mathfunc.inc`, which is not bundled here. Regenerate the netlist in your Qucs-S installation or point the include to that installation's matching helper file before running it directly.

Known issue: the exported netlist's modulation and bias nodes appear disconnected from the JFET gate nodes. Review schematic connectivity and regenerate/retest before presenting the circuit as a working vibrato implementation. The saved AC and transient dataset is preserved for inspection, not offered as proof of successful modulation.

No physical testing or new simulation run is claimed.
