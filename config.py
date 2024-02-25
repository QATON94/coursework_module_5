import os
from pathlib import Path

HH_URL = 'https://api.hh.ru/vacancies'

ROOT_PATH = Path(__file__).parent
# PATH_JSON_VACANCY = ROOT_PATH.joinpath('data', 'data_vacancies.json')
JSON_VACANCY = os.path.abspath('data/data_vacancies.json')
TEST_JSON = os.path.abspath('test_vacancy.py')