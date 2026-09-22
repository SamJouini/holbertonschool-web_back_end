#!/usr/bin/env python3
"""Module for a basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for available languages in app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/")
def index() -> str:
    """Basic function that returns a basic template"""
    return render_template("5-index.html")


def get_locale() -> str:
    """Get the best match locale language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Optional[dict]:
    """Return a user dict or None"""
    login_as = request.args.get("login_as")
    if not login_as:
        return None

    try:
        user_id = int(login_as)
    except (ValueError, TypeError):
        return None

    return users.get(user_id)


@app.before_request
def before_request():
    """Find a user and set it as a global"""
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
