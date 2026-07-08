"""Fix mixed UTF-8 / Windows-1252 corruption in SKILL.md files."""
from pathlib import Path

REPL = {
    0x91: "\u2018",
    0x92: "\u2019",
    0x93: "\u201c",
    0x94: "\u201d",
    0x96: "\u2013",
    0x97: "\u2014",
}


def fix_bytes(data: bytes) -> str:
    out: list[str] = []
    i = 0
    n = len(data)
    while i < n:
        b = data[i]
        if b < 0x80:
            out.append(chr(b))
            i += 1
            continue
        decoded = None
        size_used = 0
        for size in (4, 3, 2):
            if i + size > n:
                continue
            chunk = data[i : i + size]
            try:
                decoded = chunk.decode("utf-8")
                size_used = size
                break
            except UnicodeDecodeError:
                pass
        if decoded is not None:
            out.append(decoded)
            i += size_used
            continue
        out.append(REPL.get(b, bytes([b]).decode("latin-1")))
        i += 1
    return "".join(out)


def main() -> None:
    fixed: list[str] = []
    bad_bytes = {0x91, 0x92, 0x93, 0x94, 0x96, 0x97}
    for p in Path(".agents/skills").rglob("*.md"):
        data = p.read_bytes()
        needs = any(b in bad_bytes for b in data)
        if not needs:
            try:
                data.decode("utf-8")
            except UnicodeDecodeError:
                needs = True
        if not needs:
            continue
        text = fix_bytes(data)
        text.encode("utf-8")  # verify
        p.write_text(text, encoding="utf-8", newline="\n")
        fixed.append(str(p))
    print(f"fixed {len(fixed)} files")


if __name__ == "__main__":
    main()
