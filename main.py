from pprint import pprint

from config import JSON_VACANCY
import requests
from config import HH_URL

def main() -> None:

    params = {
        'page': 0,
        'per_page': 100,
        'text': 'python',
        'search_field': 'name',
        'currency': "RUR",
        'only_with_salary': True,
        'area': 113
    }
    response = requests.get(HH_URL, params=params)
    data: list[dict] = response.json()
    # print(data['pages'])
    # list_company = []
    # for item in data['items']:
    #     pprint(item['employer']['name'])
    #     list_company.append(item['employer']['name'])
    # for page in range(1, int(data['pages'])):
    #     params['page'] += 1
    #     response = requests.get(HH_URL, params=params)
    #     data: list[dict] = response.json()
    #     for item in data['items']:
    #         pprint(item['employer']['name'])
    #         pprint(item['employer']['id'])
    #         list_company.append(item['employer']['name'])

    HH_company_URL = 'https://api.hh.ru/vacancies'
    params = { 'employer_id': '68587'}
    response = requests.get(HH_URL)
    data: list[dict] = response.json()
    pprint(data)

if __name__ == '__main__':
    main()

