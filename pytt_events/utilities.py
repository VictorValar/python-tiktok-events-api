from random import randint
from enum import Enum

# Generate a random number for the event ID
def get_random_id():
    '''
    Returns a random number as a string.
    '''
    return str(randint(100000000000000000, 999999999999999999))


class HttpMethod:
    POST = 'POST'
    PUT = 'PUT'
    GET = 'GET'
    DELETE = 'DELETE'