import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(1)
    1
    >>> num_buses(49)
    1
    >>> num_buses(50)
    1
    >>> num_buses(51)
    2
    """
    return math.ceil(n/50)
