#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re


def filter_datum(
     fields: List[str], redaction: str, message: str, separator: str) -> str:
    """hash values"""
    for field in fields:
        message = re.sub(r"(?<={}=)(.*?(?={}))".format(
            field, separator), redaction, message)
    return message
