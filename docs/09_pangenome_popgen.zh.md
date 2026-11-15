# 9. 细胞器泛基因组和群体数据

这一章只写读过的论文里，细胞器基因组怎样被用在泛基因组和群体分析中，不另外编一套葡萄细胞器泛基因组流程。把叶绿体多态性读成葡萄的母系谱系，在第 7 章有原文之前标为 **[待确认]**。

Hou 等（JIPB 2025，全文）用 33 份长读长组装明确做了泛线粒体基因组 Grapepan_mt v.1.0（1.28 Mb，大约相当于单份线粒体基因组的两倍，来自参考 Bmng 的 144 个片段）和泛质体基因组 Grapepan_cp v.1.0（138 kb，作者写大约与单份质体相当，31 个片段）。他们把这些图和单倍型解析的核基因组一起，统计 NUMT/NUPT 并做核质互作的 GWAS（第 5 章）。图 S1 是用 Bandage 画的泛叶绿体结构。若要在公开 HPC 上按方法级重做，该文可见的步骤是：每份材料做长读长细胞器组装、把 33 份细胞器基因组做成并集或图、用核长读长或组装去调用 NUMT/NUPT、再做关联分析。具体软件版本和参数应回该文 Methods（我们打开过全文），本章不重打未经核对的命令行。这里也不放入任何私有实验室目录。

更早的工作把叶绿体多态性当作群体标记：Arroyo-García 等（2006，摘要）讨论栽培葡萄多次起源；Tabidze 等（2014，摘要）发表 11 个品种、四个单倍型组的完整质体；2018 年 PLOS ONE（全文）看野生葡萄叶绿体型；IJMS 2026（全文）在 409 个品种里报告 93 个 SNV（第 8 章）。这些是以质体为标记的群体遗传，不是泛基因组图。

Wu 等（2022，摘要）写当时完整发表的陆地植物线粒体基因组大约只有 200 套，不少还是草稿组装，并建议在群体水平上看结构变异。这是综述建议，不是葡萄数据集。

同一篇 JIPB 的 Materials and Methods 写明：长读长先用 minimap2 v2.26 比对参考线粒体 NC_012119.1，再用 Flye v2.9.2-b1786 组装，质体用类似策略；泛基因组用 minigraph-0.13 (r397)；注释用 Geseq [sic]（Tillich 2017 题名作 GeSeq）；线粒体重复用 REPuter，共线性用 NUCmer v3.1 和 Mummerplot。群体部分对 100 份重测序用 BWA v0.7.17、SAMtools v1.13、GATK v4.2.3.0、GLnexus v1.2.7 和 VCFtools v0.1.16（1,000 bp 窗口、500 bp 步长）。本仓库的 wrapper 只是打印 README 示例，不是为葡萄调过的命令，也没有实际运行。

同一篇 Materials and Methods 里的工具名和版本，已对照 JIPB 2025 全文（PMC12498075，本轮重新打开）逐条核对，均取自原文：minimap2 v2.26、Flye v2.9.2-b1786、minigraph-0.13 (r397)、Geseq（Tillich 等 2017；Methods 原文拼写为 “Geseq” [sic]，Tillich 2017 题名作 “GeSeq”；该段未给版本号）、REPuter（未给版本号；原文参数为 Edit distance 3、Minimal Repeat Size 30 bp）、NUCmer v3.1、Mummerplot（未给版本号）、BWA v0.7.17-r1188、SAMtools v1.13、GATK v4.2.3.0、GLnexus v1.2.7（DeepVariantWGS 配置），以及 VCFtools v0.1.16（1,000 bp 窗口、500 bp 步长）。同一群体段还保留 DP 大于 2、缺失率小于 0.1 的位点；上一版没有写进正文，这里补上。同一 Methods 的 GWAS 小节用的是 GATK v.4.2.6.0，不要和上面 100 份重测序的 v4.2.3.0 混写。

把细胞器基因组当作泛基因组单倍型或群体标记来读时，通常还依赖下面几条工作假设，这里写出来是为了核对，不是把它们说成已经在葡萄里成立：

1. **单亲（常常是母系）遗传。** 第 7 章已记录 Birky（2001，摘要）的单亲遗传和重组减少，以及 2026 年 JXB 综述在其讨论的被子植物例子里把细胞器当作母系遗传。葡萄质体或线粒体是否严格母系遗传，仍为 **[待确认]**（第 7 章）。在有原文之前，不要把本章的叶绿体型或线粒体型读成母系谱系。
2. **重组很少或没有，因而单倍型可当作不重组的谱系。** Birky（2001，摘要）写的是 “reduced recombination”，并不等于“无重组”。Gualberto 和 Newton（2017，摘要；第 6 章）把核修复功能丢失与异位重组增加、基因组不稳定和异质性联系起来。Woloszynska（2010，*J. Exp. Bot.*，刊期 2010，在线 2009-12-08；摘要；doi:10.1093/jxb/erp361）综述植物线粒体异质性，并写 “uniparentally inherited plant mitochondrial genomes which do not undergo sexual recombination”，同时写 “Alternative mitochondrial genomes may recombine, yielding new mtDNA variants.” 某一份葡萄细胞器数据能否按不重组来处理，标为 **[待确认]**。
3. **异质性低到可以忽略，或已被建模。** Woloszynska（2010，摘要）把植物线粒体异质性看作植物中的常见情况，包括主基因组和亚化学计量的 sublimons。第 6 章写明本批次没有打开葡萄异质性频率表，任何葡萄的异质性比例都是 **[待确认]**。若分析为每份材料只输出一个单倍型，等于假定这个问题可以忽略或已经处理；本章并不做这个断定。
4. **拷贝数和覆盖度过滤属于该文中已写明的小节，不能当成同一套流程。** JIPB 2025 的 Methods（PMC12498075，此前已打开，本轮复核）用测序深度来辅助识别 NUMT/NUPT：NUMT 区的理论深度 = 核基因组平均深度 + 线粒体平均深度，NUPT 则加上叶绿体平均深度，再用 IGV 查看 HiFi 读段。这一步与下面的变异过滤不是同一段分析。

计算 π 和 F_ST 的群体遗传小节以 “Vs” mitogenome 作为 SNP 和 INDEL 识别的参考，只保留 “SNPs and INDELs with depths (DP) greater than 2 and maximum missing rates less than 0.1”。该小节没有为用于 π 和 F_ST 的变异再设深度上限，也没有 NUMT 过滤。DP>2 是 INFO 还是 FORMAT 口径，标为 **[待确认]**。细胞器覆盖度通常很高，这一阈值在实践中可能几乎不起过滤作用，不宜当作复现参数（本仓库推断）。

同一小节采用 “a 1,000-bp sliding window and 500-bp steps” 计算 π 和 F_ST。相邻窗口因此重叠一半，彼此不独立（本仓库的说明；原文没有讨论这种不独立性）。选择清除区间的判据原文为：“the top F<sub>ST</sub> must be greater than 0.1, and the π<sub>wild</sub>/π<sub>cul</sub> ratio must be greater than 1 based on common SNPs in the grape mitogenomes.” 这两个门槛是 Methods 里写出的经验阈值，原文没有推导。

1.5 倍深度上限、至少 4 条 reads、MAF≥0.05、missing<0.2 只属于同一 Methods 里单独的 GWAS 小节。1.5 倍那句以大写 To 起首，原文为：“To eliminate the risk of false positives arising from the presence of multiple copies, we assessed the depth of coverage for each mitochondrial variant and compared it to the average depth across the whole mitochondrial genome. Variants with coverage depths exceeding 1.5 times the mean depth were excluded (Lian et al., 2024).” 1.5 倍阈值在该文中引自 Lian et al. 2024（msae028），本批次没有打开该文，标为 **[待确认]**。同一 GWAS 小节还 “filtered out mitochondrial SNPs that were supported by fewer than four reads”，并用 “PLINK with MAF ≥ 0.05 and missing < 0.2” 得到高质量变异。缺失率 0.2 只属于 GWAS 小节，不能与 π / F_ST 所用的 0.1 混写。GWAS 小节使用 GATK v.4.2.6.0；100 份重测序那段使用 GATK v4.2.3.0（上文已记录）。

“拷贝数和覆盖度是该文过滤步骤的一部分” 是本仓库的推断：它适用于上文的 NUMT/NUPT 识别和 GWAS 小节，不能理解为 π / F_ST 分析也做了 GWAS 的深度上限过滤。

5. **用二倍体模型给单倍体细胞器做基因型。** 这样可能得到杂合位点，来源可以是异质性或 NUMT。这是本仓库的推断，不是 JIPB Methods 里的原句。

论断—出处表见 [09_pangenome_popgen.md](09_pangenome_popgen.md)。
