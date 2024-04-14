#!/usr/bin/env python3
""" Get locale from request. """
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """App configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Method to determine the best match for supported languages."""
    # print(app.config['LANGUAGES'])
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Route to root."""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.route(host="0.0.0.0", port=5000)
