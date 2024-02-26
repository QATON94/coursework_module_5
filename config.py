import os
from pathlib import Path

HH_URL = 'https://api.hh.ru/vacancies'

ROOT_PATH = Path(__file__).parent
# PATH_JSON_VACANCY = ROOT_PATH.joinpath('data', 'data_vacancies.json')
JSON_VACANCY = os.path.abspath('data/data_vacancies.json')
TEST_JSON = os.path.abspath('test_vacancy.py')

company_list = [{ 'employer_id': '68587'}, {'employer': '9498120'}, {'employer': '3529'}, {'employer': '67611'},
                {'employer': '5441625'}, {'employer': '78638'}, {'employer': '5744540'}, {'employer': '2730053'},
                {'employer': '1008541'}, {'employer': '9623098'}]

db_company = {'company_id': ['68587', '9498120', '3529', '67611', '5441625', '','5744540', '2730053', '1008541', '9623098'],
              'company_name': ['ОЭЗ «АЛАБУГА»', 'Яндекс Команда для бизнеса', 'СБЕР', 'Тензор ',
                               'ООО Инновационный центр КАМАЗ', 'Тинькофф', 'ООО Онлайн-школа Фоксфорд',
                               'ООО Парус электро', 'МФТИ', 'ООО Бриф']}