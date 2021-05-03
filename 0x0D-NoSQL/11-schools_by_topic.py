#!/usr/bin/env python3
""" returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ return school by topic
    """
    schools = mongo_collection.find({
        "topics": {
            "$in": [topic]
        }
    })
    return schools
