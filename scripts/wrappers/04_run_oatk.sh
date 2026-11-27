#!/usr/bin/env bash
# UNRUN wrapper: prints a command copied from a paper or GitHub README.
# This script does not assemble genomes. No organelle assembler is executed.
set -euo pipefail
DRY=0
help() {
  cat <<'EOF'
04_run_oatk.sh [--dry-run] [--help]
Prints the Arabidopsis HiFi example from the Oatk README
(https://github.com/c-zhou/oatk, opened 2026-11-15 CST).
This prints the Arabidopsis HiFi example from the README; it is not a grape-tuned command.
Oatk is documented for PacBio HiFi only. -c 30 is the Arabidopsis example; README says set -c as 5-10 times nuclear coverage.
UNRUN: Oatk is not executed.
EOF
}
for a in "$@"; do
  case "$a" in
    --help|-h) help; exit 0 ;;
    --dry-run) DRY=1 ;;
    *) printf 'Unknown argument: %s\n' "$a" >&2; exit 2 ;;
  esac
done
CMD='oatk -k 1001 -c 30 -t 8 --nhmmscan /bin/nhmmscan -m embryophyta_mito.fam -p embryophyta_pltd.fam -o ddAraThal4 ddAraThal4_organelle.hifi.fa.gz'
printf 'Source: https://github.com/c-zhou/oatk README\n'
printf 'Paper: doi:10.1186/s13059-025-03676-6\n'
printf 'Command (not executed): %s\n' "$CMD"
printf 'Note: README Arabidopsis HiFi example, not grape-tuned. HiFi only. -c 30 is the Arabidopsis demo; README: set -c as 5-10× nuclear coverage to help filter nuclear sequence and NUMTs.\n'
printf 'Status: UNRUN. --dry-run is the only supported mode on this machine.\n'
if [[ "$DRY" -ne 1 ]]; then
  printf 'Refusing to run: pass --dry-run. Binaries were not executed when this script was written.\n' >&2
  exit 3
fi
exit 0
