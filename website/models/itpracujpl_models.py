import mysql.connector
from collections import defaultdict
import math

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="itpracujpl_db"
)

class itpracujpl_db_interaction:
    connection = mydb.cursor()
    @staticmethod
    def last_date(connection=connection):
        sql = "SELECT MAX(date) FROM daily_data;"
        connection.execute(sql)
        result = connection.fetchone()[0]
        return result
    
    @staticmethod
    def count_all(connection=connection):
        sql = "SELECT COUNT(*) FROM daily_data;"
        connection.execute(sql)
        result = connection.fetchone()[0]
        return result
    
    @staticmethod
    def positive_salary(connection=connection):
        sql = "SELECT IFNULL((SUM(CASE WHEN salary > 0 THEN 1 ELSE 0 END) / COUNT(*)) * 100, 0) AS percentage FROM daily_data;"
        connection.execute(sql)
        result = connection.fetchone()[0]
        return math.floor(result)
    
    @staticmethod
    def most_common_locations(connection=connection):
        sql = "SELECT location, COUNT(location) AS count FROM daily_data WHERE location IS NOT NULL AND location != '' GROUP BY location ORDER BY count DESC LIMIT 20;"
        connection.execute(sql)
        result = connection.fetchall()
        most_common_locations = [{"location": row[0], "count": row[1]} for row in result]
        return most_common_locations
    
    def get_salary_counts(connection=connection):
        salary_counts = {
            "Poniżej 4000": 0,
            "4000 - 5000": 0,
            "5000 - 6000": 0,
            "6000 - 7000": 0,
            "7000 - 8000": 0,
            "8000 - 10000": 0,
            "10000 - 12000": 0,
            "12000 i powyżej": 0
        }
        sql_queries = [
            ("Poniżej 4000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 1 AND salary <= 4000;"),
            ("4000 - 5000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 4000 AND salary < 5000;"),
            ("5000 - 6000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 5000 AND salary < 6000;"),
            ("6000 - 7000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 6000 AND salary < 7000;"),
            ("7000 - 8000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 7000 AND salary < 8000;"),
            ("8000 - 10000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 8000 AND salary < 10000;"),
            ("10000 - 12000", "SELECT COUNT(*) FROM daily_data WHERE salary >= 10000 AND salary < 12000;"),
            ("12000 i powyżej", "SELECT COUNT(*) FROM daily_data WHERE salary >= 12000;")
        ]
        for label, sql in sql_queries:
            connection.execute(sql)
            count = connection.fetchone()[0]
            salary_counts[label] = count
        return salary_counts
    
    @staticmethod
    def count_etat_data(connection=connection):
        etat_counts = defaultdict(int)
        sql = "SELECT etat FROM daily_etat;"
        connection.execute(sql)
        etat_records = connection.fetchall()
        for record in etat_records:
            etat = record[0]
            etat_counts[etat] += 1
        return etat_counts
    
    @staticmethod
    def count_kontrakt_data(connection=connection):
        kontrakt_counts = defaultdict(int)
        sql = "SELECT kontrakt FROM daily_kontrakt;"
        connection.execute(sql)
        kontrakt_records = connection.fetchall()
        for record in kontrakt_records:
            kontrakt = record[0]
            kontrakt_counts[kontrakt] += 1
        return kontrakt_counts
    
    @staticmethod
    def count_management_level_data(connection=connection):
        management_level_counts = defaultdict(int)
        sql = "SELECT management_level FROM daily_management_level;"
        connection.execute(sql)
        management_level_records = connection.fetchall()
        for record in management_level_records:
            management_level = record[0]
            management_level_counts[management_level] += 1
        return management_level_counts
    
    @staticmethod
    def count_work_type_data(connection=connection):
        work_type_counts = defaultdict(int)
        sql = "SELECT work_type FROM daily_work_type;"
        connection.execute(sql)
        work_type_records = connection.fetchall()
        for record in work_type_records:
            work_type = record[0]
            work_type_counts[work_type] += 1
        return work_type_counts
    
    @staticmethod
    def count_specjalizacje_data(connection=connection):
        sql = (
            "SELECT TRIM(specjalizacja) AS specjalizacja, COUNT(TRIM(specjalizacja)) AS count FROM daily_specjalizacje WHERE TRIM(specjalizacja) IS NOT NULL AND TRIM(specjalizacja) != '' GROUP BY TRIM(specjalizacja) ORDER BY count DESC LIMIT 20;"
        )
        connection.execute(sql)
        specjalizacje_records = connection.fetchall()
        specjalizacje_counts = [{"specjalizacja": record[0], "count": record[1]} for record in specjalizacje_records]
        return specjalizacje_counts
    
    @staticmethod
    def count_technologie_mile_widziane_data(connection=connection):
        sql = (
            "SELECT TRIM(technologia)as technologia, COUNT(TRIM(technologia)) AS count FROM daily_technologie_mile_widziane "
            "WHERE TRIM(technologia) IS NOT NULL AND TRIM(technologia) != '' "
            f"GROUP BY TRIM(technologia) ORDER BY count DESC LIMIT 20;"
        )
        connection.execute(sql)
        technologie_mile_widziane_records = connection.fetchall()
        technologie_mile_widziane_counts = [
            {"technologia": record[0], "count": record[1]} for record in technologie_mile_widziane_records
        ]
        return technologie_mile_widziane_counts
    
    @staticmethod
    def count_technologie_wymagane_data(connection=connection):
        sql = (
            "SELECT TRIM(technologia) as technologia, COUNT(TRIM(technologia)) AS count FROM daily_technologie_wymagane "
            "WHERE TRIM(technologia) IS NOT NULL AND TRIM(technologia) != '' "
            f"GROUP BY TRIM(technologia) ORDER BY count DESC LIMIT 20;"
        )
        connection.execute(sql)
        technologie_wymagane_records = connection.fetchall()
        technologie_wymagane_counts = [
            {"technologia": record[0], "count": record[1]} for record in technologie_wymagane_records
        ]
        return technologie_wymagane_counts
    
    #historic:
    @staticmethod
    def get_historic_count_data(connection=connection):
        sql = "SELECT date, count FROM historic_count ORDER BY date ASC;"
        connection.execute(sql)
        historic_data = connection.fetchall()
        data_for_chart = [{"date": entry[0].strftime("%Y-%m-%d"), "count": entry[1]} for entry in historic_data]
        return data_for_chart
    
    @staticmethod
    def get_historic_etat_data(connection=connection):
        sql = (
            "SELECT `pełny etat`, `część etatu`, `dodatkowa / tymczasowa`, `date` "
            "FROM historic_etat "
            "ORDER BY date ASC;"
        )
        connection.execute(sql)
        historic_data = connection.fetchall()
        data_for_chart = [
            {"pełny etat": entry[0], "część etatu": entry[1], "dodatkowa / tymczasowa": entry[2], "date": entry[3].strftime("%Y-%m-%d")}
            for entry in historic_data
        ]
        return data_for_chart
    
    @staticmethod
    def get_historic_kontrakt_data(connection=connection):
        sql = (
            "SELECT `umowa o pracę`, `kontrakt B2B`, `umowa zlecenie`, `umowa o staż / praktyki`, `umowa o dzieło`, `umowa na zastępstwo`, `date` "
            "FROM historic_kontrakt "
            "ORDER BY date ASC;")
        connection.execute(sql)
        historic_data = connection.fetchall()
        data_for_chart = [{
                "umowa o pracę": entry[0],
                "kontrakt B2B": entry[1],
                "umowa zlecenie": entry[2],
                "umowa o staż / praktyki": entry[3],
                "umowa o dzieło": entry[4],
                "umowa na zastępstwo": entry[5],
                "date": entry[6].strftime("%Y-%m-%d")}
            for entry in historic_data
            ]
        return data_for_chart
    
    @staticmethod   
    def get_historic_management_level_data(connection=connection):
        sql = ( 
            "SELECT `Mid`, `asystent`, `Junior`, `Senior`, `ekspert`, `team manager`, `menedżer`, `praktykant / stażysta`, `dyrektor`, `date` "
            "FROM historic_management_level "
            "ORDER BY date ASC ")
        connection.execute(sql)
        historic_data = connection.fetchall()
        data_for_chart = [
            {
                "Mid": entry[0],
                "asystent": entry[1],
                "Junior": entry[2],
                "Senior": entry[3],
                "ekspert": entry[4],
                "team manager": entry[5],
                "menedżer": entry[6],
                "praktykant / stażysta": entry[7],
                "dyrektor": entry[8],
                "date": entry[9].strftime("%Y-%m-%d"),
            }
            for entry in historic_data
        ]
        return data_for_chart
    
    @staticmethod
    def get_historic_work_type_data(connection=connection):
        sql = (
            "SELECT `praca hybrydowa`,  `praca zdalna`,  `praca stacjonarna`,  `praca mobilna`, `date` "
            "FROM historic_work_type "
            "ORDER BY date ASC ")
        connection.execute(sql)
        historic_data = connection.fetchall()
        data_for_chart = [
            {
                "praca hybrydowa": entry[0],
                "praca zdalna": entry[1],
                "praca stacjonarna": entry[2],
                "praca mobilna": entry[3],
                "date": entry[4].strftime("%Y-%m-%d"),
            }
            for entry in historic_data
        ]
        return data_for_chart
    
    @staticmethod
    def get_historic_technologie_mile_widziane_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, technologia, count, ROW_NUMBER() OVER (PARTITION BY date ORDER BY count DESC) AS row_num FROM historic_technologie_mile_widziane ) SELECT date, technologia, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "technologia": row[1],
                "count": row[2]
            })
        return data_for_chart

    @staticmethod
    def get_historic_technologie_wymagane_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, technologia, count, ROW_NUMBER() OVER (PARTITION BY date ORDER BY count DESC) AS row_num FROM historic_technologie_wymagane ) SELECT date, technologia, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "technologia": row[1],
                "count": row[2]
            })
        return data_for_chart

    @staticmethod
    def get_historic_location_data(connection=connection):
        sql = "WITH RECURSIVE ranked AS ( SELECT date, location, count, ROW_NUMBER() OVER ( PARTITION BY date ORDER BY count DESC ) AS row_num FROM historic_location) SELECT date, location, count FROM ranked WHERE row_num <= 20 ORDER BY date;"
        connection.execute(sql)
        data_for_chart = []
        for row in connection.fetchall():
            data_for_chart.append({
                "date": row[0].strftime("%Y-%m-%d"),
                "location": row[1],
                "count": row[2]
            })
        return data_for_chart


#old shit
#class itpracujpl_interaction:
#    class data(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        title = itpracujpl_db.Column(itpracujpl_db.String(255))
#        company = itpracujpl_db.Column(itpracujpl_db.String(255))
#        location = itpracujpl_db.Column(itpracujpl_db.String(255))
#        salary = itpracujpl_db.Column(itpracujpl_db.Integer)
#        doswiadczenie = itpracujpl_db.Column(itpracujpl_db.Integer)
#
#        @classmethod
#        def count_all(cls):
#            return cls.query.count()
#
#        @classmethod
#        def count_records_with_positive_salary(cls):
#            total_count = cls.query.count()
#            positive_salary_count = cls.query.filter(cls.salary > 0).count()
#            if total_count == 0:
#                return 0
#            percentage = (positive_salary_count / total_count) * 100
#            return math.floor(percentage)
#        
#        @classmethod
#        def most_common_locations(cls, limit=20):
#            query = itpracujpl_db.session.query(cls.location, func.count(cls.location).label("count")).\
#                filter(cls.location.isnot(None), cls.location != '').\
#                group_by(cls.location).\
#                order_by(func.count(cls.location).desc()).\
#                limit(limit).all()
#            most_common_locations = [{"location": location, "count": count} for location, count in query]
#            return most_common_locations
#        
#        @classmethod
#        def get_salary_counts(cls):
#            salary_counts = {
#                "Poniżej 4000":  cls.query.filter(cls.salary >= 1, cls.salary <= 4000).count(),
#                "4000 - 5000": cls.query.filter(cls.salary >= 4000, cls.salary < 5000).count(),
#                "5000 - 6000": cls.query.filter(cls.salary >= 5000, cls.salary < 6000).count(),
#                "6000 - 7000": cls.query.filter(cls.salary >= 6000, cls.salary < 7000).count(),
#                "7000 - 8000": cls.query.filter(cls.salary >= 7000, cls.salary < 8000).count(),
#                "8000 - 10000": cls.query.filter(cls.salary >= 7000, cls.salary < 8000).count(),
#                "10000 - 12000": cls.query.filter(cls.salary >= 7000, cls.salary < 8000).count(),
#                "12000 i powyżej": cls.query.filter(cls.salary >= 12000).count(),
#            }
#            return salary_counts
#            
#
#    class etat(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        etat = itpracujpl_db.Column(itpracujpl_db.String(255))
#
#        @classmethod
#        def count_etat_data(cls):
#            etat_counts = defaultdict(int)
#            etat_records = cls.query.all()
#            for record in etat_records:
#                etat_counts[record.etat] += 1
#            return etat_counts
#
#    class kontrakt(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        kontrakt = itpracujpl_db.Column(itpracujpl_db.String(255))
#
#        @classmethod
#        def count_kontrakt_data(cls):
#            kontrakt_counts = defaultdict(int)
#            kontrakt_records = cls.query.all()
#            for record in kontrakt_records:
#                kontrakt_counts[record.kontrakt] += 1
#            return kontrakt_counts
#
#    class management_level(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        management_level = itpracujpl_db.Column(itpracujpl_db.String(255))
#
#        @classmethod
#        def count_management_level_data(cls):
#            management_level_counts = defaultdict(int)
#            management_level_records = cls.query.all()
#            for record in management_level_records:
#                management_level_counts[record.management_level] += 1
#            return management_level_counts
#    
#    class work_type(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        work_type = itpracujpl_db.Column(itpracujpl_db.String(255))
#
#        @classmethod
#        def count_work_type_data(cls):
#            work_type_counts = defaultdict(int)
#            work_type_records = cls.query.all()
#            for record in work_type_records:
#                work_type_counts[record.work_type] += 1
#            return work_type_counts
#    
#    class specjalizacje(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        specjalizacja = itpracujpl_db.Column(itpracujpl_db.String(255))
#
#        @classmethod
#        def count_specjalizacje_data(cls, limit=20):
#            query = itpracujpl_db.session.query(cls.specjalizacja, func.count(cls.specjalizacja).label("count")).\
#                filter(cls.specjalizacja.isnot(None), cls.specjalizacja != '').\
#                group_by(cls.specjalizacja).\
#                order_by(func.count(cls.specjalizacja).desc()).\
#                limit(limit).all()
#            specjalizacje_counts = [{"specjalizacja": spec, "count": count} for spec, count in query]
#            return specjalizacje_counts
#    
#    class technologie_mile_widziane(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        technologia = itpracujpl_db.Column(itpracujpl_db.String(255))
#
#        @classmethod
#        def count_technologie_mile_widziane_data(cls, limit=20):
#            query = itpracujpl_db.session.query(cls.technologia, func.count(cls.technologia).label("count")).\
#                filter(cls.technologia.isnot(None), cls.technologia != '').\
#                group_by(cls.technologia).\
#                order_by(func.count(cls.technologia).desc()).\
#                limit(limit).all()
#            technologie_mile_widziane_counts = [{"technologia": spec, "count": count} for spec, count in query]
#            return technologie_mile_widziane_counts
#    
#    class technologie_wymagane(itpracujpl_db.Model):
#        id = itpracujpl_db.Column(itpracujpl_db.Integer, primary_key=True)
#        technologia = itpracujpl_db.Column(itpracujpl_db.String(255))
#
#        @classmethod
#        def count_technologie_wymagane_data(cls, limit=20):
#            query = itpracujpl_db.session.query(cls.technologia, func.count(cls.technologia).label("count")).\
#                filter(cls.technologia.isnot(None), cls.technologia != '').\
#                group_by(cls.technologia).\
#                order_by(func.count(cls.technologia).desc()).\
#                limit(limit).all()
#            technologie_wymagane_counts = [{"technologia": spec, "count": count} for spec, count in query]
#            return technologie_wymagane_counts
#
#    class historic_count(itpracujpl_db.Model):
#        count = itpracujpl_db.Column(itpracujpl_db.Integer)
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#        
#        @classmethod
#        def get_historic_count_data(cls):
#            historic_data = cls.query.all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "date": entry.date.strftime("%Y-%m-%d"),
#                    "count": entry.count
#                })
#            return data_for_chart
#
#    class historic_etat(itpracujpl_db.Model):
#        __tablename__ = 'historic_etat'
#        pełny_etat = itpracujpl_db.Column(itpracujpl_db.Integer, name="pełny etat")
#        część_etatu = itpracujpl_db.Column(itpracujpl_db.Integer, name="część etatu")
#        dodatkowa_tymczasowa = itpracujpl_db.Column(itpracujpl_db.Integer, name="dodatkowa / tymczasowa")
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#
#        @classmethod
#        def get_historic_etat_data(cls):
#            historic_data = cls.query.all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "pełny etat": entry.pełny_etat,
#                    "część etatu": entry.część_etatu,
#                    "dodatkowa / tymczasowa": entry.dodatkowa_tymczasowa,
#                    "date": entry.date.strftime("%Y-%m-%d")
#                })
#            return data_for_chart
#        
#    class historic_kontrakt(itpracujpl_db.Model):
#        uop = itpracujpl_db.Column(itpracujpl_db.Integer, name="umowa o pracę")
#        b2b = itpracujpl_db.Column(itpracujpl_db.Integer, name="kontrakt B2B")
#        uz = itpracujpl_db.Column(itpracujpl_db.Integer, name="umowa zlecenie")
#        us = itpracujpl_db.Column(itpracujpl_db.Integer, name="umowa o staż / praktyki")
#        ud = itpracujpl_db.Column(itpracujpl_db.Integer, name="umowa o dzieło")
#        unz = itpracujpl_db.Column(itpracujpl_db.Integer, name="umowa na zastępstwo")
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#        
#        @classmethod
#        def get_historic_kontrakt_data(cls):
#            historic_data = cls.query.all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "umowa o pracę": entry.uop,
#                    "kontrakt B2B": entry.b2b,
#                    "umowa zlecenie": entry.uz,
#                    "umowa o staż / praktyki": entry.us,
#                    "umowa o dzieło": entry.ud,
#                    "umowa na zastępstwo": entry.unz,
#                    "date": entry.date.strftime("%Y-%m-%d"),
#                })
#            return data_for_chart
#        
#    class historic_management_level(itpracujpl_db.Model):
#        Mid = itpracujpl_db.Column(itpracujpl_db.Integer, name="Mid")
#        asystent = itpracujpl_db.Column(itpracujpl_db.Integer, name="asystent")
#        Junior = itpracujpl_db.Column(itpracujpl_db.Integer, name="Junior")
#        Senior = itpracujpl_db.Column(itpracujpl_db.Integer, name="Senior")
#        ekspert = itpracujpl_db.Column(itpracujpl_db.Integer, name="ekspert")
#        tm = itpracujpl_db.Column(itpracujpl_db.Integer, name="team manager")
#        menedżer = itpracujpl_db.Column(itpracujpl_db.Integer, name="menedżer")
#        praktykant = itpracujpl_db.Column(itpracujpl_db.Integer, name="praktykant / stażysta")
#        dyrektor = itpracujpl_db.Column(itpracujpl_db.Integer, name="dyrektor")
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#        
#        @classmethod
#        def get_historic_management_level_data(cls):
#            historic_data = cls.query.all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "Mid": entry.Mid,
#                    "asystent": entry.asystent,
#                    "Junior": entry.Junior,
#                    "Senior": entry.Senior,
#                    "ekspert": entry.ekspert,
#                    "team manager": entry.tm,
#                    "menedżer": entry.menedżer,
#                    "praktykant / stażysta": entry.praktykant,
#                    "dyrektor": entry.dyrektor,
#                    "date": entry.date.strftime("%Y-%m-%d"),
#                })
#            return data_for_chart
#        
#    class historic_work_type(itpracujpl_db.Model):
#        hybrydowa = itpracujpl_db.Column(itpracujpl_db.Integer, name="praca hybrydowa")
#        zdalna = itpracujpl_db.Column(itpracujpl_db.Integer, name="praca zdalna")
#        stacjonarna = itpracujpl_db.Column(itpracujpl_db.Integer, name="praca stacjonarna")
#        mobilna = itpracujpl_db.Column(itpracujpl_db.Integer, name="praca mobilna")
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#    
#        @classmethod
#        def get_historic_work_type_data(cls):
#            historic_data = cls.query.all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "praca hybrydowa": entry.hybrydowa,
#                    "praca zdalna": entry.zdalna,
#                    "praca stacjonarna": entry.stacjonarna,
#                    "praca mobilna": entry.mobilna,
#                    "date": entry.date.strftime("%Y-%m-%d"),
#                })
#            return data_for_chart
#        
#
#    class historic_technologie_mile_widziane(itpracujpl_db.Model):
#        technologia = itpracujpl_db.Column(itpracujpl_db.String(255))
#        count = itpracujpl_db.Column(itpracujpl_db.Integer)
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#
#        @classmethod
#        def get_historic_technologie_mile_widziane_data(cls):
#            subq = (
#                itpracujpl_db.session.query(
#                    cls.date.label('date'),
#                    cls.technologia.label('technologia'),
#                    cls.count.label('count'),
#                    func.row_number().over(
#                        partition_by=cls.date,
#                        order_by=cls.count.desc()
#                    ).label('row_num')
#                )
#                .cte('ranked', recursive=True)
#            )
#            ranked = aliased(subq)
#            historic_data = itpracujpl_db.session.query(
#                ranked.c.date,
#                ranked.c.technologia,
#                ranked.c.count
#            ).filter(
#                ranked.c.row_num <= 20
#            ).order_by(
#                ranked.c.date
#            ).all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "date": entry.date.strftime("%Y-%m-%d"),
#                    "technologia": entry.technologia,
#                    "count": entry.count,
#                })
#            return data_for_chart
#    
#    class historic_technologie_wymagane(itpracujpl_db.Model):
#        technologia = itpracujpl_db.Column(itpracujpl_db.String(255))
#        count = itpracujpl_db.Column(itpracujpl_db.Integer)
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#    
#        @classmethod
#        def get_historic_technologie_wymagane_data(cls):
#            subq = (
#                itpracujpl_db.session.query(
#                    cls.date.label('date'),
#                    cls.technologia.label('technologia'),
#                    cls.count.label('count'),
#                    func.row_number().over(
#                        partition_by=cls.date,
#                        order_by=cls.count.desc()
#                    ).label('row_num')
#                )
#                .cte('ranked', recursive=True)
#            )
#            ranked = aliased(subq)
#            historic_data = itpracujpl_db.session.query(
#                ranked.c.date,
#                ranked.c.technologia,
#                ranked.c.count
#            ).filter(
#                ranked.c.row_num <= 20
#            ).order_by(
#                ranked.c.date
#            ).all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "date": entry.date.strftime("%Y-%m-%d"),
#                    "technologia": entry.technologia,
#                    "count": entry.count,
#                })
#            return data_for_chart
#        
#    class historic_location(itpracujpl_db.Model):
#        location = itpracujpl_db.Column(itpracujpl_db.String(255))
#        count = itpracujpl_db.Column(itpracujpl_db.Integer)
#        date = itpracujpl_db.Column(itpracujpl_db.Date, primary_key=True)
#    
#        @classmethod
#        def get_historic_location_data(cls):
#            subq = (
#                itpracujpl_db.session.query(
#                    cls.date.label('date'),
#                    cls.location.label('location'),
#                    cls.count.label('count'),
#                    func.row_number().over(
#                        partition_by=cls.date,
#                        order_by=cls.count.desc()
#                    ).label('row_num')
#                )
#                .cte('ranked', recursive=True)
#            )
#            ranked = aliased(subq)
#            historic_data = itpracujpl_db.session.query(
#                ranked.c.date,
#                ranked.c.location,
#                ranked.c.count
#            ).filter(
#                ranked.c.row_num <= 20
#            ).order_by(
#                ranked.c.date
#            ).all()
#            data_for_chart = []
#            for entry in historic_data:
#                data_for_chart.append({
#                    "date": entry.date.strftime("%Y-%m-%d"),
#                    "location": entry.location,
#                    "count": entry.count,
#                })
#            return data_for_chart