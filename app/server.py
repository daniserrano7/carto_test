from flask import Flask
from routes import accumulated, time_series, zipcodes


app = Flask(__name__)

# Route registering
app.register_blueprint(accumulated.bp)
app.register_blueprint(time_series.bp)
app.register_blueprint(zipcodes.bp)
