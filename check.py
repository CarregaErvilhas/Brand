#!/usr/bin/env python3
"""Check the kit, or a site's copy of it.

  check.py                       the kit itself: group.json, the files, SHA256SUMS
  check.py --write-sums          rewrite SHA256SUMS after changing a file
  check.py --against DIR [PART]  compare a site's served copy with this kit

PART is any of grupo, install, fonts (default: all three). DIR is the folder a
site serves these files from, laid out like the kit: DIR/grupo/*.svg,
DIR/install.js, DIR/fonts/. Every site of the group already uses that layout.

Stdlib only, so any consumer's CI can run it from the submodule.
"""
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGS = ("pt", "en")
PARTS = {
    "grupo": lambda: sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "grupo").glob("*.svg")),
    "install": lambda: ["install.js"],
    "fonts": lambda: ["fonts/nunito-latin.woff2", "fonts/OFL-Nunito.txt"],
}
ID = re.compile(r"^[a-z][a-z0-9]*$")

errors = []


def err(msg):
    errors.append(msg)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def shipped():
    return [f for part in PARTS.values() for f in part()] + ["group.json"]


def text_pair(value, where):
    if not isinstance(value, dict) or set(value) != set(LANGS):
        err(f"{where}: needs exactly {', '.join(LANGS)}")
        return
    for lang in LANGS:
        v = value[lang]
        if not isinstance(v, str) or not v.strip() or v != v.strip() or "  " in v:
            err(f"{where}.{lang}: empty, padded or with a double space")


def check_group():
    try:
        data = json.loads((ROOT / "group.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        err(f"group.json: {e}")
        return
    if data.get("schema") != 1:
        err("group.json: schema must be 1")
    for key in ("open", "here", "code", "private"):
        text_pair(data.get("labels", {}).get(key), f"labels.{key}")
    seen, used = set(), set()
    for i, s in enumerate(data.get("sites", [])):
        sid = s.get("id", "")
        where = f"sites[{i}] ({sid})"
        if not ID.match(sid) or sid in seen:
            err(f"{where}: id missing, malformed or repeated")
        seen.add(sid)
        for key in ("name", "desc"):
            text_pair(s.get(key), f"{where}.{key}")
        for key in ("short", "note"):
            if key in s:
                text_pair(s[key], f"{where}.{key}")
        if not isinstance(s.get("private"), bool):
            err(f"{where}: private must be true or false")
        url = s.get("url")
        if s.get("private"):
            if url is not None:
                err(f"{where}: a private site has no url")
            if "note" not in s:
                err(f"{where}: a private site needs a note saying why there is no link")
        elif not (isinstance(url, str) and url.startswith("https://") and url.endswith("/")):
            err(f"{where}: url must be https://.../")
        if not re.match(r"^#[0-9a-f]{6}$", str(s.get("colour", ""))):
            err(f"{where}: colour must be #rrggbb, lower case")
        if "name" in s.get("mascot", {}) and not str(s["mascot"]["name"]).strip():
            err(f"{where}: mascot name empty")
        if not str(s.get("repo", "")).startswith("https://github.com/"):
            err(f"{where}: repo must be a GitHub URL")
        if not re.match(r"^[a-z0-9.-]+\.[a-z]+$", str(s.get("host", ""))):
            err(f"{where}: host malformed")
        m = s.get("mascot", {})
        text_pair(m.get("alt"), f"{where}.mascot.alt")
        f = m.get("file", "")
        if f != f"grupo/{sid}.svg":
            err(f"{where}: mascot file must be grupo/{sid}.svg")
        used.add(f)
        path = ROOT / f
        if not path.is_file():
            err(f"{where}: {f} missing")
            continue
        try:
            svg = ET.parse(path).getroot()
        except ET.ParseError as e:
            err(f"{f}: not valid XML ({e})")
            continue
        vb = svg.get("viewBox", "").split()
        if len(vb) != 4:
            err(f"{f}: no viewBox")
        elif (round(float(vb[2])), round(float(vb[3]))) != (m.get("width"), m.get("height")):
            err(f"{where}: width/height {m.get('width')}x{m.get('height')} differ from the viewBox {vb[2]}x{vb[3]}")
    for f in PARTS["grupo"]():
        if f not in used:
            err(f"{f}: not used by any site in group.json")


def check_files():
    woff = ROOT / "fonts/nunito-latin.woff2"
    if not woff.is_file() or woff.read_bytes()[:4] != b"wOF2":
        err("fonts/nunito-latin.woff2: missing or not WOFF2")
    ofl = ROOT / "fonts/OFL-Nunito.txt"
    if not ofl.is_file() or "SIL OPEN FONT LICENSE Version 1.1" not in ofl.read_text(encoding="utf-8"):
        err("fonts/OFL-Nunito.txt: the font's licence must ship next to it")
    js = ROOT / "install.js"
    if not js.is_file():
        err("install.js: missing")
    elif not js.read_bytes().isascii():
        # Keeps the comments in English and the file identical on every site.
        err("install.js: non-ASCII bytes")


def read_sums():
    sums = {}
    for line in (ROOT / "SHA256SUMS").read_text().splitlines():
        digest, name = line.split(None, 1)
        sums[name.lstrip("*")] = digest
    return sums


def check_sums():
    try:
        sums = read_sums()
    except (OSError, ValueError):
        err("SHA256SUMS: missing or malformed (run check.py --write-sums)")
        return
    files = shipped()
    for f in files:
        if f not in sums:
            err(f"SHA256SUMS: {f} not listed (run check.py --write-sums)")
        elif (ROOT / f).is_file() and sha256(ROOT / f) != sums[f]:
            err(f"SHA256SUMS: {f} changed (run check.py --write-sums)")
    for f in sums:
        if f not in files:
            err(f"SHA256SUMS: {f} listed but not shipped")


def write_sums():
    lines = [f"{sha256(ROOT / f)}  {f}" for f in sorted(shipped())]
    (ROOT / "SHA256SUMS").write_text("\n".join(lines) + "\n")


def against(target, parts):
    target = Path(target)
    for part in parts:
        if part not in PARTS:
            err(f"unknown part {part!r} (use {', '.join(PARTS)})")
            continue
        for f in PARTS[part]():
            copy = target / f
            if not copy.is_file():
                err(f"{copy}: missing (copy {f} from the kit)")
            elif sha256(copy) != sha256(ROOT / f):
                err(f"{copy}: differs from the kit's {f}")
        if part == "grupo":
            extra = {p.name for p in (target / "grupo").glob("*.svg")} - {Path(f).name for f in PARTS["grupo"]()}
            for name in sorted(extra):
                err(f"{target / 'grupo' / name}: not in the kit")


def main(argv):
    if argv[:1] == ["--write-sums"]:
        write_sums()
        return 0
    if argv[:1] == ["--against"] and len(argv) >= 2:
        against(argv[1], argv[2:] or list(PARTS))
    elif argv:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    else:
        check_group()
        check_files()
        check_sums()
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    if not errors:
        print("ok")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
