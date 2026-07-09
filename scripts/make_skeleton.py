"""Create a dated experiment folder."""
from __future__ import annotations

from datetime import date
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    day = date.today().isoformat()
    exp = root / "experiments" / day
    exp.mkdir(parents=True, exist_ok=True)
    (exp / "notes.md").write_text(f"# Experiment {day}\n\n## Hypothesis\n\n## Metric\n\n", encoding="utf-8")
    (exp / "data").mkdir(exist_ok=True)
    print(exp)


if __name__ == "__main__":
    main()
