# 4. Annotation and map-drawing tools

## Annotators

**GeSeq** (Tillich et al. 2017, full text, doi:10.1093/nar/gkx391) is described in its title as “versatile and accurate annotation of organelle genomes.” It is a web-based annotator for organelle genomes; rely on the paper’s abstract and results for scope and accuracy claims rather than undocumented flags.

**CPGAVAS2** (Shi et al. 2019, full text, doi:10.1093/nar/gkz345) is “an integrated plastome sequence annotator and analyzer.”

**PGA, Plastid Genome Annotator** (Qu, Moore, Li and Yi 2019, full text, doi:10.1186/s13007-019-0435-7) is a command-line annotator that handles many plastomes in one run. Its abstract states:

> “In contrast to current existing tools, PGA uses reference plastomes as the query and unannotated target plastomes as the subject to locate genes, which we refer to as the reverse query-subject BLAST search approach. PGA accurately identifies gene and intron boundaries as well as intron loss. The program outputs GenBank-formatted files as well as a log file to assist users in verifying annotations.”

The project page in the paper and the README we opened is https://github.com/quxiaojian/PGA.

**ODNA** (2023, full text, doi:10.1093/bioinformatics/btad326) is titled “ODNA: identification of organellar DNA by machine learning.” It is a classifier for organellar DNA, not a gene annotator.

## Map drawing and IR junctions

**OGDRAW** has two versions we opened. Lohse, Drechsel, Kahlau and Bock (2013, full text, doi:10.1093/nar/gkt289) described “OrganellarGenomeDRAW—a suite of tools for generating physical maps of plastid and mitochondrial genomes.” Greiner, Lehwark and Bock (2019, full text, doi:10.1093/nar/gkz238) presented version 1.3.1 as “the standard tool to draw graphical maps of plastid and mitochondrial genomes,” with a new front end, a local copy of the NCBI RefSeq organelle database, and processing of many (multi-)GenBank files in one run. “The new OGDRAW server can be accessed at https://chlorobox.mpimp-golm.mpg.de/OGDraw.html.”

**Chloroplot** (Zheng et al. 2020, full text, doi:10.3389/fgene.2020.576124) is “An Online Program for the Versatile Plotting of Organelle Genomes.”

**IRscope** (Amiryousefi, Hyvönen and Poczai 2018, abstract only, doi:10.1093/bioinformatics/bty220) is “an online program to visualize the junction sites of chloroplast genomes.” We did not obtain a full text.

## Claim–source table

| Claim | Source | Quoted sentence or figure/table | What was read |
|---|---|---|---|
| GeSeq annotates organelle genomes | doi:10.1093/nar/gkx391 | Paper title | Full text (PMC5570176) |
| CPGAVAS2 is an integrated plastome annotator and analyzer | doi:10.1093/nar/gkz345 | Paper title | Full text (PMC6602467) |
| PGA: reverse query-subject BLAST; annotation of many plastomes in one run; GenBank + log; GitHub quxiaojian/PGA | doi:10.1186/s13007-019-0435-7 ; https://github.com/quxiaojian/PGA | Abstract sentences quoted above | Full text (PMC6528300) + README |
| ODNA identifies organellar DNA by machine learning | doi:10.1093/bioinformatics/btad326 | Paper title | Full text (PMC10229373) |
| OGDRAW 2013: physical maps of plastid and mitochondrial genomes | doi:10.1093/nar/gkt289 | Paper title | Full text (PMC3692101) |
| OGDRAW 1.3.1 is presented as the standard map-drawing tool; RefSeq copy; multi-GenBank input; server URL | doi:10.1093/nar/gkz238 | Abstract sentences quoted above | Full text (PMC6602502) |
| Chloroplot: online plotting of organelle genomes | doi:10.3389/fgene.2020.576124 | Paper title | Full text (PMC7545089) |
| IRscope visualizes chloroplast IR junction sites | doi:10.1093/bioinformatics/bty220 | Paper title | Abstract only |
