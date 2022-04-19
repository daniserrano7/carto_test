from scripts.create_schema import create_schema
from scripts.populate_db import populate_db


def setup():
    create_schema()
    populate_db()


if __name__ == "__main__":
    setup()
