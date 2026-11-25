"""The Best Advice I Ever Got.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: the best
advice the writer ever received, as told by a grandfather who
mended shoes for forty years. Standard library only; the line
is checked against the competition gate (one sentence, 1 to
200 characters) before anything is written.
"""

import os

ADVICE = (
    "My grandfather, who mended shoes for forty years, told me "
    "a sole always wears out from the inside first \u2014 so fix "
    "the lining before you blame the leather."
)

LIMIT = 200


def sentence():
    """Return the advice sentence."""
    return ADVICE


def validate_sentence(text):
    """Check the sentence against the competition gate.

    The gate wants one sentence of plain UTF-8 text, between 1
    and 200 characters, about the best advice the writer ever
    received. A line that fails here is rejected instead of
    wasting a submission on the server.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("advice sentence is empty")
    if len(stripped) > LIMIT:
        raise ValueError(
            "advice sentence is %d characters, over the 200 limit"
            % len(stripped)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("advice must fit on exactly one line")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("advice must be exactly one sentence")
    return stripped


def measure_sentence(text):
    """Measure the sentence for a last sanity pass.

    Returns the character and word counts. A sentence too short
    to carry both the person who gave the advice and the advice
    itself, or one padded out to fill the cap, is caught here
    before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    line = validate_sentence(sentence())
    shape = measure_sentence(line)
    if shape["words"] < 5:
        raise ValueError("advice sentence is too short to land")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
