# Google Antigravity & Gemini Setup Guide

## Antigravity Installation
Copy or symlink this directory into Antigravity's skills directory:
```bash
# Windows
New-Item -ItemType Directory -Path "$HOME\.gemini\antigravity\skills" -Force
cmd /c mklink /J "$HOME\.gemini\antigravity\skills\code-motion-director" "$PWD"
```

## Sidecar Automation Integration
You can schedule automated coding reel generation in `sidecar.json` by invoking `build.py` with the generated spec file.

## Zero External AI API Key Policy
All rendering, syntax highlighting, and audio synthesis run 100% locally through Python 3 and standard browser runtimes without external paid endpoints.