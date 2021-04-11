#!/usr/bin/env python3
""" auth module
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth
        """
        if path is not None:
            if path[-1] != '/':
                path = path + '/'
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ auth headers
        """
        if request is None:
            return None
        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user
        """
        return None

    def session_cookie(self, request=None) -> str:
        """ session cookie
        """
        if request is None:
            return None

        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
