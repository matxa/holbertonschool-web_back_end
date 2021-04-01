#!/usr/bin/env python3
""" basic_auth module
"""
from auth import Auth


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
