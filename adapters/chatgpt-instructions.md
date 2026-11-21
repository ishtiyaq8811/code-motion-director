# ChatGPT & Custom GPT Integration Guide

## Custom GPT Configuration
To add `code-motion-director` to a Custom GPT:
1. Open the **GPT Builder** > **Configure**.
2. Under **Instructions**, append the contents of `SKILL.md` (specifically the Spec schema and step-by-step workflow).
3. Under **Knowledge**, upload `template.html`, `build.py`, and `spec.schema.json`.

## Usage Prompt
```text
I want an animated coding reel for this Python snippet:
[paste code here]

Please output the <name>.code.json spec conforming to code-motion-director standards, then generate the animation using build.py.
```