from flask import Blueprint, jsonify, make_response
from db.database import db
from . import cache


bp = Blueprint("madrid_community", __name__)


@bp.route("/madrid_community", methods=["GET"])
@cache.cached()
def madrid_community():
    """Returns postal codes entities including geometry"""

    query = """
        SELECT
            ST_Union(postal_codes.the_geom) AS the_geom,
            (SELECT
                SUM(amount) AS amount
            FROM
                paystats
            )
        FROM
            postal_codes
        ;
    """
    data = None

    try:
        cur = db.conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
    except Exception as e:
        print("Query '{}' failed: ".format("/madrid_community"), e)

    if data:
        response = {"data": data}
        status_code = 200
    else:
        response = {"error": "data could not be retrieved"}
        status_code = 500

    return make_response(jsonify(response), status_code)
