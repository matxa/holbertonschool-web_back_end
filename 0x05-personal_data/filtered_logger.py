#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List, Tuple
import re
import logging
import datetime
import csv


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format"""
        return filter_datum(
            self.fields, self.REDACTION, super().format(
                record), self.SEPARATOR)


def filter_datum(
     fields: List[str], redaction: str, message: str, separator: str) -> str:
    """hash values"""
    for field in fields:
        message = re.sub(r"(?<={}=)(.*?(?={}))".format(
            field, separator), redaction, message)
    return message


def get_logger() -> logging.Logger:
    """logging"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(logging.StreamHandler().setFormatter(RedactingFormatter))
    return logger
