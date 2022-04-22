import sys
import psycopg2
import psycopg2.extras

from db.config import Config


class Database:
    """PostgreSQL database class"""

    def __init__(self, config):
        self.host = config.DATABASE_HOST
        self.dbname = config.DATABASE_NAME
        self.port = config.DATABASE_PORT
        self.user = config.DATABASE_USER
        self.password = config.DATABASE_PASSWORD
        self.conn = None

    def connect(self):
        """Connect to a PostgreSQL database"""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    dbname=self.dbname,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                )
                print("Connection opened successfully")
            except psycopg2.DatabaseError as e:
                print(e)
                sys.exit()


db_config = Config()

db = Database(db_config)
db.connect()
