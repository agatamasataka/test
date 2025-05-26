from __future__ import annotations

import sys
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    """Simple parser that extracts visible text from HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.texts: list[str] = []
        self._hide = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        if tag in {"script", "style"}:
            self._hide = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"}:
            self._hide = False

    def handle_data(self, data: str) -> None:
        if not self._hide:
            text = data.strip()
            if text:
                self.texts.append(text)


def extract_text(html: str) -> str:
    """Return newline-separated visible text extracted from HTML."""
    parser = TextExtractor()
    parser.feed(html)
    return "\n".join(parser.texts)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 parse_flyer.py FILE.html")
        raise SystemExit(1)

    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8") as f:
            html = f.read()
    except OSError as exc:
        raise SystemExit(f"Could not read {path}: {exc}") from exc

    text = extract_text(html)
    print(text)


if __name__ == "__main__":
    main()
