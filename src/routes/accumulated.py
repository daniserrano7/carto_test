from flask import Blueprint, request, jsonify, make_response
from db.database import db
from . import cache


bp = Blueprint("accumulated", __name__, url_prefix="/accumulated")


@bp.route("/", methods=["GET"])
def total():
    """Returns total payment amount"""

    return jsonify({"amount": 0})


# query_string=True allows different caching based
# on the query params values
@bp.route("/by_age_gender", methods=["GET"])
@cache.cached(query_string=True)
def by_age_gender():
    """Returns accumulated payment amount segregated by age and gender and,
    optionally, by start and/or end date
    """

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
    data = None

    try:
        cur = db.conn.cursor()
        cur.execute(query, values)
        data = cur.fetchall()
        cur.close()
    except Exception as e:
        print("Query '{}' failed: ".format("/by_age_gender"), e)

    if data:
        response = {"data": data}
        status_code = 200
    else:
        response = {"error": "data could not be retrieved"}
        status_code = 500

    return make_response(jsonify(response), status_code)
