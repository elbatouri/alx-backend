#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Get locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Route for homepage"""
    return render_template('3-index.html', title=_("home_title"), header=_("home_header"))

if __name__ == "__main__":
    app.run()
