import ast
import base64
import os
from io import StringIO
import pandas as pd
import requests

from resources import HASH, CLASSPATH
from utils import update_library

REPO_URL: str = 'https://api.github.com/repos/psykei/psyke-python/contents/test/resources/'
PL_URL: str = REPO_URL + 'new_predictors.csv'
SEPARATOR: str = ','


"""
Read the new predictors on psyke-python:
hash | file
"""
req = requests.get(PL_URL)
if req.status_code == requests.codes.ok:
    req = req.json()
    content = base64.b64decode(req['content']).decode('utf-8')
else:
    raise FileNotFoundError('New predictors not found.')
new_predictors = pd.read_csv(StringIO(content), sep=SEPARATOR)
hash_values = ast.literal_eval(new_predictors.values[0][0])
file_values = ast.literal_eval(new_predictors.values[0][1])

for new_hash, new_file in new_predictors, file_values:
    predictor_req = requests.get(REPO_URL + new_file)
    if predictor_req.status_code == requests.codes.ok:
        predictor_req = predictor_req.json()
        content = base64.b64decode(predictor_req['content'])
    else:
        raise FileNotFoundError('File ' + new_file + ' not found.')

    with open(CLASSPATH + os.path.sep + new_file) as file:
        file.write(content)

    update_library(new_file)
