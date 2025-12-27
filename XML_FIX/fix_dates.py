from datetime import datetime, timezone
import re

INPUT = "MIRKV.xml"
OUTPUT = "MIRKVREADY.xml"

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

with open(INPUT, "r", encoding="utf-8") as f:
    content = f.read()

for tag in ("generation-date", "creation-date", "last-update-date"):
    content = re.sub(
        fr"<{tag}>.*?</{tag}>",
        f"<{tag}>{now}</{tag}>",
        content
    )

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(content)

print("✔ Готово, UTC без смещения:", now)