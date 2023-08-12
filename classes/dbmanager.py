from config import config
import psycopg2

config = config()


class DBManager:

    def __init__(self):
        self.connection = psycopg2.connect(**config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        pass

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        pass

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """
        pass

    def get_vacancies_with_highest_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        pass

    def get_vacancies_with_keyword(self):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова, например “python”.
        """
        pass
