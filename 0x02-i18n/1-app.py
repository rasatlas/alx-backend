#!/usr/bin/env python3
"""Basic Babel setup."""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class to configure available language in our app."""

    LANGUAGEs = ["en", "fr"]
    babel.default_locale = "en"
    babel.default_timezone = "UTC"


app.config.from_object(Config())


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Route to root."""
    return render_template("1-index.html")
