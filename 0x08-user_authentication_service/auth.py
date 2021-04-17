#!/usr/bin/env python3
""" Auth Model """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hash a input password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
