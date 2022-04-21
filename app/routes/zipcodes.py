from flask import Blueprint


bp = Blueprint("zipcodes", __name__)


@bp.route("/zipcodes", methods=["GET"])
def zipcodes():
    return "Zipcodes endpoint"
