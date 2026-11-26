# Guide figures

[中文](README.zh.md) · [Knowledge map](../../KNOWLEDGE_MAP.md)

Four figures for the [knowledge map](../../KNOWLEDGE_MAP.md). Figures 1 and 2 are copied unchanged from open-access papers; figures 3 and 4 are schematics drawn by [`make_guide_figures.py`](make_guide_figures.py).

## Figure credits

| # | File | Credit | Licence |
|---|---|---|---|
| 1 | `01_plastome_map_zheng2020_fig2.jpg` | Zheng S, Poczai P, Hyvönen J, Tang J, Amiryousefi A (2020). Chloroplot: an online program for the versatile plotting of organelle genomes. *Frontiers in Genetics* 11:576124, Figure 2 (chloroplast genome map of giant ragweed, *Ambrosia trifida*). [doi:10.3389/fgene.2020.576124](https://doi.org/10.3389/fgene.2020.576124) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), reproduced unchanged |
| 2 | `02_mito_isoforms_kozik2019_fig2.png` | Kozik A, Rowan BA, Lavelle D, Berke L, Schranz ME, Michelmore RW, Christensen AC (2019). The alternative reality of plant mitochondrial DNA: one ring does not rule them all. *PLOS Genetics* 15(8):e1008373, Figure 2 (isoforms of *Lactuca* mitochondrial genomes). [doi:10.1371/journal.pgen.1008373](https://doi.org/10.1371/journal.pgen.1008373) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), reproduced unchanged |
| 3 | `03_organelle_concepts_schematic.png` | Made for this repository by `make_guide_figures.py` (toy shapes; the plastome region lengths and the count of 113 unique genes are from Jansen et al. 2006, [doi:10.1186/1471-2148-6-32](https://doi.org/10.1186/1471-2148-6-32)) | CC BY 4.0 (see [`NOTICE.md`](../../../NOTICE.md)) |
| 4 | `04_reference_route.png` | Made for this repository by `make_guide_figures.py` | CC BY 4.0 (see [`NOTICE.md`](../../../NOTICE.md)) |

How the licences of figures 1 and 2 were confirmed: the licence element of the PubMed Central full-text XML (PMC7545089 and PMC6742443), and the Crossref record both give the licence URL https://creativecommons.org/licenses/by/4.0/ (version 4.0); the Europe PMC record gives only "cc by", without a version. The image files are the files the publishers serve for those figures: for figure 1 the image on the Frontiers site (JPEG, 645,258 bytes, sha256 `610d80f28724c5aae228d5ea4d2c143459806371f3cabd473a11d94f1665a603`), and for figure 2 the PLOS "large" image (PNG, 386,819 bytes, sha256 `1c853c218a080f4e6da35d1c045613219840394dd848684d137200786572799d`), whose pixels are identical to the original TIFF that PLOS serves for the same figure.

## Captions

1. **Plastome map.** A circular map of the giant ragweed plastome: species name and genome length, GC content and gene count in the centre, the four regions (LSC, SSC, IRa, IRb) with their lengths, GC content, and genes coloured by functional class. It shows how a plastome is drawn as four parts. Caption in the paper: "Chloroplast genome map of giant ragweed (*Ambrosia trifida* L.)."
2. **Mitochondrial isoforms.** Panel A shows two major isoforms of the *Lactuca sativa* mitochondrial genome that differ by a swap of units after recombination between direct repeats; panel B shows major isoforms and recombination products of *L. saligna* through inverted repeats. Caption in the paper: "Isoforms of *Lactuca* mitochondrial genomes."
3. **Concepts on one page.** A: the four-part plastome of *Vitis vinifera* with the real region lengths (LSC 89,147 bp, IR 26,358 bp each, SSC 19,065 bp; 160,928 bp in total) and the junctions that move in an IR shift. B: a master circle with two repeats that recombine into two sub-circles. C: plastid and mitochondrial DNA segments inserted into nuclear chromosomes (NUPT, NUMT). D: a C-to-U edit that makes an AUG, and two organelle haplotypes in one individual. Everything except the plastome region lengths and the count of 113 unique genes (Jansen et al. 2006) is a toy illustration.
4. **Reference route.** The eight steps of the reference workflow with example tools; the order is a guide, not a fixed pipeline.

## Print size and legibility

Figures 3 and 4 are 1600 px wide and made to be printed 183 mm wide (222 dpi, stored in the PNG files; figure 3 is 1480 px tall, about 169 mm, and figure 4 is 1040 px tall, about 119 mm). The smallest text is 20 px, which is 6.5 pt at that width; on a screen they are read at their pixel size. Text colours have a contrast of at least 4.5:1 against the colours behind them.

## Redrawing the schematics

`make_guide_figures.py` needs only Pillow and the DejaVu fonts (paths are fixed to `/usr/share/fonts/truetype/dejavu/`). The two schematics were drawn with Pillow 12.3.0 and are reproduced byte for byte by:

```
python3 make_guide_figures.py OUTDIR
```

The script refuses to overwrite an existing file. It also stops if any text is smaller than 20 px, falls outside its frame, or has a contrast below 4.5:1 against the colours behind it. The script is MIT-licensed (see [`LICENSE`](../../../LICENSE)).
