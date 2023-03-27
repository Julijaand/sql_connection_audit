from mysql.connector import connect, Error
from decouple import config

# insert data

try:
    configValue = {
        'host': "localhost",
        'user': config('username'),
        'password': config('password'),
        'database': 'audit_system'
    }
    with connect(**configValue) as connection:
        insert_query = """
            INSERT INTO users (name, surname) 
            VALUES ("%s", "%s")
            """
        users = [
            ("Ann", "Johnson"),
            ("Peter", "Anderson"),
            ("Josh", "Pikalson")
        ]
        with connection.cursor() as cursor:
            cursor.executemany(insert_query, users)
            connection.commit()
except Error as e:
    print(e)