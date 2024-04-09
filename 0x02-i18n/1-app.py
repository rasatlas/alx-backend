#!/usr/bin/env python3
"""Basic Babel setup."""
from flask_babel import Babel

babel = Babel()


class Config:
    """Config class to configure available language in our app."""
    LANGUAGEs = ["en", "fr"]
    babel.default_locale = "en"
    babel.default_timezone = "UTC"
