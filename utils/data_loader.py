import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    ROOT_DIR
    / "data"
    / "test_data.json"
)


def load_test_data():
    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)
