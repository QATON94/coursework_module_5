import psycopg2
from config import db_company


def create_database(database_name: str, params: dict) -> None:
    """
    Создание базы данных
    """
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True

    with conn.cursor() as cursor:
        cursor.execute(f"DROP DATABASE {database_name}")
        cursor.execute(f"CREATE DATABASE {database_name}")

    conn.close()


def create_table(database_name: str, params: dict) -> None:
    """
    Создание таблицы в базе данных
    """
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE companies (
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR(255)
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE vacancy (
            vacancy_id SERIAL PRIMARY KEY,
            company_id INT REFERENCES companies(company_id),
            vacancy_name VARCHAR(255),
            salary INT,
            city VARCHAR(255),
            description TEXT,
            work_schedule VARCHAR(255),
            url TEXT
            )
            """
        )

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict], database_name: str, params: dict) -> None:
    """
    Сохранение данных в базу данных
    """
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for row in db_company:  # db_company список компаний
            cur.execute(
                """
            INSERT INTO companies (company_id, company_name)
            VALUES (%s, %s)
            RETURNING company_id
            """,
                (row["company_id"], row["company_name"]),
            )

        for row in data:
            cur.execute(
                """
                INSERT INTO vacancy (vacancy_id, company_id, vacancy_name, salary, city, description, work_schedule,
                url)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row["vacancy_id"],
                    row["company_id"],
                    row["vacancy_name"],
                    row["salary"],
                    row["city"],
                    row["description"],
                    row["work_schedule"],
                    row["url"],
                ),
            )

    conn.commit()
    conn.close()
