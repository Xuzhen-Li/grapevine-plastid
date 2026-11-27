#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse
import sys

def write_x(path: Path, text: str) -> None:
    if path.exists():
        raise FileExistsError(path)
    if not text.endswith('\n'):
        text += '\n'
    with path.open('x', encoding='utf-8') as f:
        f.write(text)

def wrap(w, h, title, body, cap1, cap2):
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">',
        f'  <title>{title}</title>',
        f'  <rect width="{w}" height="{h}" fill="#fffef8"/>',
        f'  <text x="24" y="32" font-family="Georgia, serif" font-size="18" fill="#1a1a1a">{title}</text>',
        body,
        f'  <text x="24" y="{h-28}" font-family="Georgia, serif" font-size="11" fill="#333">{cap1}</text>',
        f'  <text x="24" y="{h-12}" font-family="Georgia, serif" font-size="11" fill="#333">{cap2}</text>',
        '</svg>',
    ]
    return '\n'.join(parts) + '\n'

def fig1(out: Path) -> None:
    body = '\n'.join([
        '<circle cx="360" cy="230" r="132" fill="none" stroke="#2c5f2d" stroke-width="26"/>',
        '<circle cx="360" cy="230" r="132" fill="none" stroke="#3d7a40" stroke-width="26" stroke-dasharray="460 370" transform="rotate(-90 360 230)"/>',
        '<circle cx="360" cy="230" r="132" fill="none" stroke="#c9842a" stroke-width="26" stroke-dasharray="0 460 136 330" transform="rotate(-90 360 230)"/>',
        '<circle cx="360" cy="230" r="132" fill="none" stroke="#2a6f97" stroke-width="26" stroke-dasharray="0 596 98 140" transform="rotate(-90 360 230)"/>',
        '<circle cx="360" cy="230" r="132" fill="none" stroke="#c9842a" stroke-width="26" stroke-dasharray="0 694 136 0" transform="rotate(-90 360 230)"/>',
        '<circle cx="360" cy="230" r="78" fill="#fffef8"/>',
        '<text x="360" y="218" text-anchor="middle" font-family="Georgia, serif" font-size="14">Vitis vinifera</text>',
        '<text x="360" y="238" text-anchor="middle" font-family="Georgia, serif" font-size="13">plastome</text>',
        '<text x="360" y="256" text-anchor="middle" font-family="Georgia, serif" font-size="12">160,928 bp</text>',
        '<rect x="560" y="120" width="18" height="18" fill="#3d7a40"/>',
        '<text x="586" y="134" font-family="Georgia, serif" font-size="13">LSC 89,147 bp</text>',
        '<rect x="560" y="150" width="18" height="18" fill="#c9842a"/>',
        '<text x="586" y="164" font-family="Georgia, serif" font-size="13">IR (x2) 26,358 bp each</text>',
        '<rect x="560" y="180" width="18" height="18" fill="#2a6f97"/>',
        '<text x="586" y="194" font-family="Georgia, serif" font-size="13">SSC 19,065 bp</text>',
        '<text x="24" y="400" font-family="Georgia, serif" font-size="12">113 unique genes; 18 duplicated in the IR; 131 genes in total.</text>',
    ])
    write_x(out, wrap(820, 460, 'F1. Four-part Vitis plastome (schematic)', body,
                      'Numbers from Jansen et al. 2006, doi:10.1186/1471-2148-6-32, full text.',
                      'Original schematic, not a reprint of their Fig. 1.'))

def labeled_rect(x,y,w,h,label,fill):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#222" stroke-width="1.2"/>'
        f'<text x="{x+w/2}" y="{y+h/2+5}" text-anchor="middle" font-family="Georgia, serif" font-size="13">{label}</text>'
    )

def arrow(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#222" stroke-width="1.6" marker-end="url(#arr)"/>'

def fig2(out: Path) -> None:
    # Separate PacBio HiFi from CLR/ONT so Oatk is not drawn as a CLR/ONT tool.
    # Graph-view arrows also leave GetOrganelle and Oatk, not only PMAT.
    body = '\n'.join([
        '<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#222"/></marker></defs>',
        labeled_rect(40, 60, 180, 44, 'Illumina WGS / skimming', '#e8f0e8'),
        labeled_rect(40, 180, 180, 44, 'PacBio HiFi', '#e8eef6'),
        labeled_rect(40, 300, 180, 44, 'CLR / ONT', '#d9e0ea'),
        labeled_rect(300, 40, 230, 36, 'GetOrganelle (Jin 2020)', '#cfe3cf'),
        labeled_rect(300, 86, 230, 36, 'NOVOPlasty (2017)', '#cfe3cf'),
        labeled_rect(300, 160, 230, 36, 'Oatk (Zhou 2025, HiFi only)', '#c9d7ea'),
        labeled_rect(300, 230, 230, 36, 'PMAT / PMAT2 (2024/25)', '#c9d7ea'),
        labeled_rect(300, 300, 230, 36, 'HiMT (Tang 2025)', '#c9d7ea'),
        labeled_rect(600, 160, 190, 48, 'Bandage graph view', '#f3e2c4'),
        # Illumina -> short-read tools
        arrow(220, 82, 300, 58),
        arrow(220, 82, 300, 104),
        # HiFi -> Oatk, PMAT, HiMT
        arrow(220, 202, 300, 178),
        arrow(220, 202, 300, 248),
        arrow(220, 202, 300, 318),
        # CLR/ONT -> PMAT and HiMT, not Oatk
        arrow(220, 322, 300, 248),
        arrow(220, 322, 300, 318),
        # graphs -> Bandage from GetOrganelle, Oatk, PMAT
        arrow(530, 58, 600, 170),
        arrow(530, 178, 600, 184),
        arrow(530, 248, 600, 198),
    ])
    write_x(out, wrap(820, 480, 'F2. Assembly routes (schematic)', body,
                      'Oatk is HiFi-only (README). CLR/ONT into PMAT need Canu or NextDenovo first.',
                      'Bandage is also a graph view for GetOrganelle and Oatk, not only PMAT. Original flowchart.'))

def X(kb):
    return 80 + kb * (620/900)

def bar(y, x0, x1, color, label):
    return '\n'.join([
        f'<line x1="{X(0)}" y1="{y}" x2="{X(900)}" y2="{y}" stroke="#ccc" stroke-width="1"/>',
        f'<rect x="{X(x0)}" y="{y-10}" width="{X(x1)-X(x0)}" height="20" fill="{color}" stroke="#222"/>',
        f'<text x="80" y="{y-18}" font-family="Georgia, serif" font-size="13">{label}</text>',
        f'<text x="{X(x0)}" y="{y+28}" font-family="Georgia, serif" font-size="11">{x0:g}</text>',
        f'<text x="{X(x1)-10}" y="{y+28}" font-family="Georgia, serif" font-size="11">{x1:g} kb</text>',
    ])

def fig3(out: Path) -> None:
    ticks = []
    for kb in range(0, 901, 150):
        x = X(kb)
        ticks.append(f'<line x1="{x}" y1="340" x2="{x}" y2="350" stroke="#333"/>')
        ticks.append(f'<text x="{x}" y="366" text-anchor="middle" font-family="Georgia, serif" font-size="11">{kb}</text>')
    body = '\n'.join([
        bar(120, 159.011, 163.619, '#3d7a40', 'Plastid genomes, 33 Vitis accessions (159,011-163,619 bp)'),
        bar(200, 663.16, 817.37, '#8b3a2a', 'Mitochondrial genomes, 33 Vitis accessions (663.16-817.37 kb)'),
        '<text x="80" y="270" font-family="Georgia, serif" font-size="13">NUMTs 212-431; NUPTs 95-205 (same 33-accession study).</text>',
        '<text x="80" y="292" font-family="Georgia, serif" font-size="13">Grapepan_mt v.1.0 = 1.28 Mb; Grapepan_cp v.1.0 = 138 kb.</text>',
        '<text x="390" y="385" text-anchor="middle" font-family="Georgia, serif" font-size="12">Scale in kb</text>',
    ] + ticks)
    write_x(out, wrap(820, 430, 'F3. Vitis organelle size ranges (JIPB 2025)', body,
                      'Ranges from Hou et al., JIPB 2025, doi:10.1111/jipb.13968, full text.',
                      'Original chart, not a journal reprint.'))

def fig4(out: Path) -> None:
    body = '\n'.join([
        '<ellipse cx="240" cy="210" rx="90" ry="60" fill="none" stroke="#8b3a2a" stroke-width="3"/>',
        '<ellipse cx="360" cy="210" rx="90" ry="60" fill="none" stroke="#8b3a2a" stroke-width="3"/>',
        '<circle cx="300" cy="210" r="10" fill="#8b3a2a"/>',
        '<text x="300" y="198" text-anchor="middle" font-family="Georgia, serif" font-size="11">repeat</text>',
        '<text x="240" y="300" text-anchor="middle" font-family="Georgia, serif" font-size="13">alternative paths</text>',
        '<text x="560" y="140" font-family="Georgia, serif" font-size="13">A single master circle is not the</text>',
        '<text x="560" y="160" font-family="Georgia, serif" font-size="13">default description of plant mtDNA</text>',
        '<text x="560" y="180" font-family="Georgia, serif" font-size="13">(Kozik et al. 2019).</text>',
        '<text x="560" y="220" font-family="Georgia, serif" font-size="13">GetOrganelle reports all circular</text>',
        '<text x="560" y="240" font-family="Georgia, serif" font-size="13">configurations it can disentangle.</text>',
        '<text x="560" y="280" font-family="Georgia, serif" font-size="13">Oatk searches for a best-supported</text>',
        '<text x="560" y="300" font-family="Georgia, serif" font-size="13">path through the assembly graph.</text>',
    ])
    write_x(out, wrap(820, 400, 'F4. Plant mitogenome as a graph (schematic)', body,
                      'Sources: doi:10.1371/journal.pgen.1008373; doi:10.1186/s13059-020-02154-5;',
                      'doi:10.1186/s13059-025-03676-6. Schematic only, not a reprint.'))

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--outdir', required=True)
    args = ap.parse_args(argv)
    outdir = Path(args.outdir)
    targets = [
        outdir / 'F1_vitis_plastome_four_part.svg',
        outdir / 'F2_assembly_routes.svg',
        outdir / 'F3_vitis_organelle_size_ranges.svg',
        outdir / 'F4_mitogenome_graph_schematic.svg',
    ]
    if not outdir.exists():
        outdir.mkdir()
    missing = [p for p in targets if p.exists()]
    if missing:
        print('refusing to write; already present:', *missing, sep='\n  ', file=sys.stderr)
        sys.exit(2)
    fig1(targets[0])
    fig2(targets[1])
    fig3(targets[2])
    fig4(targets[3])
    print('wrote 4 SVGs in', outdir)

if __name__ == '__main__':
    main()
