from flask import Blueprint, jsonify


bp = Blueprint("time_series", __name__, url_prefix="/time_series")


@bp.route("/by_age_gender", methods=["GET"])
def time_series():
    """Returns turnover by age and gender and, optionally, by
    start and/or end date
    """
    return jsonify({"data": []})
