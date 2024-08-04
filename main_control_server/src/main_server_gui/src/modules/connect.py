# pip install mysql-connector-python
import mysql.connector as con

class Connect():
    def __init__(self, User, Password):
        self.conn = con.connect(
            host='localhost',
            user=User,
            password=Password,
            database='DFC_system_db'
        )
        self.cursor = self.conn.cursor(buffered=True)

    def disConnection(self):
        if self.conn:
            print('!!!!!!DB SHUT DOWN!!!!!!')
            self.conn.close()
            self.cursor.close()
            self.conn = None