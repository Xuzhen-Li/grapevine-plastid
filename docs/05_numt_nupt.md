# 5. NUMTs and NUPTs

The GSAT abstract (He et al. 2023, first author He W, not Wang; title “Master graph: an essential integrated assembly model for the plant mitogenome based on a graph-based framework,” doi:10.1093/bib/bbac522) uses these names: “The nuclear mitochondrial DNA segments (NUMTs)” and “The mitochondrial plastid DNA segments (MTPTs).” In this chapter: a NUMT is a mitochondrial-derived segment in the nuclear genome; a NUPT is a plastid-derived segment in the nuclear genome; an MTPT is a plastid-derived segment in the mitochondrial genome. NUMTs and NUPTs sit in the nucleus; MTPTs sit in the mitochondrion.

## Definitions and a recent review

A 2026 review in *The Plant Journal* (full text, doi:10.1111/tpj.70685), titled “Nuclear DNA of plastid origin (NUPTs), neglected driver of genome variation and evolutionary innovation.” states in its abstract:

> “Plant nuclear genomes contain a variable, though typically minor, fraction of DNA sequences of plastid origin known as NUPTs. Unlike the massive transfer of DNA and genes from the proto-organelle genome to the nucleus that occurred during the endosymbiotic event that gave rise to plastids, the formation of NUPTs is an ongoing process that does not imply concomitant DNA loss.”

It also states that NUPTs “show preferential overlap with specific superfamilies of transposable elements,” and that they are “consistently enriched among certain classes of non-coding RNA genes.” Those are the authors’ review conclusions; we quote them rather than re-scoring any genome.

## Grapevine counts from Hou et al. 2025

Hou et al. (JIPB 2025, full text) examined cytonuclear interactions during grapevine domestication with pan-mitogenome, pan-plastome, and haplotype-resolved nuclear genomes from 33 accessions. The abstract (and the matching main-text statement) reports:

> “Extensive genomic signals of cytonuclear interactions were detected, including a total of 212–431 nuclear–mitochondrial segments (NUMTs) and 95–205 nuclear–plastid segments (NUPTs). These results showed that NUMTs were under strong selection and were more abundant in cultivated grapes, whereas NUPTs dominated in wild grapes.”

They also wrote that they identified 84 candidate genes associated with mitochondrial–nuclear interactions by GWAS, including *PFD1*, and that “there are significantly more cytonuclear interaction genes near NUMTs than in other genomic regions.”

Oatk (Zhou et al. 2025, abstract) lists “DNA exchange between organelles” among the insights from 195 plant species. That is a cross-species observation from the Oatk paper, not a grape count.

The same GSAT abstract noted that NUMTs in thale cress “strongly affected the frequency evaluation of the homologous structures in the mitogenome,” while MTPTs “had no effects on the assessment of the MMGs,” “while the effects of NUMTs in rice were relatively weak.” Abstract only.

## Distinguishing nuclear transfers from assembly artefacts

A NUMT or NUPT in the nuclear genome is a biological transfer. A nuclear-derived contig mixed into an organelle assembly is a different problem (an assembly artefact). The papers and READMEs opened here describe filters, not a grape-specific protocol we ran:

- Oatk README: set `-c` to 5–10 times nuclear coverage to “filter out the nuclear genome and numts” (chapter 2).
- MitoHiFi README: “Identify and separate NUMTS … from genuine mitogenome contigs” (chapter 2). The same README, section 6, states, verbatim, “MitoHiFi is still not optmized to assemble a plant mitochondria or chloroplast.” The `-a plant` flag is for use with `-c` to finish an existing plant organelle contig; the paper (PMC10354987) says plant “outcomes may vary.” MitoHiFi is not a direct replacement for the plant graph-assembler filters listed here.
- GetOrganelle filters and disentangles the assembly graph (chapters 2 and 3).

Whether any individual filter is sufficient for a given *Vitis* dataset remains **[待确认]**.

## Claim–source table

| Claim | Source | Quoted sentence or figure/table | What was read |
|---|---|---|---|
| NUPTs are nuclear DNA of plastid origin; their formation is ongoing and need not coincide with DNA loss from the plastid | doi:10.1111/tpj.70685 | Abstract sentences quoted above | Full text (PMC12863932) |
| NUPTs overlap certain TE superfamilies and are enriched in some ncRNA classes (review conclusion) | doi:10.1111/tpj.70685 | Abstract | Full text |
| In 33 *Vitis* accessions: 212–431 NUMTs and 95–205 NUPTs; NUMTs more abundant in cultivated grapes, NUPTs dominated in wild grapes | doi:10.1111/jipb.13968 | Abstract / main-text sentences quoted above | Full text |
| 84 GWAS candidate genes for mitochondrial–nuclear interaction, including *PFD1*; more such genes near NUMTs | doi:10.1111/jipb.13968 | Abstract | Full text |
| Oatk paper reports insights into DNA exchange between organelles (195 species) | doi:10.1186/s13059-025-03676-6 | Abstract | Full text |
| NUMT / MTPT names and definitions as used in the GSAT abstract; NUMTs strongly affected structure-frequency estimates in thale cress, weakly in rice; MTPTs did not affect MMG assessment | doi:10.1093/bib/bbac522 | Abstract sentences quoted above | Abstract only |
| MitoHiFi NUMT separation is documented in the README, but the same README §6 says the tool is “still not optmized to assemble a plant mitochondria or chloroplast”; `-a plant` is used with `-c` to finish existing contigs; plant “outcomes may vary”; not a direct replacement for plant graph-assembler filters | doi:10.1186/s12859-023-05385-y ; https://github.com/marcelauliano/MitoHiFi | README §6 and paper sentences quoted in chapter 2 | Full text (PMC10354987) + README, re-opened 2026-11-15 CST |
