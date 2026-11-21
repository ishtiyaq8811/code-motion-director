# Claude & Claude Code Setup Guide

## Option A: Global Installation
Copy or symlink this directory into your Claude Code skills directory:
```bash
# macOS / Linux
mkdir -p ~/.claude/skills
ln -s "$(pwd)" ~/.claude/skills/code-motion-director

# Windows PowerShell
New-Item -ItemType Directory -Path "$HOME\.claude\skills" -Force
cmd /c mklink /J "$HOME\.claude\skills\code-motion-director" "$PWD"
```

## Option B: Repository Plugin Mode
Add this folder to your repository's `.claude-plugin/skills/` directory.

## Invocation
In Claude Code, invoke with:
- `/code-motion`
- *"Animate this function into a vertical reel"*
- *"Create a code motion walkthrough for my auth pipeline"*