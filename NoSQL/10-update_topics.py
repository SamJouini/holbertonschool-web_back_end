#!/usr/bin/env python3
"""Changes all topics of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name.
    Returns the number of documents updated."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )