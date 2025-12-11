# fix_visitor_tags.py
import re
from pathlib import Path
import shutil

TEMPLATES_ROOT = Path("core/templates")  # adjust only if your templates live elsewhere
TAG_RE = re.compile(r"\{\%\s*visitor_count\s+(['\"])(?P<key>.+?)\1\s*\%\}")

if not TEMPLATES_ROOT.exists():
    print("Templates folder not found:", TEMPLATES_ROOT)
    raise SystemExit(1)

changed = 0
files_changed = []

for f in TEMPLATES_ROOT.rglob("*.html"):
    txt = f.read_text(encoding="utf-8", errors="ignore")
    matches = list(TAG_RE.finditer(txt))
    if not matches:
        continue

    # backup file
    bak = f.with_suffix(f.suffix + ".bak")
    if not bak.exists():
        shutil.copyfile(f, bak)

    def repl(m):
        key = m.group("key")
        safe = re.sub(r"\W+", "_", key).strip("_").lower()
        return "{{ " + f"{safe}_visits" + " }}"

    new_txt, n = TAG_RE.subn(repl, txt)
    if n:
        f.write_text(new_txt, encoding="utf-8")
        changed += n
        files_changed.append((f, n))

if not files_changed:
    print("No visitor_count tags found. Nothing changed.")
else:
    print(f"Replaced {changed} tag(s) in {len(files_changed)} file(s):")
    for p, n in files_changed:
        print(f" - {p}  ({n} replacements)")

print("Backups were created with a .bak extension next to each modified file.")
