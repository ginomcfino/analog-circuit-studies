# Third-Party Material

- Qucs-S supplies the LM324 library model used by the bandpass study and the standard transformer/math helpers. The bundled `ngspice_mathfunc.inc` and `xfmr.cir` come from the official [Qucs-S 26.1.1 source](https://github.com/ra3xdh/qucs_s/tree/26.1.1); its [COPYING text](licenses/qucs-s-COPYING.txt) is retained. This attribution does not assign a license to the author's circuit work.
- The 555 and TL072 model files retain their supplied headers. Embedded transistor and generic-op-amp models retain their source comments.
- The Linkwitz reference schematic is a supplied educational example with 2015-seminar annotations. The reference topology and model are distinct from the author's simulation implementation and analysis.
- The dual-supply regulator models are supplied behavioral equivalents, not manufacturer macromodels.

Original circuit/simulation work and subsequent review corrections are identified in the study documentation. Simulation plots are not hardware measurements.
