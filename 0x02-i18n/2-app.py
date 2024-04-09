#!/usr/bin/env python3
""" Get locale from request. """
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class to configure available language and time zone in our app.
    """

    LANGUAGES = ["en", "fr"]
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Method to determine the bet match for supportd languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Route to root."""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.route(host="0.0.0.0", port="5000")
