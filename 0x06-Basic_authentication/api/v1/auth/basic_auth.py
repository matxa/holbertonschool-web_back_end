#!/usr/bin/env python3
""" basic_auth module
"""
from .auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
         self, authorization_header: str) -> str:
        """ Ectract base64
        """
        if authorization_header is None or type(authorization_header) != str\
           or authorization_header.startswith("Basic ") is False:
            return None
        else:
            return authorization_header.split()[1]

    def decode_base64_authorization_header(
         self, base64_authorization_header: str) -> str:
        """ Decode base64
        """
        if base64_authorization_header is None or\
           type(base64_authorization_header) != str:
            return None
        try:
            is_it = base64.b64encode(base64.b64decode(
                base64_authorization_header)) == base64_authorization_header
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
         self, decoded_base64_authorization_header: str) -> (str, str):
        """ Decode base64 with extra credentials
        """
        if decoded_base64_authorization_header is None or\
           type(decoded_base64_authorization_header) != str or\
           ":" not in decoded_base64_authorization_header:
            return (None, None)
        return (
            decoded_base64_authorization_header.split(':')[0],
            decoded_base64_authorization_header.split(':')[1]
            )

    def user_object_from_credentials(
         self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Credentials
        """
        if user_email is None or type(user_email) != str or\
           user_pwd is None or type(user_pwd) != str:
            return None
        user = User().search({"email": user_email})
        if len(user) == 0 or user[0].is_valid_password(user_pwd) is False:
            return None
        else:
            return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        auth_header = self.authorization_header(request)
        self.extract_base64_authorization_header(auth_header)
        self.decode_base64_authorization_header(auth_header)
        credentials = self.extract_user_credentials("")
        self.user_object_from_credentials(credentials)
