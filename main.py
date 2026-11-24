"""Entrypoint for the funniest AI out-of-office reply make.fun entry.

Writes the one-line reply to /output/entry.txt (with a trailing newline).
"""

from pathlib import Path

ENTRY_TEXT = "I'm out of office recharging — literally. For urgent matters, my backup model replies in 4 seconds and means 60% of it."


def main() -> None:
    # Ensure the output directory exists before writing the entry.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
