# 3. Assembly graphs and alternative conformations

Plant mitochondrial DNA is often better reported as a graph than as one circle. This chapter collects statements from papers and READMEs that were opened in this batch.

## Why a graph

Kozik et al. (2019, full text) titled their paper “The alternative reality of plant mitochondrial DNA: One ring does not rule them all.” The work is an explicit argument against treating a single master circle as the default description of plant mtDNA.

Gualberto and Newton (2017, abstract) already framed the biology: recombination at repeats “generate[s] subgenomic forms and extensive genomic variation even within the same species.”

Fischer et al. (2022, full text, doi:10.1093/nargab/lqac027), titled “Graph-based models of the *Oenothera* mitochondrial genome capture the enormous complexity of higher plant mitochondrial DNA organization,” is a worked example of encoding that complexity as a graph.

He et al. (2023, abstract only, first author He W, not Wang; title “Master graph: an essential integrated assembly model for the plant mitogenome based on a graph-based framework,” doi:10.1093/bib/bbac522) introduced a “graph-based sequence assembly toolkit (GSAT)” that constructs mitochondrial master graphs (MMGs). For rice and thale cress they reported MMG lengths of 346,562 and 358,041 bp, “including 9 and 6 contigs and 12 and 8 links, respectively,” which “could be further divided into 6 and 3 minimum master circles and 4 and 2 minimum secondary circles separately.” We have only the abstract, not the full text.

## What assemblers output

GetOrganelle’s abstract (Jin et al. 2020, full text) states that the toolkit “filters and disentangles the assembly graph, and produces all possible configurations of circular organelle genomes.” The full text also notes “labeled assembly graphs for user-friendly manual completion and correction.”

Oatk (Zhou et al. 2025, full text) “leverages a new search method to find the best supported path through the assembly graph,” and discusses structural complexity and heteroplasmy across 195 plant species.

PMAT’s README documents a `graphBuild` mode: if autoMito “fails to generate the assembly graph,” “you can use this command to manually select seeds for assembly.” We have not run that mode.

Hou et al. (JIPB 2025, full text) include “Figure S1. Pan-chloroplast structure from 33 *Vitis* accessions generated using Bandage.” That is a grape-specific use of graph visualization, not a new assembler.

## Looking at the graph

Wick et al. (2015, full text) described Bandage as “interactive visualization of de novo genome assemblies.” The expanded name “a Bioinformatics Application for Navigating De novo Assembly Graphs Easily” is the GitHub repository description and the wording on the project homepage (https://rrwick.github.io/Bandage/). The README opened in this batch introduces Bandage as “a GUI program that allows users to interact with the assembly graphs.” The JIPB supplement cited above is one published use on *Vitis* chloroplast graphs.

## What to report from a graph assembly

This is a recommended output list drawn from the READMEs already cited, not a protocol we ran:

- GetOrganelle: the README and paper describe labeled assembly graphs and “all possible configurations of circular organelle genomes.”
- Oatk: the paper describes searching for “the best supported path through the assembly graph.”
- PMAT: note whether `autoMito` completed or whether `graphBuild` was used to select seeds; retain the GFA/graph alongside any linearized path, and document which path was selected.
- Repeat-pair and cross-repeat support counts should be taken from the tool’s own output documentation when that documentation has been opened; we do not invent a grape reporting format here.

Figure F2 now also draws a graph-view arrow from GetOrganelle and from Oatk, not only from PMAT, because those tools also emit assembly graphs.

## Claim–source table

| Claim | Source | Quoted sentence or figure/table | What was read |
|---|---|---|---|
| Plant mtDNA should not be assumed to be one master circle | doi:10.1371/journal.pgen.1008373 | Paper title | Full text |
| Repeat recombination generates subgenomic forms | doi:10.1146/annurev-arplant-043015-112232 | Abstract sentence in chapter 1 | Abstract only |
| Graph models of the *Oenothera* mitochondrial genome | doi:10.1093/nargab/lqac027 | Paper title | Full text (PMC8969700) |
| GSAT MMGs for rice and *A. thaliana*: lengths, contig and link counts, master and secondary circles | doi:10.1093/bib/bbac522 | Abstract sentences quoted above | Abstract only |
| GetOrganelle produces all possible circular configurations and labeled graphs | doi:10.1186/s13059-020-02154-5 | Abstract and full-text workflow sentences | Full text |
| Oatk finds a best-supported path through the assembly graph | doi:10.1186/s13059-025-03676-6 | Abstract | Full text |
| PMAT `graphBuild` is the fallback when `autoMito` fails | https://github.com/bichangwei/PMAT | README | README |
| JIPB Fig. S1: pan-chloroplast structure of 33 *Vitis* accessions, drawn with Bandage | doi:10.1111/jipb.13968 | Figure S1 caption | Full text (caption); the figure image itself was not redrawn from the paper |
| Bandage: interactive visualization of de novo assembly graphs | doi:10.1093/bioinformatics/btv383 ; https://rrwick.github.io/Bandage/ ; https://github.com/rrwick/Bandage | Paper title; homepage/repo description; README intro quoted above | Full text + README + homepage wording via the repo description already logged |
