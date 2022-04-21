from flask import Blueprint
from db.database import db


bp = Blueprint("zipcodes", __name__, url_prefix="/zipcodes")


@bp.route("/", methods=["GET"])
def zipcodes():
    cur = db.conn.cursor()

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
    data = []

    try:
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
    except Exception as e:
        print("Query '{}' failed: ".format("/zipcodes"), e)

    return {"res": data}


@bp.route("/<int:zipcode_id>", methods=["GET"])
def zipcode_id(zipcode_id):
    return {
        "res": {
            "zipcode_id": zipcode_id
        }
    }
