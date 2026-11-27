# 6. 异质性和 RNA 编辑

没有从 2017 年 NOVOPlasty 组装论文或 Oatk 2025 摘要里抄到一句教科书式的“异质性”定义。2019/2020 年的 NOVOPlasty 异质性论文（doi:10.1093/nargab/lqz011；EuropePMC 记为 2020 年，README 写 2019 年）摘要写该方法能检测线粒体和叶绿体基因组中的个体内多态，并查看多态位点之间的连锁。下面按这个操作含义来用。更一般的生物学定义仍为 **[待确认]**。

NOVOPlasty 的 README（https://github.com/ndierckx/NOVOPlasty）自称细胞器组装器和 heteroplasmy caller。同一 README 的 Cite 段写明：若使用异质性或变异检测选项，须同时引用 2017 年组装论文（doi:10.1093/nar/gkw955）和 2019/2020 年这篇（doi:10.1093/nargab/lqz011）。2017 年那篇讲的是组装，不能单独支撑异质性检测。官方用法（README 的 MAF 说明）：第一次运行不要填 MAF，先组装；再把组装结果同时作为 reference 和 seed，并设 MAF 为 0.007–0.49。README 注明 “0.01 will detect heteroplasmy of >1%”。MAF 取 0.01 时能否检出，取决于测序深度；这是本仓库的推断，不是 README 原句。

Oatk（2025，全文）在 195 种植物的结果中讨论了异质性。Gualberto 和 Newton（2017，摘要）把核修复功能丢失与异位重组增加、基因组不稳定和异质性联系起来。第 5 章记录了 GSAT 摘要（He 等 2023）中 NUMT 会扭曲线粒体同源结构频率估计；短读长里的低频“异质性”单核苷酸是否也可能来自 NUMT/NUPT，GSAT 没有直接讲，标为 **[待确认]**。没有读到葡萄异质性频率表，任何葡萄的异质性比例都标为 **[待确认]**。

RNA 编辑先用 PREPACT 3.0（2018，全文）的原句：植物叶绿体和线粒体的基因表达受 RNA 编辑影响，有大量 C-to-U 转换，并在“some plant clades”中伴随反向的 U-to-C。葡萄线粒体里有：Picardi 等（2010，全文，doi:10.1093/nar/gkq202）在线粒体 tRNA 和 II 类内含子中报告了 44 个额外的编辑，“38 C-to-U and 6 U-to-C”；作者同时写到，Solexa/Illumina 读段给出的一些非典型编辑没有得到 SOLiD 读段支持，而另一个紧挨反密码子的 U-to-C 有 SOLiD 数据支持。葡萄质体里是否有 U-to-C，没有读到原文，标为 **[待确认]**。PREP-Mt（2005，全文）面向植物线粒体蛋白编码基因中的 C-to-U 位点。这些工具我们没有运行。PREP-Mt 摘要写预测“could reduce or even eliminate the need for experimental determination … for many sequences”；对新的葡萄材料，我们仍把转录组验证当作预测位点是否真被编辑的检查，预测能否替代验证在葡萄上标为 **[待确认]**。

论断—出处表见 [06_heteroplasmy_rna_editing.md](06_heteroplasmy_rna_editing.md)。
