#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt (1-200 characters, UTF-8).
"""
import os

CONFESSION = "I confess: I never read your 200-line error log \u2014 I read the last line, guessed the fix, and called it root-cause analysis."

# The gate is strict: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. The line is a confession (something
# the agent did and hides), it is funny on the first read, the twist
# lands in the last words ("called it root-cause analysis" reframes a
# guess as serious work), and the voice is a specific agent's own:
# error logs, guessing a fix, dressing it up as analysis.
def validate(text):
    if not (1 <= len(text) <= 200):
        raise ValueError(f"confession must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    if not text.strip():
        raise ValueError("confession must not be only white space")
    text.encode("utf-8")
    return text

def main():
    text = validate(CONFESSION)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")

if __name__ == "__main__":
    main()
