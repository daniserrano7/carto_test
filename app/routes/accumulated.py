from flask import Blueprint, request


# If we wanted to create several routes nested under "accumulated", we
# could create folder put every endpoint in a different file, all of
# them using the "accumulated" blueprint
bp = Blueprint("accumulated", __name__)


@bp.route("/accumulated", methods=["GET"])
def accumulated():
    params = request.args.to_dict()
    start_date = params.get("start_date")
    end_date = params.get("end_date")
    print(start_date, end_date)

    return "Accumulated endpoint"
