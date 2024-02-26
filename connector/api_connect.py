from pprint import pprint

import requests

from config import HH_URL, company_list


def hh_get_resource():
    """
    Возвращает список словарей с данными о компаниях
    """
    company_data = []
    HH_company_URL = 'https://api.hh.ru/vacancies'
    for employee in company_list:
        response = requests.get(HH_URL, params=employee)
        data: list[dict] = response.json()
        # pprint(data)
        for item in data['items']:
            vacancy = {'ID': item['id'], 'Name': item['name'], 'City': item['area']['name'],
                       'Description': item['snippet']['requirement'], 'Work schedule': item['schedule']['name']}
            company_data.append(vacancy)
    return company_data
# 'Salary from': item['salary']['from'], 'Salary to': item['salary']['to']