import mysql.connector

class Requester:

    def make_connection(self):
        conn = mysql.connector.connect(
            user='tomka',
            password='ieyah',
            host='192.168.0.19',
            database='db',
        )

        return conn

    def return_value_from_bd(self, column_to_return, table, column_to_check, value_to_check):
        conn = self.make_connection()
        get_query = f"""SELECT {column_to_return} FROM {table} WHERE {column_to_check} = '{value_to_check}'"""
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(get_query)

        conn.close()
        return cursor.fetchone()

    def return_list_of_values_from_bd(self):
        conn = self.make_connection()
        get_query = f"""SELECT * FROM users"""
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(get_query)

        conn.close()
        return cursor.fetchall()

    def insert_certificate_id(self, certificate_id):
        conn = self.make_connection()
        insert_query = f"""INSERT INTO certificate_ids (certificate_id) VALUES ('{certificate_id}')"""
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(insert_query)
            conn.commit()

        conn.close()

    def insert_user(self, certificate_id, user_id, university_id, surname, first_name, patronymic):
        conn = self.make_connection()
        first_insert_query = \
            f"""INSERT INTO users (certificate_id, user_id, university_id) VALUES ('{certificate_id}', '{user_id}', '{university_id}')"""
        second_insert_quety = f"""INSERT INTO users_info (user_id, user_surname, user_first_name, user_patronymic) VALUES 
                                ('{user_id}', '{surname}', '{first_name}', '{patronymic}')"""

        with conn.cursor(buffered=True) as cursor:
            cursor.execute(first_insert_query)
            cursor.execute(second_insert_quety)
            conn.commit()

        conn.close()
