#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re


def filter_datum(
     fields: List, redaction: str, message: str, separator: str) -> str:
    for field in fields:
        message = re.sub(r"(?<={}=)(.*?(?={}))".format(
            field, separator), redaction, message)
    return message
