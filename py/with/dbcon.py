import MySQLdb as mysql

class DatabaseConnection(object):

    def __enter__(self):
        # make a database connection and return it
        self.db = mysql.connect(
            host="shadow.corp.vewd.com",
                user='root',
                passwd='root',
                db='performance_test',
        )
        self.db.autocommit(False)
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.db.close()
try:
    with DatabaseConnection() as db:
        print("coś tam robimy na bazie")
except:
    print("error connection to db")
