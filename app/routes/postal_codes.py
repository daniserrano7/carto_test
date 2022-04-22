from flask import Blueprint, jsonify, make_response
from db.database import db
from . import cache


bp = Blueprint("postal_codes", __name__, url_prefix="/postal_codes")


@bp.route("/", methods=["GET"])
@cache.cached()
def postal_codes():
    """Returns postal codes entities including geometry"""

    query = """
        SELECT
            postal_codes.id,
            postal_codes.code,
            ST_AsGeoJSON(
                ST_Transform(
                    postal_codes.the_geom,4326
                )
            ) AS the_geom
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
        print("Query '{}' failed: ".format("/postal_codes"), e)

    if data:
        response = {"data": data}
        status_code = 200
    else:
        response = {"error": "data could not be retrieved"}
        status_code = 500

    return make_response(jsonify(response), status_code)


@bp.route("/<int:postal_code_id>", methods=["GET"])
def postal_code_id(postal_code_id):
    return jsonify({"postal_code_id": postal_code_id})


# This endoint is proposed in order to separate
# geospatial data from its individual data.
# Depending on the context, it could have been more
# efficient to include entitie's data as feature
# properties and serve postal_codes as a whole GeoJSON
