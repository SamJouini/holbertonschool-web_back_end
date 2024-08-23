#!/usr/bin/env python3
"Returns the list of schools having a specific topics."


def schools_by_topic(mongo_collection, topic):
    """Returns a list of school documents that have the specified topic"""
    schools = mongo_collection.find({"topics": topic}),
    return list(schools)
