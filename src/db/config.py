from os import environ

defaults = {
    "DB_HOST": "localhost",
    "DB_NAME": "carto_test",
    "DB_PORT": 5432,
    "DB_USER": "postgres",
    "DB_PASSWORD": "password",
}


class Config:
    DATABASE_HOST = environ.get("DB_HOST") or defaults["DB_HOST"]
    DATABASE_NAME = environ.get("DB_NAME") or defaults["DB_NAME"]
    DATABASE_PORT = environ.get("DB_PORT") or defaults["DB_PORT"]
    DATABASE_USER = environ.get("DB_USER") or defaults["DB_USER"]
    DATABASE_PASSWORD = environ.get("DB_PASSWORD") or defaults["DB_PASSWORD"]
