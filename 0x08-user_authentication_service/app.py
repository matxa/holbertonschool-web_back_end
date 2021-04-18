#!/usr/bin/env python3
""" App module """
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Home endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register():
    """ Register User
    """
    if "email" in request.form.keys() and "password" in request.form.keys():
        try:
            email = request.form['email']
            pwd = request.form['password']
            AUTH.register_user(email, pwd)
            return jsonify({
                "email": "{}".format(email),
                "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400

    return jsonify({"message": "missing parameters email or password"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
