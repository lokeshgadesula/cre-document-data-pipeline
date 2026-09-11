import json
from pathlib import Path

def quarantine(source: str, failures: list[dict], path: str | Path) -> None:
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"source":source,"failures":failures}, sort_keys=True)+"\n")
