#!/usr/bin/env python3
"""
Retrieve schools by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find schools in the collection that cover a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic: The topic to search for.

    Returns:
        pymongo.cursor.Cursor: A cursor to the documents matching the topic.
    """
    # Find schools covering the specified topic
    return mongo_collection.find({"topics": {"$in": [topic]}})
