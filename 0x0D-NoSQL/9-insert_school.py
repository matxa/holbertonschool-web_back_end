#!/usr/bin/env python3
"""  inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ insert into school collection
    """
    document = mongo_collection.insert(kwargs)
    return document
