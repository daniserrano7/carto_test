from db.database import db


def create_schema():
    print("CREATING DATABASE SCHEMA")
    with open("scripts/schema.sql") as sql_file:
        schema_raw_sql = sql_file.read()

    try:
        cur = db.conn.cursor()
        cur.execute(schema_raw_sql)

        db.conn.commit()
    except Exception as e:
        print("Schema creation failed: ", e)
