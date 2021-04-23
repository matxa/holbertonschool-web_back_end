#!/usr/bin/env python3
""" Flask App """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Config class
    """
    LANGUAGES = ["en", "fr"]


babel = Babel(
    app=app,
    default_locale=Config.LANGUAGES[0],
    default_timezone='UTC')


app.config.from_object(Config())


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Home endpoint
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
