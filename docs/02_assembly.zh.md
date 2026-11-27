# 2. 按数据类型看组装软件

这一章打印的命令都抄自文末表里的 README 或论文，本机没有实际跑过。

## 短读长（Illumina）质体组装

**GetOrganelle**（Jin 等 2020，Genome Biology，全文）的摘要写道：

> “GetOrganelle is a state-of-the-art toolkit to accurately assemble organelle genomes from whole genome sequencing data. It recruits organelle-associated reads using a modified ‘baiting and iterative mapping’ approach, conducts de novo assembly, filters and disentangles the assembly graph, and produces all possible configurations of circular organelle genomes. For 50 published plant datasets, we are able to reassemble the circular plastomes from 47 datasets using GetOrganelle. GetOrganelle assemblies are more accurate than published and/or NOVOPlasty-reassembled plastomes as assessed by mapping. We also assemble complete mitochondrial genomes using GetOrganelle.”

全文补充：主脚本用 Bowtie2、BLAST 和 SPAdes，从种子出发，把比对到种子上的读段当作 “baits”。GitHub README（https://github.com/Kinggerm/GetOrganelle，2026-11-15 CST 打开）写它从 genomic skimming 数据组装细胞器基因组，并提醒更新到 1.7.5 以上以修正 self-loop 顶点拷贝数估计的错误。植物质体的示例命令是：

```
get_organelle_from_reads.py -1 forward.fq -2 reverse.fq -o plastome_output -R 15 -k 21,45,65,85,105 -F embplant_pt
```

线粒体示例用 `-F embplant_mt`。README 还写：该脚本面向 Illumina 双端或单端 fastq，建议用已去接头、未再做质控的原始读段。

**NOVOPlasty**（Dierckxsens、Mardulyn 和 Smits 2017，全文）可从全基因组数据中从头组装细胞器基因组。其仓库 README（https://github.com/ndierckx/NOVOPlasty）自称 “The organelle assembler and heteroplasmy caller”，运行命令为 `perl NOVOPlasty4.3.1.pl -c config.txt`。

**Freudenthal 等（2020，全文）**在模拟和真实数据集上比较了多种叶绿体组装工具，在 “Guidelines for the end-user” 一节中写道：

> “Given these results, our recommendation is to use GetOrganelle as a default option for chloroplast assemblies. If GetOrganelle does not produce a use-able assembly, Fast-Plast is a valid back-up solution that might be successful.”

讨论里还有： “The best performance overall, both on simulated and real data, was achieved by GetOrganelle.” 这项比较早于 PMAT（2024）、Oatk（2025）和 HiMT（2025），那些工具主要面向 HiFi 长读长，不能直接套用 2020 年的排名。

## HiFi 等长读长：线粒体和细胞器组装

**PMAT**（Bi 等 2024，全文）面向低覆盖度 HiFi。摘要写：在 13 个有代表性的植物线粒体基因组上做了从头组装，并写作者的评估认为 “PMAT only requires 1× HiFi sequencing data to obtain a complete plant mitogenome.” README（https://github.com/bichangwei/PMAT）补充：也可用 HiFi/CLR/ONT，也可组装叶绿体或动物线粒体；有一步式 `autoMito`，失败时用 `graphBuild`。这两种模式我们都没有实跑。

**Oatk**（Zhou 等 2025，Genome Biology 正式发表，全文；优先用这篇而不是 2024 预印本）摘要写了三块：基于 syncmer 的组装器、profile-HMM 识别细胞器、在组装图里找 “best supported path”。作者报告了 195 种植物的细胞器组装，并讨论结构复杂度、异质性和细胞器之间的 DNA 交换。README（https://github.com/c-zhou/oatk）写明面向 PacBio HiFi（不是 CLR/ONT）。示例：

```
oatk -k 1001 -c 30 -t 8 --nhmmscan /bin/nhmmscan -m embryophyta_mito.fam -p embryophyta_pltd.fam -o ddAraThal4 ddAraThal4_organelle.hifi.fa.gz
```

其中 `-c 30` 是拟南芥示例，不是葡萄默认值。同一 README 写 `-c` 应按核基因组覆盖度的 5–10 倍来设，以帮助滤掉核序列和 NUMT。

**HiMT**（Tang 等 2025，全文）面向 HiFi 的“一键”叶绿体和线粒体组装，摘要写它会自动估计覆盖度，并用固定 k-mer 前缀降低计算量，可在普通笔记本上使用，带 GUI。论文写明 GitHub（https://github.com/tang-shuyuan/HiMT）对非商业用户免费。README 示例：`himt assemble -i hifi.fa -o output_dir -t 10`，并记录了 `-d ONT/CLR`。使用前请同时看论文里的许可说明。

**PMAT2**（doi:10.1002/imt2.70064，全文）题名为图形化的综合细胞器组装工具。摘要写它适用于植物、动物和真菌线粒体以及植物叶绿体，即使大约 1× HiFi 也可。我们打开的是 https://github.com/bichangwei/PMAT2 的 README，其中的安装命令指向 `https://github.com/aiPGAB/PMAT2`。参数名与 PMAT 不同（`-t` 是 seqtype，`-G` 是 organelles，`-x` 是 taxo），不能照搬 PMAT 命令。

**MitoHiFi**（Uliano-Silva 等 2023，全文及 README；doi:10.1186/s12859-023-05385-y；PMC10354987）是从 PacBio HiFi 组装线粒体的 Python 流程。“寻找、环化并注释”这一句出在 GitHub 仓库简介（仓库元数据），不是 README 正文。README 写明可 “Identify and separate NUMTS … from genuine mitogenome contigs”，并提供 `-a {animal,plant,fungi}`。README 第 6 节题为 “New parameter for plants!!”，原话是 “MitoHiFi is still not optmized to assemble a plant mitochondria or chloroplast”（optmized 为原文拼写）。同一段写：若已经有一条被认作植物线粒体或叶绿体的 contig，可用 `-c` “to finalize your organelle”（在可环化时环化、注释并输出统计），并且 “you need to use the parameter **-a plant**”。因此 `-a plant` 是配合 `-c`、给已有植物细胞器 contig 做收尾和注释，并不是说 MitoHiFi 已经是通用的植物细胞器组装器。论文写明组装绿色植物（Viridiplantae）线粒体时应使用 `-a plant`；同一篇也写，原话是：“Although MitoHiFi was optimised to assemble metazoan mitochondrial genomes, it has performed well with Fungi where the mitochondrial genomes assembled ranged from 43 to 133 kb (Fig. 2).” 文中另一句是：“It's worth noting that MitoHiFi is not optimised to assemble plants or fungal organelles.” 接着写：“While MitoHiFi can also assemble plant mitochondria and plastid genomes, the outcomes may vary.”完整程度取决于组装图的复杂程度。论文摘要的数据是 368 种后生动物和 6 种真菌，这是该文的数据集。不要把它直接当成植物线粒体或叶绿体图组装器的替代方案；植物细胞器组装应优先使用本章和第 3 章的图组装器（PMAT/PMAT2、Oatk、HiMT、GetOrganelle）。需要近缘参考 FASTA 和 GenBank。

GetOrganelle 的 README 写明：`embplant_mt` 模式“was not tested in the GetOrganelle paper due to the complexity of plant mitogenomes and the defects of short reads.”NOVOPlasty README 当前标题为 version 4.3.3，本仓库 wrapper 里的 `NOVOPlasty4.3.1.pl` 只是示例脚本名；README 还写目前只支持双端读段、植物线粒体要用 `mito_plant` 并先组装叶绿体，以及不要做质量修剪（只去接头）。异质性检测须另引 doi:10.1093/nargab/lqz011，见第 6 章。PMAT 的 README 要求 CLR/ONT 数据先用 Canu 或 NextDenovo 纠错，打开的 README 版本段写的是 1.5.3。

## 长读长质体组装要单独看

Zhou 等（2023，第一作者是 Zhou W，不是 Wang；doi:10.1111/1755-0998.13787，全文）题为 “Plastid Genome Assembly Using Long-read data”，并发表了工具 ptGAUL。摘要写它用 ONT 或 PacBio 长读长组装质体，大约 50× 的质体覆盖度即可。选长读长质体流程时应读这篇，不要假定 Freudenthal 2020 的短读长排名可以直接用在长读长质体上。ptGAUL 的官方命令以该工具 README（https://github.com/Bean061/ptgaul，2026 年 11 月 27 日读，CST）为准：基本调用为 `ptGAUL.sh -r [PATH]/[reference_genome]/ -l [PATH]/[long_read_data]`，`-r` 为近缘物种的质体基因组，`-l` 为长读长（fasta、fastq 或 fq.gz）；可选参数有 `-t` 线程数、`-g` 预期质体大小（默认 160000）、`-c` 大致覆盖度（默认 50）、`-f` 最短读长（默认 3000）和 `-o` 输出目录。我们没有运行。

论断—出处表与英文版相同，见 [02_assembly.md](02_assembly.md)。
