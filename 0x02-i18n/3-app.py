#!/usr/bin/env python3
""" Parametrize templates. """
from flask_babel import Babel, get_locale
from flask import Flask, render_template, request, g


class Config:
    """App configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale)


# @babel.localeselector
def get_locale() -> str:
    """Method to determine the best match for supported languages."""
    user = getattr(g, "user", None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Route to root."""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.route(host="0.0.0.0", port="5000")
