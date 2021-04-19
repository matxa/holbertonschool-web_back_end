#!/usr/bin/env python3
""" App module """
from flask import Flask, jsonify, request, abort, redirect, Response
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth
import subprocess


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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Logout user
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        AUTH.destroy_session(user_id=user.id)
        return redirect('/')
    return Response(status=403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ find user using session_id cookie
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        return jsonify({"email": "{}".format(user.email)}), 200
    return Response(status=403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ Get and reset password token
    """
    if "email" in request.form.keys():
        try:
            reset_token = AUTH.get_reset_password_token(request.form['email'])
            return jsonify({
                "email": "{}".format(request.form['email']),
                "reset_token": "{}".format(reset_token)})
        except ValueError:
            return Response(status=403)
    return Response(status=403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ Update users new_password using email and reset_token """
    form_keys = request.form.keys()
    if "email" in form_keys and "reset_token" in\
       form_keys and "new_password" in form_keys:

        email = request.form.get("email")
        reset_token = request.form.get("reset_token")
        password = request.form.get("new_password")

        try:
            AUTH.update_password(reset_token, password)
            return jsonify({
                "email": email,
                "message": "Password updated"}), 200
        except ValueError:
            return Response(status=403)
    return Response(status=403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
