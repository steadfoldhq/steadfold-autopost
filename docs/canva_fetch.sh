#!/usr/bin/env bash
# Usage: canva_fetch.sh <name> <signed-url> [<name> <url> ...]
# Pulls Canva export URLs into steadfold-autopost/assets/inbox via the fetch-asset workflow, ONE AT A TIME
# (the workflow's concurrency group keeps only one pending run, so parallel dispatches get dropped).
set -euo pipefail
R=steadfoldhq/steadfold-autopost; W=fetch-asset.yml; REPO=/home/claude/steadfold-autopost
while [ $# -ge 2 ]; do
  name=$1; url=$2; shift 2
  last=$(gh api "repos/$R/actions/workflows/$W/runs?per_page=1" --jq '.workflow_runs[0].id // 0')
  gh api -X POST "repos/$R/actions/workflows/$W/dispatches" -f ref=main -f "inputs[url]=$url" -f "inputs[name]=$name"
  for i in $(seq 1 60); do
    sleep 5
    read -r id st co < <(gh api "repos/$R/actions/workflows/$W/runs?per_page=1" --jq '.workflow_runs[0] | "\(.id) \(.status) \(.conclusion // "-")"')
    [ "$id" != "$last" ] && [ "$st" = completed ] && break
  done
  echo "$name: $st $co"
done
git -C "$REPO" pull -q --rebase origin main
ls -la "$REPO/assets/inbox"
