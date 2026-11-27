# 5. NUMT 和 NUPT

GSAT 摘要（He 等 2023，第一作者是 He W，不是 Wang；题为 “Master graph: an essential integrated assembly model for the plant mitogenome based on a graph-based framework,” doi:10.1093/bib/bbac522）给出了定义用语：NUMT 是核线粒体 DNA 片段，MTPT 是线粒体中的质体 DNA 片段。本章采用：NUMT 是核基因组里的线粒体来源片段；NUPT 是核基因组里的质体来源片段；MTPT 是线粒体基因组里的质体来源片段。前两个在核里，第三个在线粒体里。

2026 年 *The Plant Journal* 综述（全文，doi:10.1111/tpj.70685）题为质体来源的核 DNA（NUPT）。摘要写：植物核基因组里通常只有少量质体来源片段；与内共生时大规模的基因转移不同，NUPT 的形成是持续发生的，并不意味着质体一定同时丢掉这些 DNA。综述还写，NUPT 与某些转座子超家族有偏好重叠，并在一些非编码 RNA 基因类别中富集。这是综述作者的判断，我们只引用，不重新计算。

Hou 等（JIPB 2025，全文）在 33 份葡萄材料上报告：共检测到 212–431 个 NUMT 和 95–205 个 NUPT；NUMT 在栽培葡萄中更多且他们写受到强选择，NUPT 则在野生葡萄中占主导。GWAS 找到 84 个与线粒体—核互作相关的候选基因，其中包括 *PFD1*，并且互作基因更常出现在 NUMT 附近。

Oatk（2025，摘要）在 195 种植物的结果中提到细胞器之间的 DNA 交换，这是跨物种观察，不是葡萄的计数。GSAT 摘要（2023）写拟南芥中 NUMT 会明显影响同源结构频率的估计，MTPT 则不影响 MMG 评估；我们只有摘要。

同一篇 GSAT 摘要后半句是 “while the effects of NUMTs in rice were relatively weak”，应与拟南芥那一半一起读，不要写成 NUMT 在各物种影响都一样强。

组装时把核来源片段排除出细胞器组装，和细胞核里真实存在的 NUMT/NUPT，是两类问题。已打开的资料里的做法包括：Oatk 的 `-c` 取核覆盖度的 5–10 倍；MitoHiFi 的 NUMT 分离步骤（但其 README 第 6 节原话是 “still not optmized to assemble a plant mitochondria or chloroplast”，`-a plant` 只与 `-c` 配合给已有 contig 收尾；论文写植物上 outcomes may vary，不能直接替代植物图组装器的过滤步骤）；GetOrganelle 的图过滤。对某一份葡萄数据是否足够，标为 **[待确认]**。

论断—出处表见 [05_numt_nupt.md](05_numt_nupt.md)。
