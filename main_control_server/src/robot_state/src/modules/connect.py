# pip install mysql-connector-python
import mysql.connector as con

class Connect():
    def __init__(self, User, Password):
        self.conn = con.connect(
<<<<<<< HEAD
            # host='database-1.cdigc6umyoh0.ap-northeast-2.rds.amazonaws.com',
=======
            host='localhost',
>>>>>>> 07b9818d4ac797aa0a4b0603716d9c00cfa10a66
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