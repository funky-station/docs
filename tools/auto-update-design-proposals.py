#!/usr/bin/env python3

# auto generate summary.md proposals

from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SUMMARY = SCRIPT_DIR.parent / "src" / "SUMMARY.md"
PROPOSAL_DIR = SCRIPT_DIR.parent / "src" / "design-proposals"

if not PROPOSAL_DIR.is_dir():
    print(f"Directory {PROPOSAL_DIR} not found")
    exit(1)

def get_title(md_file: Path) -> str:
    with open(md_file, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return md_file.stem.replace("_", " ").replace("-", " ")

proposals = sorted(f for f in PROPOSAL_DIR.iterdir() if f.suffix == ".md" and f.name != "template.md")

proposal_lines = [f"  - [{get_title(f)}](design-proposals/{f.name})" for f in proposals]

with open(SUMMARY, "r") as f:
    lines = f.readlines()

with open(SUMMARY, "w") as f:
    for line in lines:
        line = line.rstrip("\n")
        if line.startswith("- [Game Design Proposals]"):
            f.write("- [Game Design Proposals]()\n")
            for pline in proposal_lines:
                f.write(f"{pline}\n")
        else:
            f.write(f"{line}\n")


print(f"Updated {SUMMARY} with {len(proposal_lines)} proposals")
