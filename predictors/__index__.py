from pathlib import Path
from io import IOBase

PATH = Path(__file__).parents[0]


def get_predictor_path(filename: str) -> Path:
    return PATH / f"{filename}.onnx"


def open_predictor(filename: str) -> IOBase:
    return open(get_dataset_path(filename))
