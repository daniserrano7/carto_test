from flask import Blueprint, request
from db.database import db


bp = Blueprint("accumulated", __name__, url_prefix="/accumulated")


@bp.route("/", methods=["GET"])
def total():
    return {"res": {"amount": 0}}


@bp.route("/by_age_gender", methods=["GET"])
def by_age_gender():
    params = request.args.to_dict()
    start_date = params.get("start_date")
    end_date = params.get("end_date")

    query = """
        SELECT
            paystats.age,
            paystats.gender,
            SUM(paystats.amount) AS amount
        FROM
            paystats
        WHERE
            (%(start_date)s IS NULL
                OR TO_DATE(%(start_date)s, 'DD-MM-YYYY') <= pay_date) AND
            (%(end_date)s IS NULL
                OR TO_DATE(%(end_date)s, 'DD-MM-YYYY') >= pay_date)
        GROUP BY
            paystats.age,
            paystats.gender
        ORDER BY
            paystats.age
        ;
    """
    values = {"start_date": start_date, "end_date": end_date}
    data = []

    try:
        cur = db.conn.cursor()
        cur.execute(query, values)
        data = cur.fetchall()
    except Exception as e:
        print("Query '{}' failed: ".format("/by_age_gender"), e)

    return {"res": data}
