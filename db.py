# persistent DB connection by putting it in a module
# (cus python only load modules once)
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


class Database:
    def __init__(self):
        self.mysql = None
        self.app = None

    def init_app(self, app):
        print("Grabbing fresh connection to Database")
        self.app = app

        self.app.config['MYSQL_DATABASE_USER'] = 'root'
        self.app.config['MYSQL_DATABASE_PASSWORD'] = 'lol'
        self.app.config['MYSQL_DATABASE_DB'] = 'chimken_dinner'
        self.app.config['MYSQL_DATABASE_HOST'] = 'sql-lol.duckdns.org'

        try:
            # Initialize MySQL extension
            self.mysql = MySQL()
            self.mysql.init_app(app)
            print("Database initialized successfully!")
        except Exception as e:
            print(f"Error initializing database: {e}")

    def get_db(self):
        return self.mysql.connect()

    def get_cursor(self):
        return self.mysql.get_db().cursor(DictCursor)
