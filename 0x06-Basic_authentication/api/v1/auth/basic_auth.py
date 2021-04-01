#!/usr/bin/env python3
""" basic_auth module
"""
from .auth import Auth
import base64


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
