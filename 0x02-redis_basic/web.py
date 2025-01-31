#!/usr/bin/env python3
'''A module that provides tools for caching HTTP requests
and tracking request counts using Redis.'''

import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''A Redis client instance used for caching request results
and tracking request counts.'''


def data_cacher(method: Callable) -> Callable:
    '''A decorator that caches the response of an HTTP request
    and tracks the number of times a URL is requested.'''

    @wraps(method)
    def invoker(url: str) -> str:
        '''Increments the request count,
        retrieves cached data if available, 
        or fetches and caches the response if not.
        '''
        # Increment the request count for the given URL
        redis_store.incr(f'count:{url}')

        # Check if the response is already cached
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        # Fetch the response if not cached
        result = method(url)

        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)

        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Fetches the content of a given URL,
    caches the response,
    and tracks request counts.'''
    return requests.get(url).text
