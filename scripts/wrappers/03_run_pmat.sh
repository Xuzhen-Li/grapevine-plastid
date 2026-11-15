#!/usr/bin/env bash
# UNRUN wrapper: prints a command copied from a paper or GitHub README.
# This script does not assemble genomes. No organelle assembler is executed.
set -euo pipefail
DRY=0
help() {
  cat <<'EOF'
03_run_pmat.sh [--dry-run] [--help]
Prints the help invocation documented for PMAT autoMito
(https://github.com/bichangwei/PMAT, opened 2026-11-15 CST).
This prints a README autoMito demo (Arabidopsis HiFi); it is not a grape-tuned command.
CLR/ONT require Canu or NextDenovo first. Opened README Version section: 1.5.3.
UNRUN: PMAT is not executed.
EOF
}
for a in "$@"; do
  case "$a" in
    --help|-h) help; exit 0 ;;
    --dry-run) DRY=1 ;;
    *) printf 'Unknown argument: %s\n' "$a" >&2; exit 2 ;;
  esac
done
CMD='PMAT autoMito -i Arabidopsis_thaliana_550Mb.fa.gz -o ./test1 -st hifi -g 120m -m'
printf 'Source: https://github.com/bichangwei/PMAT README (autoMito / graphBuild / --type TYPE)\n'
printf 'Paper: doi:10.1093/hr/uhae023\n'
printf 'Command (not executed): %s\n' "$CMD"
printf 'Note: README autoMito demo (Arabidopsis HiFi), not grape-tuned. CLR/ONT need Canu or NextDenovo. Version in opened README: 1.5.3.\n'
printf 'graphBuild (not printed as the default command): if autoMito fails to generate the assembly graph, use graphBuild to manually select seeds.\n'
printf 'Status: UNRUN. --dry-run is the only supported mode on this machine.\n'
if [[ "$DRY" -ne 1 ]]; then
  printf 'Refusing to run: pass --dry-run. Binaries were not executed in this batch.\n' >&2
  exit 3
fi
exit 0
