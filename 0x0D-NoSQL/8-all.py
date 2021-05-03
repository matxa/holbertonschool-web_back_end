#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """  lists all documents
    in a collection
    """
    collection_content = mongo_collection.find()
    return collection_content
