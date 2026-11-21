---
name: code-motion-director
description: Generates animated syntax walkthroughs, code explanation videos, and terminal execution reels for technical creators, educators, and developers. Features progressive typewriter typing, focus line dimming, leader callouts, and animated terminal stdout. Use when the user runs /code-motion or asks to animate code, create a coding reel, make a syntax walkthrough, or visualize code execution.
---

# /code-motion-director

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

## First Use
This skill's directory is the base directory of the skill package.
```bash
# Verify Python 3 is installed
python3 --version || python --version
```
Runs standalone without external AI API keys, heavy dependencies, or paid cloud APIs. Uses headless HTML5 Canvas / SVG with optional Playwright, Puppeteer, or ffmpeg for headless MP4 rendering.

---

## Agent Execution Steps

1. **Code & Storyboard:** Ask the user for the code snippet or extract it from their request. Identify the core narrative:
   - What language? (JavaScript, TypeScript, Python, Rust, Go, SQL, Bash, HTML/CSS).
   - What is the focal point? (e.g. an async await call, a decorator, an error throw, a recursive return).
   - What terminal output or execution result proves it works?
2. **Spec Creation:** Write `<name>.code.json` (specification detailed below) in the working directory.
3. **Build & Render:** Run the builder script:
   ```bash
   python build.py <name>.code.json
   ```
   - For an immediate interactive HTML playback, open the generated `<name>.motion.html`.
   - To inspect a static frame snapshot: `python build.py <name>.code.json --snap 4.5`.
   - To validate schema syntax: `python build.py <name>.code.json --validate`.
4. **Quality Check:**
   - Code lines fit comfortably without horizontal overflow (max 48 characters per line recommended for 9:16 mobile; max 80 for 16:9).
   - Callouts are concise, numbered 01 to 03, and clearly point to the target lines.
   - Terminal output accurately reflects realistic execution behavior.
5. **Handover:** Deliver the rendered HTML / video path and spec summary to the user.

---

## Spec Format (`<name>.code.json`)

```json
{
  "title": "src/auth/session.ts",
  "language": "typescript",
  "aspectRatio": "9:16",
  "theme": "obsidian",
  "code": [
    "async function verifyToken(token: string) {",
    "  const session = await auth.verify(token);",
    "  if (!session.isValid) {",
    "    throw new UnauthorizedError('Expired');",
    "  }",
    "  return session.user;",
    "}"
  ],
  "focusLines": [2, 3],
  "typingSpeed": 35,
  "callouts": [
    {
      "line": 2,
      "label": "Async Verification",
      "note": "Awaits cryptographic signature",
      "side": "right"
    },
    {
      "line": 4,
      "label": "Guard Clause",
      "note": "Rejects expired JWT payloads",
      "side": "right"
    }
  ],
  "terminal": {
    "enabled": true,
    "title": "Server Output (Node.js v22)",
    "commands": [
      "$ curl -X POST https://api.dev/auth/verify",
      "> Verifying HMAC-SHA256 signature...",
      "> Token Verified: user_id=4092 [200 OK]"
    ]
  },
  "sound": {
    "typewriterClicks": true,
    "completionChime": true
  },
  "durationSeconds": 8.0
}
```

### Parameter Definitions
- **`title`**: String displayed in the window header bar (e.g. filename or module path).
- **`language`**: `"javascript"`, `"typescript"`, `"python"`, `"rust"`, `"go"`, `"sql"`, `"bash"`.
- **`aspectRatio`**: `"9:16"` (Vertical reel for TikTok/Shorts/Instagram) or `"16:9"` (Horizontal widescreen).
- **`theme`**: `"obsidian"` (deep dark violet), `"onedark"` (Atom-inspired), `"monokai"` (classic high-contrast), or `"cyberpunk"` (neon cyan/magenta).
- **`code`**: Array of strings, each representing one line of code.
- **`focusLines`**: Array of 1-based line numbers to keep at 100% brightness while other lines dim.
- **`callouts`**: Optional list of annotations. Max 3 callouts recommended.
  - `line`: 1-based line number to anchor the leader line.
  - `label`: Short uppercase or bold heading (max 18 chars).
  - `note`: Explanatory subtitle (max 28 chars).
- **`terminal`**: Optional bottom drawer with stdout commands and responses.
- **`sound`**: Optional Web Audio API procedural synthesis settings (typing clicks and chime).
- **`durationSeconds`**: Total animation duration (default: 8.0s).

---

## Supported Platforms

| Platform | Integration Method |
| :--- | :--- |
| **Claude / Claude Code** | Loaded via `SKILL.md` in `~/.claude/skills/code-motion-director/` or workspace `.claude-plugin/` |
| **Google Antigravity** | Registered under `.gemini/antigravity/skills/code-motion-director/` |
| **ChatGPT / Custom GPTs** | Configured via Custom Instructions using `adapters/chatgpt-instructions.md` |
| **Google Gemini** | Injected via system instruction using `adapters/antigravity-gemini.md` |

---

## Taste & Aesthetic Standards

- **Clear visual hierarchy:** Keep code clean, formatted, and readable. Never paste minified code.
- **Concise callouts:** Callout notes should be technical facts, not marketing hype ("Awaits promise", not "Super cool feature!").
- **Contrast & Legibility:** Always ensure code font is sufficiently sized for mobile smartphone screens (minimum 28px on 1080x1920 canvas).
- **Pacing:** Typing should feel natural (25–40ms per character). Terminal output should appear after the code finishes typing.