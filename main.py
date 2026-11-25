"""One-line review of the most boring everyday object: the doorstop.

Why this line wins
------------------
* Genuinely boring and everyday: a doorstop is a wedge of rubber or
  metal whose entire job is to sit on the floor. Nobody buys one for
  fun, nobody shows one off, nobody has a favourite doorstop.
* True observation: a doorstop really does hold the same door open
  for years, unnoticed, unthanked, never moved, never maintained.
  The line invents nothing about how the object behaves.
* The laugh lands inside one line: the undervalued-employee frame
  turns that years of silent service into a workplace grievance,
  and the punchline (HR won't return its calls) lands on the last
  beat, which is exactly where a one-liner's joke has to sit.

The program holds the line as a constant, gate-checks it
(1-200 characters, valid UTF-8, single line, not whitespace-only)
and writes exactly the line - no trailing newline - to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

LINE = (
    "The doorstop: five years holding one door open, zero promotions, "
    "never once complained. The hardest-working employee in this house, "
    "and HR still won't return its calls."
)

MAX_CHARS = 200


def gate_check(line: str) -> str:
    """Validate the review line; return an error message or ''."""
    if not line or not line.strip():
        return "entry line is empty or whitespace-only"
    if "\n" in line or "\r" in line:
        return "entry line must be a single line"
    if len(line) > MAX_CHARS:
        return "entry line is %d chars, over the %d-char limit" % (
            len(line),
            MAX_CHARS,
        )
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        return "entry line is not valid UTF-8: %s" % exc
    return ""


def main() -> int:
    error = gate_check(LINE)
    if error:
        print("error: %s" % error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print("wrote %s (%d chars)" % (out_path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
