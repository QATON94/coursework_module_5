import psycopg2


class DBManager:

    def get_companies_and_vacancies_count(self, database_name: str, params: dict) -> list[dict]:
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        conn = psycopg2.connect(dbname=database_name, **params)
        with conn.cursor() as cur:
            cur.execute("""
                SELECT company_name, COUNT(vacancy_id) 
                FROM companies
                JOIN vacancy USING(company_id)
                GROUP BY company_name
                            """)
            rows = cur.fetchall()
            companies_count_vecancy = []
            for row in rows:
                # print(row)
                company_vecancy_value = {'company_name': row[0], 'vecancy_count': row[1]}
                companies_count_vecancy.append(company_vecancy_value)

        return companies_count_vecancy

    def get_all_vacancies(self, database_name: str, params: dict) -> list[dict]:
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """

        conn = psycopg2.connect(dbname=database_name, **params)
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT company_name, vacancy_name, salary, url
                        FROM companies
                        JOIN vacancy USING(company_id)
                        """)
            rows = cur.fetchall()
            bd_rows = []
            for row in rows:
                # print(row)
                bd_row = {'company_name': row[0], 'vacancy_name': row[1], 'solary': row[2],
                          'url': row[3]}
                bd_rows.append(bd_row)

        return bd_rows

    def get_avg_salary(self, database_name: str, params: dict) -> float:
        """
        Получает среднюю зарплату по вакансиям.
        """

        conn = psycopg2.connect(dbname=database_name, **params)
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT AVG(salary) FROM vacancy
                        """)
            avg_salary = cur.fetchall()[0][0]

        return round(avg_salary, 2)

    def get_vacancies_with_higher_salary(self, database_name: str, params: dict) -> list[dict]:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """

        conn = psycopg2.connect(dbname=database_name, **params)
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM vacancy
                        WHERE salary > (SELECT AVG(salary) FROM vacancy)
                        """)
            rows = cur.fetchall()
            bd_rows = []
            for row in rows:
                # print(row)
                bd_row = {'vacancy_id': row[0], 'company_id': row[1], 'vacancy_name': row[2],
                          'salary': row[3], 'city': row[4], 'description': row[5], 'work_schedule': row[6],
                          'url': row[7]}
                bd_rows.append(bd_row)

        return bd_rows

    def get_vacancies_with_keyword(self, database_name: str, params: dict, text: str) -> list[dict]:
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова
        """

        conn = psycopg2.connect(dbname=database_name, **params)
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM vacancy WHERE LOWER (description) LIKE '%{text}%' ")
            rows = cur.fetchall()
            bd_rows = []
            for row in rows:
                # print(row)
                bd_row = {'vacancy_id': row[0], 'company_id': row[1], 'vacancy_name': row[2],
                          'salary': row[3], 'city': row[4], 'description': row[5], 'work_schedule': row[6],
                          'url': row[7]}
                bd_rows.append(bd_row)

        return bd_rows
