from mysql.connector import connect, Error
from decouple import config

# create table users
try:
    with connect(
            host="localhost",
            user=config('username'),
            password=config('password'),
            database="audit_system",
    ) as connection:
        create_user_table_query = """
        CREATE TABLE users(
        user_id int auto_increment PRIMARY KEY,
        name varchar(30),
        surname varchar(30)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_user_table_query)
            connection.commit()
            print("Table created successfully")

# create table users_visit
        with connection.cursor() as cursor:
            create_user_visit_table_query = """
            CREATE TABLE users_visit(
            user_visit_id int auto_increment PRIMARY KEY,
            user_id int,
            foreign key(user_id) references users(user_id),
            user_login_time timestamp
    )
            """
            cursor.execute(create_user_visit_table_query)
            connection.commit()
            print("Table created successfully")

# update/edit data
        with connection.cursor() as cursor:
            update_query = "UPDATE `users` SET password = '' WHERE name = '';"
            cursor.execute(update_query)

# select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users`"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `users`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

except Error as e:
    print(e)
