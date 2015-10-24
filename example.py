#Import Flask and FlaskCasl
# This script can take a first argument giving a configuration from examples.py
from flask import Flask
from flask.ext.casl import Casl
from sys import argv
from pkg_resources import resource_filename


if __name__ == "__main__":
    # We create a Flask app
    app = Flask(
        __name__
    )

    # We set up Casl
    casl = Casl(
        app=app,
        name="casl"
    )
    # We register its routes
    casl.register_routes()

    # We run the app
    app.debug = True
    app.run()
