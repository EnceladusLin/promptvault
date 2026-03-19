# PromptVault

A local-first prompt manager for AI workflows.

## What it does

PromptVault helps developers and teams store, tag, search, diff, and version prompts.

## Why this has star potential

- prompt management is still messy for most teams
- local-first beats SaaS friction
- versioning + search + exports is a strong combo
- useful across devs, PMs, researchers, and AI builders

## CLI

```bash
# add a prompt
promptvault add "Bug triage" --content "Summarize the issue and propose fixes" --tag support --tag engineering

# list prompts
promptvault list

# search prompts
promptvault search bug

# export all prompts
promptvault export > prompts.json
```

## MVP

- create prompt entries
- tag and search prompts
- export to markdown/json
- version history via filesystem
- CLI interface

## Stack

- Python
- Click
- PyYAML
- Rich
