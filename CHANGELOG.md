# Changelog

This is the public summary of changes to the teaching files in `grapevine-plastid`. Internal build logs stay on the build machine and are not part of this repository.

## 2026-11-26: knowledge-base layout and licence

- The home page (English and Chinese) now opens with a short **Start here** section: what the repository is, how to use it, and links to the knowledge map. The chapters and the catalogue below it are unchanged; lines are only inserted.
- New knowledge map in English and Chinese: [`docs/KNOWLEDGE_MAP.md`](docs/KNOWLEDGE_MAP.md) and [`docs/KNOWLEDGE_MAP.zh.md`](docs/KNOWLEDGE_MAP.zh.md). It covers the main concepts (plastome four-part structure, inverted-repeat shifts, plant mitochondrial recombination and multipartite structure, NUPT and NUMT, RNA editing, heteroplasmy), tools by analysis step, a reference workflow and the published grapevine organelle genomes, and lists the papers it cites.
- Four guide figures in [`docs/figures/guide/`](docs/figures/guide/README.md): two figures reproduced unchanged from open-access papers (CC BY 4.0) and two schematics drawn by a script in the same folder.
- New [`LICENSE`](LICENSE) (MIT, for code) and [`NOTICE.md`](NOTICE.md) (CC BY 4.0 for text and figures made here; reproduced figures keep their own licence), with a Chinese version [`NOTICE.zh.md`](NOTICE.zh.md).

## 2026-11-15 (bundle v7b)

- Wording polish; facts and quotes unchanged.
- README.md and README.zh.md keep the existing lines from the repository front page (the "This is not" links, "What will land later", "See also" and the author line). Only the sentence that called this a placeholder repository with no content yet is replaced by the new introduction.

## 2026-11-15 (bundle v6)

Punctuation only; no facts, numbers, DOIs, or [待确认] markers were changed.

- The JIPB 2025 selective-sweep quotation now writes π<sub>wild</sub>/π<sub>cul</sub> with no spaces around the slash, matching the source wording.
- In the Chinese chapters 02 and 09, English verbatim quotations that had ended with a fullwidth period now end with a halfwidth period.

## Already in the teaching tree (earlier revisions)

- Chapter 9 splits the JIPB 2025 (*J. Integr. Plant Biol.*, doi:10.1111/jipb.13968, PMC12498075) filters by subsection: the NUMT/NUPT depth formula; π and *F*<sub>ST</sub> keep variants with DP > 2 and missing < 0.1; the 1.5-fold depth cap, the four-read rule, MAF ≥ 0.05, and missing < 0.2 belong only to the GWAS subsection. The remark that copy number and coverage are part of that paper’s filters is labelled as this repository’s inference.
- Author attribution in the teaching text uses Hou, not Xiao.
- MitoHiFi is quoted as “was optimised” and “not optimised to assemble plants or fungal organelles.” The source spelling Geseq is kept and marked [sic].
- Pipia et al. 2024 (OENO One, doi:10.20870/oeno-one.2024.58.4.8087) is listed in DOI_CHECKS from the title and the Crossref abstract.
- Claims without an opened source are cut or marked [待确认].
