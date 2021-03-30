#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re
import logging
import datetime
import csv


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
    logging.Logger.__name__ = "user_data"
    logging.Logger.setLevel(logging.INFO)
    logging.StreamHandler(RedactingFormatter)
    return logging.Logger


f = []
with open('user_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    f = [row for row in reader][0]

PII_FIELDS = (f[0], f[1], f[2], f[3], f[4])
