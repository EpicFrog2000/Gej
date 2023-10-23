import mysql.connector
from collections import defaultdict

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="nofluffjobs_db"
)
    
class nofluffjobs_db_interaction:
    connection = mydb.cursor()
    @staticmethod
    def count_all(connection = connection):
        sql = "SELECT COUNT(*) FROM daily_data;"
        connection.execute(sql)
        count = connection.fetchone()[0]
        return count
    @staticmethod
    def get_salary_counts(connection=connection):
        salary_counts = {
            "Poniżej 4000": 0,
            "4000 - 5000": 0,
            "5000 - 6000": 0,
            "6000 - 7000": 0,
            "7000 - 8000": 0,
            "8000 - 10000": 0,
            "10000 - 12000": 0,
            "12000 - 15000": 0,
            "15000 - 20000": 0,
            "20000 i powyżej": 0,
        }
        sql_queries = [
            ("Poniżej 4000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 1 AND salary <= 4000;"),
            ("4000 - 5000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 4000 AND salary < 5000;"),
            ("5000 - 6000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 5000 AND salary < 6000;"),
            ("6000 - 7000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 6000 AND salary < 7000;"),
            ("7000 - 8000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 7000 AND salary < 8000;"),
            ("8000 - 10000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 8000 AND salary < 10000;"),
            ("10000 - 12000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 10000 AND salary < 12000;"),
            ("12000 - 15000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 12000 AND salary < 15000;"),
            ("15000 - 20000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 15000 AND salary < 20000;"),
            ("20000 i powyżej", "SELECT COUNT(*) FROM daily_data WHERE salary >= 20000;")
        ]
        for label, sql in sql_queries:
            connection.execute(sql)
            count = connection.fetchone()[0]
            salary_counts[label] = count
        return salary_counts
    
    @staticmethod
    def count_seniority_data(connection=connection):
        seniority_counts = defaultdict(int)
        sql = "SELECT seniority FROM daily_data;"
        connection.execute(sql)
        seniority_records = connection.fetchall()
        for record in seniority_records:
            seniority = record[0]
            seniority_counts[seniority] += 1
        return seniority_counts

    @staticmethod
    def most_common_category(connection=connection):
        sql = "SELECT category, COUNT(category) AS count FROM daily_data WHERE category IS NOT NULL AND category != '' GROUP BY category ORDER BY count DESC LIMIT 20;"
        connection.execute(sql)
        result = connection.fetchall()
        most_common_categorys = [{"category": row[0], "count": row[1]} for row in result]
        return most_common_categorys
    
    @staticmethod
    def count_lokacja_data(connection=connection):
        sql = (
            "SELECT lokacja, COUNT(lokacja) AS count FROM daily_lokacje "
            "WHERE lokacja IS NOT NULL AND lokacja != '' "
            "GROUP BY lokacja "
            f"ORDER BY count DESC LIMIT 20;"
        )
        connection.execute(sql)
        lokacja_records = connection.fetchall()
        lokacja_counts = [{"lokacja": record[0], "count": record[1]} for record in lokacja_records]
        return lokacja_counts

    @staticmethod
    def count_all(connection = connection):
        sql = "SELECT COUNT(*) FROM daily_data;"
        connection.execute(sql)
        count = connection.fetchone()[0]
        return count
    
    @staticmethod
    def get_doswiadczenie_counts(connection=connection):
        doswiadczenie_counts = {
            "1 - 2": 0,
            "2 - 4": 0,
            "4 - 6": 0,
            "6 - 10": 0,
            "10 +": 0,
        }
        sql_queries = [
            ("1 - 2", "SELECT COUNT(*) FROM daily_data WHERE doswiadczenie >= 1 AND doswiadczenie < 2;"),
            ("2 - 4", "SELECT COUNT(*) FROM daily_data WHERE doswiadczenie >= 2 AND doswiadczenie < 4;"),
            ("4 - 6", "SELECT COUNT(*) FROM daily_data WHERE doswiadczenie >= 4 AND doswiadczenie < 6;"),
            ("6 - 10", "SELECT COUNT(*) FROM daily_data WHERE doswiadczenie >= 6 AND doswiadczenie < 10;"),
            ("10 +", "SELECT COUNT(*) FROM daily_data WHERE doswiadczenie >= 10 ;"),
        ]
        for label, sql in sql_queries:
            connection.execute(sql)
            count = connection.fetchone()[0]
            doswiadczenie_counts[label] = count
        return doswiadczenie_counts
    
    @staticmethod
    def count_wymagania_must_data(connection=connection):
        sql = (
            "SELECT wymaganie, COUNT(wymaganie) AS count FROM daily_wymagania_must "
            "WHERE wymaganie IS NOT NULL AND wymaganie != '' "
            f"GROUP BY wymaganie ORDER BY count DESC LIMIT 20;"
        )
        connection.execute(sql)
        wymagania_must_records = connection.fetchall()
        wymagania_must_counts = [
            {"wymaganie": record[0], "count": record[1]} for record in wymagania_must_records
        ]
        return wymagania_must_counts
    
    @staticmethod
    def count_wymagania_nice_data(connection=connection):
        sql = (
            "SELECT wymaganie, COUNT(wymaganie) AS count FROM daily_wymagania_nice "
            "WHERE wymaganie IS NOT NULL AND wymaganie != '' "
            f"GROUP BY wymaganie ORDER BY count DESC LIMIT 20;"
        )
        connection.execute(sql)
        wymagania_nice_records = connection.fetchall()
        wymagania_nice_counts = [
            {"wymaganie": record[0], "count": record[1]} for record in wymagania_nice_records
        ]
        return wymagania_nice_counts

#historic shit
    @staticmethod
    def get_historic_count_data(connection=connection):
        sql = "SELECT date, count FROM historic_count ORDER BY date ASC;"
        connection.execute(sql)
        historic_data = connection.fetchall()
        data_for_chart = [{"date": entry[0].strftime("%Y-%m-%d"), "count": entry[1]} for entry in historic_data]
        return data_for_chart
    
    @staticmethod
    def get_historic_doswiadczenie_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, experience_range, count_in_range, ROW_NUMBER() OVER (PARTITION BY date ORDER BY count_in_range DESC) AS row_num FROM historic_doswiadczenie WHERE experience_range <> 'brak_danych') SELECT date, experience_range, count_in_range FROM ranked ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "experience_range": row[1],
                "count_in_range": row[2]
            })
        return data_for_chart
    
    @staticmethod
    def get_historic_kategoria_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, kategoria, count, ROW_NUMBER() OVER (PARTITION BY date ORDER BY count DESC) AS row_num FROM historic_kategoria ) SELECT date, kategoria, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "kategoria": row[1],
                "count": row[2]
            })
        return data_for_chart
    
    @staticmethod
    def get_historic_lokacja_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, lokacja, count, ROW_NUMBER() OVER ( PARTITION BY date ORDER BY count DESC ) AS row_num FROM historic_lokacja) SELECT date, lokacja, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "lokacja": row[1],
                "count": row[2]
            })
        return data_for_chart

    @staticmethod
    def get_historic_salary_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, salary_range, count_in_range, ROW_NUMBER() OVER (PARTITION BY date ORDER BY count_in_range DESC) AS row_num FROM historic_salary WHERE salary_range <> 'Unknown') SELECT date, salary_range, count_in_range FROM ranked ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "salary_range": row[1],
                "count_in_range": row[2]
            })
        return data_for_chart
    
    @staticmethod
    def get_historic_seniority_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, seniority, count, ROW_NUMBER() OVER ( PARTITION BY date ORDER BY count DESC ) AS row_num FROM historic_seniority) SELECT date, seniority, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "seniority": row[1],
                "count": row[2]
            })
        return data_for_chart
    
    @staticmethod
    def get_historic_wymagania_must_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, wymaganie, count, ROW_NUMBER() OVER ( PARTITION BY date ORDER BY count DESC ) AS row_num FROM historic_wymagania_must) SELECT date, wymaganie, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "wymaganie": row[1],
                "count": row[2]
            })
        return data_for_chart

    @staticmethod
    def get_historic_wymagania_nice_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, wymaganie, count, ROW_NUMBER() OVER ( PARTITION BY date ORDER BY count DESC ) AS row_num FROM historic_wymagania_nice) SELECT date, wymaganie, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "wymaganie": row[1],
                "count": row[2]
            })
        return data_for_chart