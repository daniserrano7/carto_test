from flask import Blueprint


bp = Blueprint("time_series", __name__, url_prefix="/time_series")


@bp.route("/by_age_gender", methods=["GET"])
def time_series():
    return {"res": []}
