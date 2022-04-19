from os import environ

default_values = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'carto_test',
    'DB_PORT': 5432,
    'DB_USER': 'postgres',
    'DB_PASSWORD': 'password'
}


class Config:
    DATABASE_HOST = environ.get('DB_HOST') or default_values['DB_HOST']
    DATABASE_NAME = environ.get('DB_NAME') or default_values['DB_NAME']
    DATABASE_PORT = environ.get('DB_PORT') or default_values['DB_PORT']
    DATABASE_USER = environ.get('DB_USER') or default_values['DB_USER']
    DATABASE_PASSWORD = environ.get('DB_PASSWORD')  or default_values['DB_PASSWORD']
