# 3. 组装图和多种构型

植物线粒体 DNA 往往更适合用图来报告，而不是画成一个环。以下只使用本批次打开过的论文和 README。

Kozik 等（2019，全文）的题名就是 “One ring does not rule them all”。Gualberto 和 Newton（2017，摘要）从生物学上说明：重复序列之间的重组会产生亚基因组形式，同种之内也可以有很大结构差异。Fischer 等（2022，全文，doi:10.1093/nargab/lqac027）用月见草线粒体基因组给出了图模型的实例。

He 等（2023，第一作者是 He W，不是 Wang；仅摘要，doi:10.1093/bib/bbac522）介绍了 GSAT 和 mitochondrial master graph（MMG），水稻和拟南芥的 MMG 长度分别为 346,562 和 358,041 bp，并给出了 contig、连接、主环和次环的数目。我们没有打开这篇的全文。

GetOrganelle 摘要写它会整理组装图并给出环状基因组的所有可能构型，全文还提到带标记的组装图便于人工补全。Oatk 摘要写它在组装图中寻找 “best supported path”。PMAT 的 README 在 `autoMito` 失败时提供 `graphBuild`，意味着图上有时需要人工选种子。Hou 等（JIPB 2025）的图 S1 是用 Bandage 画的 33 份葡萄叶绿体泛结构，这是已发表的可视化例子，不是新的组装器。Bandage（Wick 等 2015，全文及 README）用于交互查看从头组装图。

PMAT 的 README 对 graphBuild 的中性表述是：autoMito 无法生成组装图时，可用该命令手动选择种子。Bandage 的全称出自项目主页和 GitHub 仓库描述，当前 README 正文的说法是可交互查看组装图的 GUI。推荐报告主图（GFA）还是某条线性化路径、以及路径依据（Oatk 的 best-supported path，GetOrganelle 的全部环状构型），见英文版新增小节。图 F2 现已把 GetOrganelle 和 Oatk 也连到图查看。

论断—出处表见 [03_graphs_conformations.md](03_graphs_conformations.md)。
