from pathlib import Path
import os

CLASSPATH = str(Path(__file__).parents[0])
DELIMITER = ';'
HASH: str = 'hash'
PL = CLASSPATH + os.path.sep + '/predictors_library.csv'
PREDICTOR_FILE: str = 'file'


def is_file_present(file) -> bool:
    return Path(file).is_file()
