# Based on https://github.com/codefresh-contrib/python-flask-sample-app

import os

from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        PASSWORD="password",
        # store the database in the instance folder
        # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    # TODO: conditionalize
    from gpiozero.pins.mock import MockFactory
    from gpiozero import Device
    Device.pin_factory = MockFactory()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # apply the blueprints to the app
    from fanpi import fan_app

    app.register_blueprint(fan_app.bp)
    app.add_url_rule("/", endpoint="fan.index")

    return app
