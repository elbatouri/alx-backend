#!/usr/bin/env python3

"""
This module implements a Flask application that provides greetings in different languages based on the specified locale.
"""

from flask import Flask, request
from typing import Optional

app = Flask(__name__)

# Supported locales
SUPPORTED_LOCALES = ['en', 'fr']

# Default locale
DEFAULT_LOCALE = 'en'


def get_locale() -> str:
    """
    Get the locale from the request parameters.

    Returns:
        str: The locale obtained from the request parameters.
    """
    locale = request.args.get('locale')
    if locale and locale in SUPPORTED_LOCALES:
        return locale
    return DEFAULT_LOCALE


@app.route('/')
def hello_world() -> str:
    """
    Return a greeting message based on the locale.

    Returns:
        str: The greeting message in the appropriate language.
    """
    locale = get_locale()
    if locale == 'fr':
        return 'Bonjour, monde!'
    else:
        return 'Hello, world!'


if __name__ == '__main__':
    app.run(debug=True)
