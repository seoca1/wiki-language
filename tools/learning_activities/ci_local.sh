#!/bin/bash
# scripts/ci_local.sh — Run all CI checks locally (mirror of GitHub Actions).
#
# Usage:
#   bash scripts/ci_local.sh           # run all
#   bash scripts/ci_local.sh fiction   # only fiction-verify
#   bash scripts/ci_local.sh lint      # only vault-lint
#   bash scripts/ci_local.sh dashboard # only dashboard-build
#
# Exit codes:
#   0 = all checks pass
#   1 = one or more checks failed

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Colors
RED=$'\033[0;31m'
GREEN=$'\033[0;32m'
YELLOW=$'\033[0;33m'
BOLD=$'\033[1m'
RESET=$'\033[0m'

# Track results
RESULTS=()

run_fiction_verify() {
    echo
    echo "${BOLD}=== fiction-verify ===${RESET}"
    local exit_code=0

    if ! python3 Fiction/tools/verify_derivative.py --all; then
        echo "${RED}✗ verify_derivative FAIL${RESET}"
        exit_code=1
    else
        echo "${GREEN}✓ verify_derivative PASS${RESET}"
    fi

    if ! python3 Fiction/tools/verify_mission_sync.py; then
        echo "${RED}✗ verify_mission_sync FAIL${RESET}"
        exit_code=1
    else
        echo "${GREEN}✓ verify_mission_sync PASS${RESET}"
    fi

    if ! python3 Fiction/tools/verify_3way_consistency.py --all; then
        echo "${RED}✗ verify_3way_consistency FAIL${RESET}"
        exit_code=1
    else
        echo "${GREEN}✓ verify_3way_consistency PASS${RESET}"
    fi

    if ! python3 Fiction/tools/story_check.py --all > story_check_output.txt 2>&1; then
        echo "${RED}✗ story_check FAIL${RESET}"
        exit_code=1
    else
        if grep -E "^Fiction/derivative.*grade:.*[BCDEF] " story_check_output.txt; then
            echo "${RED}✗ B/C/D/F grade stories detected — must be A${RESET}"
            exit_code=1
        else
            echo "${GREEN}✓ story_check A-only PASS${RESET}"
        fi
    fi

    RESULTS+=("fiction-verify: $([ $exit_code -eq 0 ] && echo PASS || echo FAIL)")
    return $exit_code
}

run_vault_lint() {
    echo
    echo "${BOLD}=== vault-lint ===${RESET}"
    local exit_code=0

    python3 -c "
import re, sys
from pathlib import Path

EXCLUDE = {'.git', 'node_modules', '.obsidian', '.pytest_cache', '.ruff_cache', '.mypy_cache', 'venv', '.venv', '.github'}

def load_tracked_broken():
    tracked = set()
    inv = Path('Language/wiki/_inventory/BROKEN_WIKILINKS_2026-07-11.md')
    if inv.exists():
        for m in re.finditer(r'\[\[([^\]]+)\]\]', inv.read_text()):
            tracked.add(m.group(1).strip())
    return tracked

tracked = load_tracked_broken()

def lint_project(wiki_path, project_name):
    files = [p for p in Path(wiki_path).rglob('*.md') if not any(e in p.parts for e in EXCLUDE)]
    stems = {p.stem: p for p in files}
    WIKILINK = re.compile(r'(?<!\\\`)\[\[([^\]|#]+)')
    CODE = re.compile(r'\`\`\`.*?\`\`\`', re.DOTALL)

    broken = 0
    tracked_count = 0
    for f in files:
        txt = f.read_text(errors='ignore')
        no_code = CODE.sub('', txt)
        for w in WIKILINK.findall(no_code):
            w = w.strip()
            if not w or w in {'wikilink', '...', '…'}: continue
            try:
                target = (f.parent / w).resolve()
                ok = target.exists()
                if not ok:
                    target_md = (f.parent / (w + '.md')).resolve()
                    ok = target_md.exists()
            except: ok = False
            if not ok: ok = w in stems or Path(w).stem in stems
            if not ok:
                if w in tracked:
                    tracked_count += 1
                else:
                    broken += 1
                    print(f'  BROKEN  {f.relative_to(wiki_path.parent.parent)}  →  [[{w}]]')
    print(f'{project_name}: {len(files)} files, {broken} untracked + {tracked_count} tracked broken')
    return broken

total_broken = 0
for project in ['Fiction', 'Game/roguelike_sprawl', 'Language']:
    wiki = Path(f'{project}/wiki')
    if wiki.exists():
        total_broken += lint_project(wiki, project)

if total_broken > 0:
    print(f'Total UNTRACKED broken: {total_broken}')
    sys.exit(1)
print('All untracked wikilinks valid.')
"
    local rc=$?
    if [ $rc -eq 0 ]; then
        echo "${GREEN}✓ vault-lint PASS${RESET}"
    else
        echo "${RED}✗ vault-lint FAIL${RESET}"
        exit_code=1
    fi

    RESULTS+=("vault-lint: $([ $exit_code -eq 0 ] && echo PASS || echo FAIL)")
    return $exit_code
}

run_dashboard_build() {
    echo
    echo "${BOLD}=== dashboard-build ===${RESET}"
    local exit_code=0

    if ! python3 Game/roguelike_sprawl/tools/build_dashboard.py > /dev/null 2>&1; then
        echo "${RED}✗ build_dashboard FAIL${RESET}"
        exit_code=1
    else
        echo "${GREEN}✓ build_dashboard PASS${RESET}"
    fi

    if ! python3 Game/roguelike_sprawl/tools/build_static_data.py > /dev/null 2>&1; then
        echo "${RED}✗ build_static_data FAIL${RESET}"
        exit_code=1
    else
        echo "${GREEN}✓ build_static_data PASS${RESET}"
    fi

    if ! python3 Fiction/tools/verify_mission_sync.py > /dev/null 2>&1; then
        echo "${RED}✗ post-build verify_mission_sync FAIL${RESET}"
        exit_code=1
    else
        echo "${GREEN}✓ post-build verify_mission_sync PASS${RESET}"
    fi

    RESULTS+=("dashboard-build: $([ $exit_code -eq 0 ] && echo PASS || echo FAIL)")
    return $exit_code
}

# Parse args
JOB="${1:-all}"

case "$JOB" in
    all) run_fiction_verify; run_vault_lint; run_dashboard_build ;;
    fiction) run_fiction_verify ;;
    lint) run_vault_lint ;;
    dashboard) run_dashboard_build ;;
    *)
        echo "Usage: $0 {all|fiction|lint|dashboard}"
        exit 2
        ;;
esac

echo
echo "${BOLD}=== Summary ===${RESET}"
for r in "${RESULTS[@]}"; do
    if [[ "$r" == *PASS ]]; then
        echo "${GREEN}✓ $r${RESET}"
    else
        echo "${RED}✗ $r${RESET}"
    fi
done

# Final exit code
for r in "${RESULTS[@]}"; do
    if [[ "$r" == *FAIL ]]; then
        exit 1
    fi
done
exit 0