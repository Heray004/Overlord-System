import mysql.connector
from Base import Sql_data


class DatabaseRead:
    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    def sql_connect(self):
        conn = mysql.connector.connect(
            host=Sql_data.sql_host,
            user=Sql_data.sql_user,
            database=Sql_data.sql_database,
            password=Sql_data.sql_password,
            port=Sql_data.sql_port
        )
        cursor = conn.cursor()
        return conn, cursor

    def sql_close(self, conn, cursor):
        cursor.close()
        conn.close()

    def get_voice(self, conn, cursor):
        cursor.execute(
            "SELECT * FROM Voice WHERE executed = 0 ORDER BY id ASC LIMIT 2",
        )
        data = cursor.fetchall()
        return data

    def executed(self, conn, cursor, voice_id):
        cursor.execute(
            "UPDATE Voice SET executed = 1 WHERE id = %s",
            (voice_id,)
        )
        conn.commit()
