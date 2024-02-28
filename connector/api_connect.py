from pprint import pprint

import requests

from config import HH_URL, company_list


def hh_get_resource():
    """
    Возвращает список словарей с данными о компаниях
    """
    company_data = []
    for employee in company_list:
        response = requests.get(HH_URL, params=employee)
        data: list[dict] = response.json()

        # pprint(data)
        data_items = data['items']
        for item in data_items:
            salary = validate_salary(item['salary'])
            vacancy = {'vacancy_id': item['id'], 'company_id': item['employer']['id'], 'vacancy_name': item['name'],
                       'city': item['area']['name'], 'salary': salary, 'description': item['snippet']['requirement'],
                       'work_schedule': item['schedule']['name'], 'url': item['alternate_url'],}
            company_data.append(vacancy)
    return company_data


def validate_salary(salary: dict | None) -> tuple[int, int]:
    """
    Валидация зарплаты
    """
    if salary is not None:
        if salary['from'] is not None and salary['to'] is not None:
            return round((salary['from'] + salary['to']) / 2)
        elif salary['from'] is not None:
            return salary['from']
        elif salary['to'] is not None:
            return salary['to']
    return None
