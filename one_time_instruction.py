import mysql.connector

conn = mysql.connector.connect(
            user='tomka',
            password='ieyah',
            host='192.168.0.22',
            database='db',
        )

create_movies_table_query = """
CREATE TABLE users_info(
    user_id VARCHAR(100) PRIMARY KEY,
    user_surname VARCHAR(100),
    user_first_name VARCHAR(100),
    user_patronymic VARCHAR(100)
)
"""

with conn.cursor() as cursor:
    cursor.execute(create_movies_table_query)
    conn.commit()

conn.close()