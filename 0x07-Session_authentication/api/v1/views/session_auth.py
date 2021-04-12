#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """ Auth Session
    """
    email = request.form.get("email")
    pwd = request.form.get("password")

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if pwd is None or pwd == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if len(user) < 1:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if user.is_valid_password(pwd) is False:
        return jsonify({"error": "wrong password"}), 401

    # IMPORT may cause circular import error
    from api.v1.app import auth
    cookie = os.getenv('SESSION_NAME')
    session_id = auth.create_session(user.id)

    res = jsonify(user.to_json())
    res.set_cookie(cookie, session_id)
    return res, 200


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def delete_session() -> str:
    """ Delete Session / LogOut
    """
    from api.v1.app import auth
    is_logout = auth.destroy_session(request)

    if is_logout is False:
        return abort(404)

    return jsonify({}), 200
