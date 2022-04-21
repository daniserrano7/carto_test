from flask import Flask
from flask_compress import Compress
from routes import accumulated, time_series, zipcodes


app = Flask(__name__)

# Compresses all server http responses with gzip
app.config["COMPRESS_ALGORITHM"] = "gzip"
compress = Compress()
compress.init_app(app)

# Route registering
app.register_blueprint(accumulated.bp)
app.register_blueprint(time_series.bp)
app.register_blueprint(zipcodes.bp)
