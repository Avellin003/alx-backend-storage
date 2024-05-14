#!/usr/bin/env python3

"""def that lists everything"""
import pymongo


def list_all(mongo_collection):
    """
    parses through every files
    """
    if mongo_collection is None:
        return []
    files = mongo_collection.find()
    return [file for file in files]
