#!/usr/bin/env python3
"""Returns the list of school having a specific topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns list of schools and the specific topics"""
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(schools)
