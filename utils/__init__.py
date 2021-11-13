from resources import PL, CLASSPATH, DELIMITER, is_file_present, HASH, PREDICTOR_FILE
import csv
import os


def _create_pl():
    if not is_file_present(PL):
        with open(PL, 'w') as file:
            file.write(HASH + DELIMITER + PREDICTOR_FILE)


def get_predictor(file_hash) -> str:
    """
    Given the file hash of an already existing predictor.onnx return its file path.

    :param file_hash: the hash value
    :return: the predictor's file path
    """
    _create_pl()
    with open(PL) as file:
        rows = csv.DictReader(file, delimiter=DELIMITER)
        for row in rows:
            if file_hash in row[HASH] and is_file_present(CLASSPATH + os.path.sep + row[HASH]):
                return CLASSPATH + os.path.sep + row[PREDICTOR_FILE]
            else:
                raise FileNotFoundError('Predictor not present.')


def update_library(predictor_file):
    """
    Once a new predictor.onnx file is added to this repository, it's necessary to insert it in the library.

    :param predictor_file: the predictor's file name
    """
    _create_pl()
    with open(CLASSPATH + os.path.sep + predictor_file) as file:
        file_content = file.read()
    file_hash = hash(file_content)

    with open(PL, 'a') as file:
        file.write(file_hash + DELIMITER + predictor_file)
