import mysql.connector
from mysql.connector import errorcode
import os

class DBConnection():
    def init_conn(self):
        conn=None
        cursor=None
        
        host=os.environ['DB_HOST']
        user=os.environ["DB_USER"]
        password=os.environ["DB_PASSWORD"]
        database=os.environ["DB_DATABASE"]
        
        try:
         cnx = mysql.connector.connect(user=user,password=password,
                                      host=host,database=database)
         cursor=cnx.cursor()
         return cnx,cursor
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return "Something is wrong with your user name and password"
            elif err.errno == errorcode.ER_BA_DB_ERROR:
                return "Database doesn't exist"
            else:
                return(err)
        return(cnx,cursor)