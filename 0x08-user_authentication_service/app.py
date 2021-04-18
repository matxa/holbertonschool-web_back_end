#!/usr/bin/env python3
""" App module """
from flask import Flask, jsonify, request, abort
from sqlalchemy.orm.exc import NoResultFound
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ Login user
    """
    if "email" in request.form.keys() and "password" in request.form.keys():
        try:
            email = request.form['email']
            password = request.form['password']
            if AUTH.valid_login(email, password):
                session_id = AUTH.create_session(email)
                response = {
                    "email": "{}".format(email),
                    "message": "logged in"
                }
                response = jsonify(response)
                response.set_cookie("session_id", session_id)
                return response
            else:
                abort(401)
        except NoResultFound:
            abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
