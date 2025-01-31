#!/usr/bin/env python3
'''A module for interacting with Redis as a NoSQL data storage.
'''
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    '''Decorator that tracks the number of times a method is called
    within a Cache class.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Increments the call counter for the method before executing it.'''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    '''Decorator that records the input arguments and outputs of a method
    within a Cache class.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Stores the method's input arguments and result in Redis before returning the output.'''
        in_key = f'{method.__qualname__}:inputs'
        out_key = f'{method.__qualname__}:outputs'
        
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        
        output = method(self, *args, **kwargs)
        
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        
        return output
    return invoker


def replay(fn: Callable) -> None:
    '''Retrieves and displays the call history of a method decorated with @call_history.'''
    if fn is None or not hasattr(fn, '__self__'):
        return
    
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    
    fxn_name = fn.__qualname__
    in_key = f'{fxn_name}:inputs'
    out_key = f'{fxn_name}:outputs'
    
    call_count = int(redis_store.get(fxn_name) or 0)
    print(f'{fxn_name} was called {call_count} times:')
    
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print(f'{fxn_name}(*{fxn_input.decode("utf-8")}) -> {fxn_output}')


class Cache:
    '''A class for storing and retrieving data in Redis.'''
    
    def __init__(self) -> None:
        '''Initializes a Redis client and clears any existing data.'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores a given value in Redis and returns a unique key for retrieval.'''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a stored value from Redis and applies an optional transformation function.'''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a value from Redis and decodes it as a string.'''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves a value from Redis and converts it to an integer.'''
        return self.get(key, lambda x: int(x))
