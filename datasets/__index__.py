from pathlib import Path
from io import IOBase


PATH = str(Path(__file__).parents[0])


def get_dataset_path(filename: str) -> Path:
    return PATH / f"{filename}.csv"


def open_dataset(filename: str) -> IOBase:
    return open(get_dataset_path(filename))

