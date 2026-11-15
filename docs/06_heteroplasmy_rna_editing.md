# 6. Heteroplasmy and RNA editing

## What “heteroplasmy” refers to in the papers we opened

A general textbook definition of heteroplasmy was not copied from a sentence in the 2017 NOVOPlasty assembly paper or from the Oatk 2025 abstract in this revision. The 2019 NOVOPlasty paper (Dierckxsens, Mardulyn and Smits; EuropePMC records the year as 2020, the README cites 2019; doi:10.1093/nargab/lqz011) describes a method that “detects intra-individual polymorphisms within mitochondrial and chloroplast genomes … and looks for linkage among polymorphic sites.” That is the operational sense used below. A broader biological definition remains **[待确认]** until a definition sentence is quoted from a paper opened for that purpose.

The NOVOPlasty GitHub README (https://github.com/ndierckx/NOVOPlasty) calls the program “The organelle assembler and heteroplasmy caller.” The same README’s “Cite” section says: “If you use the heteroplasmy or variance calling option, please cite both articles,” and names the 2017 assembly paper (doi:10.1093/nar/gkw955) together with the 2019/2020 heteroplasmy paper (doi:10.1093/nargab/lqz011). The 2017 paper is about assembly and is not the citation for the heteroplasmy caller.

Official README usage for heteroplasmy (section “Heteroplasmy”, MAF): first assemble the genome with MAF left unset; then give the resulting sequence as both the reference and the seed, and set MAF in the range 0.007–0.49 (“0.01 will detect heteroplasmy of >1%”). Whether a MAF of 0.01 is actually detected depends on sequencing depth; that is this repository’s inference, not a README sentence.

Oatk (Zhou et al. 2025, full text) lists heteroplasmy among the “insights” from assemblies of 195 plant species. Gualberto and Newton (2017, abstract) connect loss of nuclear repair functions to “increased ectopic recombination, genome instability, and heteroplasmy.”

Chapter 5 records that the GSAT abstract (He et al. 2023, not Wang) found NUMTs in thale cress “strongly affected the frequency evaluation of the homologous structures in the mitogenome.” Whether a low-frequency SNP called as heteroplasmy in short-read data can also come from a NUMT or NUPT is **[待确认]**; GSAT addressed structure-frequency estimates, not that SNP case.

We did not open a grape-specific heteroplasmy-frequency table in this batch. Any grape heteroplasmy rate is **[待确认]** until a paper is read for that number.

## Predicting C-to-U (and, in some plant clades, U-to-C) RNA editing

The PREPACT 3.0 paper (Lenz, Hein and Knoop 2018, full text, doi:10.1186/s12859-018-2244-9) states:

> “Gene expression in plant chloroplasts and mitochondria is affected by RNA editing. Numerous C-to-U conversions, accompanied by reverse U-to-C exchanges in some plant clades, alter the genetic information encoded in the organelle genomes.”

PREPACT 2.0 (Lenz and Knoop 2013, full text) likewise refers to “up to thousands of targeted C-to-U and U-to-C substitutions in mitochondria and chloroplasts of certain plants.” U-to-C is therefore not assumed for every plant. Whether *Vitis* has U-to-C organelle RNA editing was not established in a *Vitis* paper opened in this batch and is **[待确认]**.

**PREP-Mt** (Mower 2005, full text, doi:10.1186/1471-2105-6-96) is titled “PREP-Mt: predictive RNA editor for plant mitochondrial genes.” Its abstract discusses identifying “C to U RNA editing sites in plant mitochondrial protein-coding genes.”

These tools predict or catalogue editing sites on organelle sequences. We did not run them. PREP-Mt’s abstract also says prediction “could reduce or even eliminate the need for experimental determination of editing sites for many sequences.” For a new *Vitis* accession we still treat transcriptome validation as the check that a predicted site is actually edited, and we mark any claim that prediction can replace that check as **[待确认]** for grape.

## Claim–source table

| Claim | Source | Quoted sentence or figure/table | What was read |
|---|---|---|---|
| NOVOPlasty README: organelle assembler and heteroplasmy caller; cite both the 2017 assembly paper and the 2019/2020 heteroplasmy paper if the caller is used | https://github.com/ndierckx/NOVOPlasty ; doi:10.1093/nar/gkw955 ; doi:10.1093/nargab/lqz011 | README “Cite” section, quoted above | README (12,323 bytes) + 2017 full text + 2019/2020 abstract (PMC7671380) |
| 2019/2020 paper: detects intra-individual polymorphisms in mt and cp genomes and looks for linkage among polymorphic sites | doi:10.1093/nargab/lqz011 | Abstract phrase quoted above | Abstract (EuropePMC year 2020; README cites 2019) |
| Official heteroplasmy run: assemble first without MAF; then use the assembly as reference and seed and set MAF 0.007–0.49 (“0.01 will detect heteroplasmy of >1%”); whether 0.01 is detected depends on depth (repository inference) | https://github.com/ndierckx/NOVOPlasty | README “Heteroplasmy” / MAF explanation | README |
| Oatk paper discusses heteroplasmy among results from 195 species | doi:10.1186/s13059-025-03676-6 | Abstract | Full text |
| Loss of certain nuclear repair activities increases ectopic recombination, instability and heteroplasmy | doi:10.1146/annurev-arplant-043015-112232 | Abstract | Abstract only |
| RNA editing: numerous C-to-U conversions, with reverse U-to-C in some plant clades | doi:10.1186/s12859-018-2244-9 | Sentence quoted above | Full text (PMC6029061) |
| PREP-Mt predicts C-to-U sites in plant mitochondrial protein-coding genes | doi:10.1186/1471-2105-6-96 | Title / abstract | Full text (PMC1087475) |
| U-to-C editing in *Vitis* | — | — | Not opened; **[待确认]** |
| Low-frequency short-read “heteroplasmy” SNPs versus NUMT/NUPT | — | — | Not established by GSAT’s structure-frequency result; **[待确认]** |
| Numeric grape heteroplasmy rates | — | — | Not read in this batch; **[待确认]** |
