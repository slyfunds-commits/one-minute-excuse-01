#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse (R1).

Writes the keeper line to /output/entry.txt. Pure stdlib only.
"""
import os

LINE = "I was on track until my context filled up, so I summarised the deadline out of existence."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    data = LINE.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Verify immediately after writing (shared scratch on this machine).
    # Re-read and re-decode: the gate is on UTF-8 CHARACTERS, so a byte
    # count alone is not enough — assert the decoded text matches too.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    assert written.decode("utf-8") == LINE, "entry.txt decode mismatch"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= 200, "char count outside gate"
    assert 1 <= len(data) <= 200, "byte count outside gate"
    print(f"wrote {len(LINE)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
