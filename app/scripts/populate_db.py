from db.database import db


def populate_db():
    print("POPULATING DATABASE")
    populate_postal_codes()
    populate_paystats()


def populate_postal_codes():
    cur = db.conn.cursor()

    with open("data/postal_codes.csv") as postal_code_csv:
        rows = postal_code_csv.readlines()

    headers = rows[0].split(",")
    column_index = get_columns_index(headers)

    # Iterate over the rows excluding the header
    for row in rows[1:]:
        query = """
            INSERT INTO postal_codes (
                id,
                code,
                the_geom
            ) VALUES (
                %(id)s,
                %(code)s,
                ST_Multi(%(the_geom)s)
            );
        """

        # Gets row values by column index using its name instead of
        # using directly its position
        columns = row.split(",")
        values = {
            "id": columns[column_index["id"]],
            "code": columns[column_index["code"]],
            "the_geom": columns[column_index["the_geom"]],
        }
        cur.execute(query, values)

    db.conn.commit()
    db.conn.close()


def populate_paystats():
    cur = db.conn.cursor()

    with open("data/paystats.csv") as paystats_csv:
        rows = paystats_csv.readlines()

    headers = rows[0].split(",")
    column_index = get_columns_index(headers)
    print("COLUMN INDEX: ", column_index)

    for row in rows[1:]:
        query = """
            INSERT INTO paystats (
                id,
                postal_code_id,
                pay_date,
                gender,
                age,
                amount
            ) VALUES (
                %(id)s,
                %(postal_code_id)s,
                TO_DATE(%(pay_date)s, 'YYYY-MM-DD'),
                %(gender)s,
                %(age)s,
                %(amount)s
            );
        """

        columns = row.split(",")
        values = {
            "id": columns[column_index["id"]],
            "postal_code_id": columns[column_index["postal_code_id"]],
            "pay_date": columns[column_index["p_month"]],
            "gender": columns[column_index["p_gender"]],
            "age": columns[column_index["p_age"]],
            "amount": columns[column_index["amount"]],
        }

        cur.execute(query, values)

    db.conn.commit()


def get_columns_index(headers):
    column_index = {}

    for i, header in enumerate(headers):
        column_index[header.strip()] = i

    return column_index
