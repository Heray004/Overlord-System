import mysql.connector
from Base import Sql_data


class DatabaseRead:
    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    def __sql_connect(self):
        conn = mysql.connector.connect(
            host=Sql_data.sql_host,
            user=Sql_data.sql_user,
            database=Sql_data.sql_database,
            password=Sql_data.sql_password,
            port=Sql_data.sql_port
        )
        cursor = conn.cursor()
        return conn, cursor

    def __sql_close(self, conn, cursor):
        cursor.close()
        conn.close()

    def get_voice(self):
        conn, cursor = self.__sql_connect()
        cursor.execute(
            "SELECT * FROM Voice WHERE Status = 'Waiting' ORDER BY id ASC LIMIT 2",
        )
        data = cursor.fetchall()
        self.__sql_close(conn=conn, cursor=cursor)
        return data

    def executed(self, voice_id):
        conn, cursor = self.__sql_connect()
        cursor.execute(
            "UPDATE Voice SET Status = 'Executed' WHERE id = %s",
            (voice_id,)
        )
        conn.commit()
        self.__sql_close(conn=conn, cursor=cursor)

    def deny(self, voice_id):
        conn, cursor = self.__sql_connect()
        cursor.execute(
            "UPDATE Voice SET Status = 'Deny' WHERE id = %s",
            (voice_id,)
        )
        conn.commit()
        self.__sql_close(conn=conn, cursor=cursor)