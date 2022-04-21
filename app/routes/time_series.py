from flask import Blueprint, request


# If we wanted to create several routes nested under "time_series", we
# could create folder put every endpoint in a different file, all of
# them using the "time_series" blueprint
bp = Blueprint("zipcodes", __name__)


@bp.route("/time_series", methods=["GET"])
def time_series():
    params = request.args.to_dict()
    start_date = params.get("start_date")
    end_date = params.get("end_date")
    print(start_date, end_date)

    return "Time series endpoint"
