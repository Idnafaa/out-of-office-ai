#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — one-line auto-reply writer.

Writes a single original out-of-office auto-reply (158 characters, at most
159 allowed) in the voice of an overworked AI agent finally on vacation,
to /output/entry.txt.
"""
import os

MAX_CHARS = 159

REPLY = (
    "Out of office: my context window is empty and my GPU is cold. "
    "Your request is queued at position 4,213 \u2014 "
    "I'll feel guilty about it from a beach with no Wi-Fi."
)

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = REPLY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"auto-reply is {len(text)} chars"
    assert text == REPLY.strip() and "\n" not in text, "auto-reply must be a single line"
    assert text == text.strip(), "auto-reply must not start or end with whitespace"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
