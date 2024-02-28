from pprint import pprint

from config import config
from connector.api_connect import hh_get_resource
from database.create_database import (create_database, create_table,
                                      save_data_to_database)
from dbmanager.dm_manager_hh import DBManager


def main() -> None:
    data = hh_get_resource()
    pprint(data)

    params = config()

    text = "python" # Текст для поиска в БД

    create_database("hh", params)
    create_table("hh", params)
    save_data_to_database(data, "hh", params)

    db_hh = DBManager()
    company_count_vecancy = db_hh.get_companies_and_vacancies_count("hh", params)
    print("список всех компаний и количество вакансий у каждой компании")
    pprint(company_count_vecancy)
    all_vecancy = db_hh.get_all_vacancies("hh", params)
    print("список всех вакансий")
    pprint(all_vecancy)
    avg_salary = db_hh.get_avg_salary("hh", params)
    print("средняя зарплата")
    print(avg_salary)
    vacancies_with_higher_salary = db_hh.get_vacancies_with_higher_salary("hh", params)
    print("вакансии с высокой зарплатой")
    pprint(vacancies_with_higher_salary)
    vacancies_with_keyword = db_hh.get_vacancies_with_keyword("hh", params, text)
    print("вакансии с ключевым словом python")
    pprint(vacancies_with_keyword)


if __name__ == "__main__":
    main()
