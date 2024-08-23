#!/usr/bin/env python3
""" Lists all documents in a collection"""

def list_all(mongo_collection):
    """Lists all documents in a collection/
    Return an empty list if no document."""
    docs = mongo_collection.find()
    result = []
    for doc in docs:
        result.append(doc)
    return result
