#!/usr/bin/env bash
# UNRUN wrapper: prints a command copied from a paper or GitHub README.
# This script does not assemble genomes. No organelle assembler is executed.
set -euo pipefail
DRY=0
help() {
  cat <<'EOF'
05_run_himt.sh [--dry-run] [--help]
Prints the assemble example from the HiMT README
(https://github.com/tang-shuyuan/HiMT, opened 2026-11-15 CST).
This prints a README example; it is not a grape-tuned command.
UNRUN: HiMT is not executed. The paper states it is freely available to non-commercial users.
EOF
}
for a in "$@"; do
  case "$a" in
    --help|-h) help; exit 0 ;;
    --dry-run) DRY=1 ;;
    *) printf 'Unknown argument: %s\n' "$a" >&2; exit 2 ;;
  esac
done
CMD='himt assemble -i hifi.fa -o output_dir -t 10'
printf 'Source: https://github.com/tang-shuyuan/HiMT README\n'
printf 'Paper: doi:10.1016/j.xplc.2025.101467\n'
printf 'Command (not executed): %s\n' "$CMD"
printf 'Note: README example only, not grape-tuned.\n'
printf 'Status: UNRUN. --dry-run is the only supported mode on this machine.\n'
if [[ "$DRY" -ne 1 ]]; then
  printf 'Refusing to run: pass --dry-run. Binaries were not executed when this script was written.\n' >&2
  exit 3
fi
exit 0
