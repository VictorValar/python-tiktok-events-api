from random import randint

# Generate a random number for the event ID
def get_random_id():
    '''
    Returns a random number as a string.
    '''
    return str(randint(100000000000000000, 999999999999999999))
