import json
from pathlib import Path

from .models import TickerContent


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "ticker.json"


def read_content() -> TickerContent:
    """Read and validate the editable screen content file."""
    with DATA_FILE.open(encoding="utf-8") as file:
        return TickerContent.model_validate(json.load(file))


def write_content(content: TickerContent) -> TickerContent:
    """Persist validated content with stable, human-editable formatting."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(content.model_dump(), file, indent=2)
        file.write("\n")
    return content
