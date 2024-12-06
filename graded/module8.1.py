import mysql.connector
from mysql.connector import connection


def get_airport_data(icao_code):
    sql = f"SELECT name, municipality FROM airports WHERE ident = '{icao_code}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport {row[0]} is in town {row[1]} with ICAO code {icao_code}")


connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='airport_db',
        user='dbuser',
        password='password',
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )

icao_code = input("Enter ICAO code: ")
get_airport_data(icao_code)

