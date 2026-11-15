#!/usr/bin/env bash
# UNRUN wrapper: prints a command copied from a paper or GitHub README.
# This script does not assemble genomes. No organelle assembler is executed.
set -euo pipefail
DRY=0
help() {
  cat <<'EOF'
02_run_novoplasty.sh [--dry-run] [--help]
Prints the command from the NOVOPlasty README
(https://github.com/ndierckx/NOVOPlasty, opened 2026-11-15 CST).
This prints a README example; it is not a grape-tuned command.
The script name NOVOPlasty4.3.1.pl is copied from an older README example; the README opened 2026-11-15 CST is titled version 4.3.3.
Heteroplasmy calling is a separate option (doi:10.1093/nargab/lqz011).
UNRUN: NOVOPlasty is not executed.
EOF
}
for a in "$@"; do
  case "$a" in
    --help|-h) help; exit 0 ;;
    --dry-run) DRY=1 ;;
    *) printf 'Unknown argument: %s\n' "$a" >&2; exit 2 ;;
  esac
done
CMD='perl NOVOPlasty4.3.1.pl -c config.txt'
printf 'Source: https://github.com/ndierckx/NOVOPlasty README\n'
printf 'Paper: doi:10.1093/nar/gkw955\n'
printf 'Command (not executed): %s\n' "$CMD"
printf 'Note: README example only, not grape-tuned. Example script name is 4.3.1; README title is 4.3.3. PE only; do not quality-trim; plant mt = mito_plant after cp assembly. Heteroplasmy: doi:10.1093/nargab/lqz011.\n'
printf 'Status: UNRUN. --dry-run is the only supported mode on this machine.\n'
if [[ "$DRY" -ne 1 ]]; then
  printf 'Refusing to run: pass --dry-run. Binaries were not executed in this batch.\n' >&2
  exit 3
fi
exit 0
