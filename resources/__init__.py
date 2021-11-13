from pathlib import Path

CLASSPATH = str(Path(__file__).parents[0])
DELIMITER = ';'
HASH: str = 'hash'
PL = CLASSPATH + '/predictors_library.csv'
PREDICTOR_FILE: str = 'file'


def is_file_present(file) -> bool:
    return Path(file).is_file()
