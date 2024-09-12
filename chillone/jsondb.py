import json
from pathlib import Path
from typing import Any


class JSONDB:
    def __init__(self, location: Path | str) -> None:
        self.location = Path(location)
        with self.location.open("a+", encoding="utf-8") as file:
            try:
                default = json.dumps(
                    json.loads(file.read()),
                    indent=4,
                )
            except json.JSONDecodeError:
                default = "{}"
        with self.location.open("w", encoding="utf-8") as file:
            file.write(default)

    def __get__(self, *_) -> dict[Any, Any]:
        with self.location.open("r", encoding="utf-8") as file:
            return json.load(file)

    def __set__(self, _, value: dict[Any, Any]) -> None:
        with self.location.open("w", encoding="utf-8") as file:
            json.dump(value, file)
