#!/usr/bin/env python3
"""
insertion of a dcoment
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts based on keyword arguments
    """
    if not kwargs:
        return None
    # Insert the document into the collection
    insertions = mongo_collection.insert_one(kwargs).inserted_id

    return insertions
