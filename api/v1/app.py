#!/usr/bin/python3

"""flask application file"""

from flask import Flask
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close current session"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """404 error handler"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":

    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)
