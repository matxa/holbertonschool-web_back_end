#!/usr/bin/env python3
""" Flask App """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict


class Config:
    """ Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict or None:
    """ Get user from url param
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        try:
            return users[int(user_id)]
        except Exception:
            return None
    return None


@babel.localeselector
def get_locale() -> str:
    """ Get locale
    """
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.before_request
def before_request():
    """ Before request decorator
    """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Home endpoint
    """
    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
