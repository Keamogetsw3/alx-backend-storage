#!/usr/bin/env python3
""" 11 module """


def schools_by_topic(mongo_collection, topic):
    '''11 module'''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
