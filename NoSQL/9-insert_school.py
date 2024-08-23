#!/usr/bin/env python3
"""Inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document into the MongoDB collection and returns the inserted document's ID.
    """
    document = kwargs
    inserted_doc = mongo_collection.insert_one(document)
    inserted_doc_id = inserted_doc.inserted_id
    return inserted_doc_id
