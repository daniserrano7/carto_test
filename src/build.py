from server import app
from scripts.create_schema import create_schema
from scripts.populate_db import populate_db


def build():
    create_schema()
    populate_db()
    app.run()


if __name__ == "__main__":
    build()
