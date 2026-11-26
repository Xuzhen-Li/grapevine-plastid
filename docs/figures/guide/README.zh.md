# 指南图

[English](README.md) · [知识地图](../../KNOWLEDGE_MAP.zh.md)

为[知识地图](../../KNOWLEDGE_MAP.zh.md)配的四张图。图 1 和图 2 原样取自开放获取论文；图 3 和图 4 是 [`make_guide_figures.py`](make_guide_figures.py) 绘制的示意图。

## 图的署名

| 编号 | 文件 | 署名 | 许可 |
|---|---|---|---|
| 1 | `01_plastome_map_zheng2020_fig2.jpg` | Zheng S, Poczai P, Hyvönen J, Tang J, Amiryousefi A (2020). Chloroplot: an online program for the versatile plotting of organelle genomes. *Frontiers in Genetics* 11:576124，图 2（豚草 *Ambrosia trifida* 的叶绿体基因组图）。[doi:10.3389/fgene.2020.576124](https://doi.org/10.3389/fgene.2020.576124) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，原样转载 |
| 2 | `02_mito_isoforms_kozik2019_fig2.png` | Kozik A, Rowan BA, Lavelle D, Berke L, Schranz ME, Michelmore RW, Christensen AC (2019). The alternative reality of plant mitochondrial DNA: one ring does not rule them all. *PLOS Genetics* 15(8):e1008373，图 2（*Lactuca* 线粒体基因组的异构体）。[doi:10.1371/journal.pgen.1008373](https://doi.org/10.1371/journal.pgen.1008373) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，原样转载 |
| 3 | `03_organelle_concepts_schematic.png` | 由 `make_guide_figures.py` 为本仓库绘制（示意形状；质体各区长度和 113 个不重复基因的计数取自 Jansen 等 2006，[doi:10.1186/1471-2148-6-32](https://doi.org/10.1186/1471-2148-6-32)） | CC BY 4.0（见 [`NOTICE.zh.md`](../../../NOTICE.zh.md)） |
| 4 | `04_reference_route.png` | 由 `make_guide_figures.py` 为本仓库绘制 | CC BY 4.0（见 [`NOTICE.zh.md`](../../../NOTICE.zh.md)） |

图 1 和图 2 的许可是这样确认的：PubMed Central 全文 XML 的许可字段（PMC7545089 和 PMC6742443）和 Crossref 记录都给出 CC BY 4.0 的许可网址 https://creativecommons.org/licenses/by/4.0/（版本 4.0）；Europe PMC 记录只写 “cc by”，没有版本号。图片文件就是出版社为这些图提供的文件：图 1 是 Frontiers 网站上的图（JPEG，645,258 字节，sha256 `610d80f28724c5aae228d5ea4d2c143459806371f3cabd473a11d94f1665a603`），图 2 是 PLOS 的 “large” 图（PNG，386,819 字节，sha256 `1c853c218a080f4e6da35d1c045613219840394dd848684d137200786572799d`），其像素与 PLOS 为同一张图提供的原始 TIFF 完全相同。

## 图注

1. **质体基因组图。** 豚草质体基因组的环状图：中心是物种名、基因组长度、GC 含量和基因数；四个区（LSC、SSC、IRa、IRb）及其长度、GC 含量，基因按功能类别着色。它展示质体基因组如何画成四段。论文中的图注为 “Chloroplast genome map of giant ragweed (*Ambrosia trifida* L.).”
2. **线粒体异构体。** A 图是 *Lactuca sativa* 线粒体基因组的两个主要异构体，它们因正向重复之间重组而交换了单元；B 图是 *L. saligna* 经反向重复产生的主要异构体和重组产物。论文中的图注为 “Isoforms of *Lactuca* mitochondrial genomes.”
3. **概念总览。** A：*Vitis vinifera* 的四段质体基因组，使用真实的区长度（LSC 89,147 bp，每份 IR 26,358 bp，SSC 19,065 bp；共 160,928 bp），并标出 IR 移动时会移动的连接点。B：一个主环，其中两个重复序列重组成两个子环。C：插入核染色体的质体和线粒体 DNA 片段（NUPT、NUMT）。D：一次产生 AUG 的 C 到 U 编辑，以及一个个体中的两种细胞器单倍型。除质体各区长度和 113 个不重复基因这一计数（Jansen 等 2006）外，其余都是示意。
4. **参考流程图。** 参考流程的八个步骤和示例工具；顺序只是指引，不是固定流水线。

## 打印尺寸与可读性

图 3 和图 4 宽 1600 像素，按 183 mm 宽打印设计（222 dpi，写在 PNG 文件里；图 3 高 1480 像素，约 169 mm，图 4 高 1040 像素，约 119 mm）。最小的字是 20 像素，在该宽度下是 6.5 pt；在屏幕上按像素大小阅读。文字颜色与其背景色的对比度至少为 4.5:1。

## 重新绘制示意图

`make_guide_figures.py` 只需要 Pillow 和 DejaVu 字体（路径固定为 `/usr/share/fonts/truetype/dejavu/`）。两张示意图是用 Pillow 12.3.0 绘制的，用下面的命令可以逐字节重现：

```
python3 make_guide_figures.py OUTDIR
```

脚本不会覆盖已存在的文件。若有文字小于 20 像素、超出所在框线，或与背景色的对比度低于 4.5:1，脚本也会停止。脚本按 MIT 许可发布（见 [`LICENSE`](../../../LICENSE)）。
