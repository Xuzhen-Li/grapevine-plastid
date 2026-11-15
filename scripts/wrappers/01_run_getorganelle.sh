#!/usr/bin/env bash
# UNRUN wrapper: prints a command copied from a paper or GitHub README.
# This script does not assemble genomes. No organelle assembler is executed.
set -euo pipefail
DRY=0
help() {
  cat <<'EOF'
01_run_getorganelle.sh [--dry-run] [--help]
Prints the embplant plastome example from the GetOrganelle README
(https://github.com/Kinggerm/GetOrganelle, opened 2026-11-15 CST).
This prints a README example; it is not a grape-tuned command.
UNRUN: GetOrganelle is not executed.
EOF
}
for a in "$@"; do
  case "$a" in
    --help|-h) help; exit 0 ;;
    --dry-run) DRY=1 ;;
    *) printf 'Unknown argument: %s\n' "$a" >&2; exit 2 ;;
  esac
done
CMD='get_organelle_from_reads.py -1 forward.fq -2 reverse.fq -o plastome_output -R 15 -k 21,45,65,85,105 -F embplant_pt'
printf 'Source: https://github.com/Kinggerm/GetOrganelle README\n'
printf 'Paper: doi:10.1186/s13059-020-02154-5\n'
printf 'Command (not executed): %s\n' "$CMD"
printf 'Note: README example only, not grape-tuned. embplant_mt was not tested in the GetOrganelle paper.\n'
printf 'Status: UNRUN. --dry-run is the only supported mode on this machine.\n'
if [[ "$DRY" -ne 1 ]]; then
  printf 'Refusing to run: pass --dry-run. Binaries were not executed in this batch.\n' >&2
  exit 3
fi
exit 0
