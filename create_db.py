from mysql.connector import connect, Error
from decouple import config

try:
    configValue = {
        'host': "localhost",
        'user': config('username'),
        'password': config('password')
    }
    with connect(**configValue) as connection:
        create_db_query = "CREATE DATABASE audit_system"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            connection.commit()
            print("Database created successfully")
except Error as e:
    print(e)