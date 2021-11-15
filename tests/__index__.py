from pathlib import Path
from io import IOBase
from typing import Iterable, Dict
import csv


PATH = str(Path(__file__).parents[0])


def get_test_path(filename: str) -> Path:
    return PATH / f"{filename}.csv"


def open_test(filename: str) -> IOBase:
    return open(get_dataset_path(filename))


def test_cases(filename: str) -> Iterable[Dict]:
    with open_test(filename) as file:
        yield csv.DictReader(file, delimiter=';', quotechar='"')
