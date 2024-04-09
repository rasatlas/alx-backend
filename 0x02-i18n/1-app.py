#!/usr/bin/env python3
"""Basic Babel setup."""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Config class to configure available language in our app."""

    LANGUAGES = ["en", "fr"]
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


babel = Babel(app)
app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Route to root."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.route(host="0.0.0.0", port="5000")
