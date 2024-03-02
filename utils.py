from pprint import pprint

from config import config, db_name
from dbmanager.dm_manager_hh import DBManager


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """
    params = config()
    db_hh = DBManager()
    user_input = ''
    while user_input != '6':
        print("""
        Выберете действие:
        1. Список всех компаний
        2. Список всех вакансий
        3. Средняя зарплата
        4. Вакансии с высокой зарплатой
        5. Поиск по ключевому слову
        6. Выход
        """)
        user_input = input()
        if user_input == '1':
            company_count_vecancy = db_hh.get_companies_and_vacancies_count(db_name, params)
            print("список всех компаний и количество вакансий у каждой компании")
            pprint(company_count_vecancy)
        elif user_input == '2':
            all_vecancy = db_hh.get_all_vacancies(db_name, params)
            print("список всех вакансий")
            pprint(all_vecancy)
        elif user_input == '3':
            avg_salary = db_hh.get_avg_salary(db_name, params)
            print("средняя зарплата")
            pprint(avg_salary)
        elif user_input == '4':
            vacancies_with_higher_salary = db_hh.get_vacancies_with_higher_salary(db_name, params)
            print("вакансии с высокой зарплатой")
            pprint(vacancies_with_higher_salary)
        elif user_input == '5':
            text = input("Введите ключевое слово: ")
            vacancies_with_keyword = db_hh.get_vacancies_with_keyword(db_name, params, text)
            if vacancies_with_keyword == []:
                print("Ничего не найдено")
            else:
                pprint(vacancies_with_keyword)
        elif user_input == '6':
            break
        else:
            print("Не верный ввод")
            print("Введите число от 1 до 6")
