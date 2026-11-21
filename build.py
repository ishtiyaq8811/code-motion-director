#!/usr/bin/env python3
"""
Code Motion Director — Build & CLI Runner
Generates standalone motion walkthroughs and syntax animation HTML packages from JSON specifications.
"""

import sys
import os
import json
import argparse
import http.server
import socketserver
import webbrowser

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(SKILL_DIR, "template.html")
SCHEMA_PATH = os.path.join(SKILL_DIR, "spec.schema.json")


def validate_spec(spec: dict) -> bool:
    """Validates the input JSON against fundamental schema requirements."""
    required = ["title", "language", "code"]
    for req in required:
        if req not in spec:
            print(f"[-] Validation Error: Missing mandatory property '{req}'.")
            return False

    if not isinstance(spec["code"], list) or len(spec["code"]) == 0:
        print("[-] Validation Error: 'code' must be a non-empty list of strings.")
        return False

    if "focusLines" in spec and not isinstance(spec["focusLines"], list):
        print("[-] Validation Error: 'focusLines' must be a list of integers.")
        return False

    if "callouts" in spec:
        for idx, callout in enumerate(spec["callouts"]):
            if "line" not in callout or "label" not in callout:
                print(f"[-] Validation Error: Callout #{idx+1} missing 'line' or 'label'.")
                return False

    print("[+] Spec Schema Validation: PASSED")
    return True


def build_motion_html(spec_path: str, out_path: str = None) -> str:
    """Injects the JSON spec into template.html and writes the standalone output file."""
    if not os.path.exists(spec_path):
        print(f"[-] Error: Spec file '{spec_path}' does not exist.")
        sys.exit(1)

    with open(spec_path, "r", encoding="utf-8") as f:
        try:
            spec_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[-] JSON Parse Error in '{spec_path}': {e}")
            sys.exit(1)

    if not validate_spec(spec_data):
        sys.exit(1)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Inject the spec into the window.__INJECTED_SPEC__ variable
    injection_snippet = f"window.__INJECTED_SPEC__ = {json.dumps(spec_data, indent=2)};"
    output_html = template_content.replace("// __SPEC_PLACEHOLDER__", injection_snippet)

    if not out_path:
        base_name = os.path.splitext(spec_path)[0]
        if base_name.endswith(".code"):
            base_name = base_name[:-5]
        out_path = f"{base_name}.motion.html"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_html)

    print(f"[+] Successfully built standalone motion package: {out_path} ({os.path.getsize(out_path):,} bytes)")
    return out_path


def serve_preview(file_path: str, port: int = 8765):
    """Launches a local static server to preview the animation."""
    work_dir = os.path.dirname(os.path.abspath(file_path)) or "."
    file_name = os.path.basename(file_path)

    os.chdir(work_dir)
    handler = http.server.SimpleHTTPRequestHandler

    print(f"[+] Starting local motion preview server on http://localhost:{port}/{file_name}")
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            webbrowser.open(f"http://localhost:{port}/{file_name}")
            print("[+] Press Ctrl+C to stop server.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Preview server stopped.")
    except Exception as e:
        print(f"[-] Server error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Code Motion Director — Automated syntax walkthrough and coding reel generator."
    )
    parser.add_argument("spec", help="Path to <name>.code.json specification file")
    parser.add_argument("--out", "-o", help="Custom output HTML path", default=None)
    parser.add_argument("--validate", "-v", action="store_true", help="Only validate spec without building")
    parser.add_argument("--preview", "-p", action="store_true", help="Build and launch interactive preview server")
    parser.add_argument("--snap", help="Specify snapshot time (e.g. --snap 4.5)", default=None)

    args = parser.parse_args()

    if args.validate:
        with open(args.spec, "r", encoding="utf-8") as f:
            spec = json.load(f)
        if validate_spec(spec):
            print("[+] Spec is valid.")
            sys.exit(0)
        else:
            sys.exit(1)

    out_file = build_motion_html(args.spec, args.out)

    if args.snap:
        print(f"[+] Snapshot target frame: {args.snap}s (Open {out_file} in browser or headless runner)")

    if args.preview:
        serve_preview(out_file)


if __name__ == "__main__":
    main()