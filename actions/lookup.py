"""Business logic independent of the Rasa SDK, usable in unit tests."""
import json
import unicodedata
from pathlib import Path

KNOWLEDGE = json.loads(Path(__file__).with_name("knowledge.json").read_text(encoding="utf-8"))


def normalize(value: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", value.casefold().strip())
                   if unicodedata.category(c) != "Mn")


def find_service(value: str):
    aliases = {"bu": "bibliothèque", "bourses": "service des bourses",
               "service des aides": "service des bourses"}
    key = normalize(value)
    return aliases.get(key) or next((s for s in KNOWLEDGE if normalize(s) == key), None)
