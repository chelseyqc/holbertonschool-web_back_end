#!/usr/bin/env python3
"""Lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a collection and returns a list"""
    documents = mongo_collection.find()
    return list(documents)
