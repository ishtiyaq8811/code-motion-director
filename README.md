# 🎬 Code Motion Director — Reusable AI Skill Package

> An autonomous AI skill for directing animated syntax walkthroughs, code explanation reels, and terminal execution videos for technical educators, software creators, and developers.

![Skill Version](https://img.shields.io/badge/Version-1.0.0-brightgreen)
![Skill Standard](https://img.shields.io/badge/Standard-claude--animation--skills-blue)
![Platform Support](https://img.shields.io/badge/Platforms-Claude%20%7C%20ChatGPT%20%7C%20Antigravity%20%7C%20Gemini-purple)
![Zero External Keys](https://img.shields.io/badge/External%20AI%20Keys-Zero%20Required-success)
![License](https://img.shields.io/badge/License-MIT-orange)

```
┌──────────────────────────────────────┐
│ 🔴 🟡 🟢  src/auth/session.ts   [9:16]│  mac title bar with file path
├──────────────────────────────────────┤
│ 01 async function verifyToken(jwt) { │
│ 02   const decoded = await verify(); │  active line focused
│ 03   if (!decoded.valid) {     ┌─────┼─ 01 Token validation
│ 04     throw new AuthError();  │     │
│ 05   }                               │  inactive lines dimmed
│ 06   return decoded.user;            │
├──────────────────────────────────────┤
│ > TERMINAL EXECUTION                 │  sliding terminal drawer
│ > POST /api/v1/auth/verify HTTP/1.1  │  animated stdout logging
│ > Status: 200 OK (14.2ms)            │
└──────────────────────────────────────┘
```

---

## 🌟 Overview

**Code Motion Director** is a reusable AI Skill package inspired by the architecture of `claude-animation-skills`. It equips AI assistants with the capability to transform static source code snippets into engaging, 60fps animated walkthrough videos and interactive HTML presentations.

### Why this skill?
Creating technical reels and video walkthroughs traditionally requires heavy video editing software (After Effects, Premiere) or complex motion libraries. This skill provides a declarative, JSON-driven motion pipeline that any LLM can generate and render in seconds.

---

## 🚀 Key Capabilities

- **⌨️ Natural Typewriter Engine:** Animates code line-by-line and character-by-character with a realistic blinking cursor (`█`).
- **💡 Focal Line Dimming:** Automatically dims inactive code lines to 25% opacity while highlighting current focal lines with accent borders.
- **🏷️ Leader Callout Badges:** Draws annotated badges connected by leader lines pointing directly to specific code statements.
- **📟 Sliding Terminal Drawer:** Built-in bottom console drawer that slides open and prints real-time execution stdout logs.
- **🎵 Web Audio Synthesizer:** Pure procedural audio generation for mechanical keyboard clicks and completion chimes (zero external sound files needed).
- **📐 Multi-Aspect Ratio Support:** Native support for `9:16` vertical video (TikTok, YouTube Shorts, Instagram Reels) and `16:9` widescreen desktop video.
- **🎨 Modern Developer Themes:** Pre-built palettes including Obsidian Dark, One Dark, Monokai, and Cyberpunk Neon.

---

## 📂 Package Structure

```text
code-motion-director/
├── SKILL.md                 # Master skill prompt specification & agent instructions
├── README.md                # Comprehensive documentation & installation guide
├── build.py                 # Python 3 CLI runner & validator
├── template.html            # Standalone 60fps HTML5 Canvas/SVG animation engine
├── spec.schema.json         # JSON Schema specification
├── examples/                # Functional test fixtures
│   ├── async-await.json     # TypeScript async/await auth verification
│   ├── python-decorator.json# Python timing decorator benchmark
│   └── rust-borrow.json     # Rust mutable borrow and memory retention
└── adapters/                # Multi-platform installation guides
    ├── claude-code.md       # Claude Code setup instructions
    ├── chatgpt-instructions.md# ChatGPT / Custom GPT setup instructions
    └── antigravity-gemini.md# Google Antigravity & Gemini setup instructions
```

---

## ⚡ Quickstart & CLI Usage

### 1. Validate a Spec
```bash
python build.py examples/async-await.json --validate
```

### 2. Build Standalone Interactive Motion HTML
```bash
python build.py examples/async-await.json
# Generates: examples/async-await.motion.html
```

### 3. Launch Local Motion Scrubber & Preview
```bash
python build.py examples/async-await.json --preview
```

---

## 🛠️ Multi-Platform Installation

### 🤖 Claude & Claude Code
Symlink or copy this repository into your skills directory:
```bash
# macOS/Linux
ln -s "$(pwd)" ~/.claude/skills/code-motion-director

# Windows PowerShell
cmd /c mklink /J "$HOME\.claude\skills\code-motion-director" "$PWD"
```
Trigger with `/code-motion` in any conversation.

### 🧠 Google Antigravity & Gemini
Link into your Antigravity skills repository:
```bash
cmd /c mklink /J "$HOME\.gemini\antigravity\skills\code-motion-director" "$PWD"
```

### 💬 ChatGPT & Custom GPTs
Upload `SKILL.md`, `template.html`, and `build.py` into your Custom GPT's Knowledge section and append the workflow prompt from `adapters/chatgpt-instructions.md`.

---

## 📄 License

MIT License. Free for open-source and commercial use.