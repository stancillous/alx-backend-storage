#!/usr/bin/env python3
"""
func that lists all docs in a collection

"""


def list_all(mongo_collection):
    """func that lists all docs in a collection"""
    if mongo_collection is None:
        return []
    return mongo_collection.find()
