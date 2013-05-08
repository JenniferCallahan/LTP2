def num_buses(n):
    """ (int) -> int
	
    Precondition: n >= 0
	
    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
	## in Python 3, 5/2 == 2.5 (floating point division) and 5//2 = 2 (floor
	## or integer division)#
    return math.ceil(n/50)
	
#>>> print (math.ceil(0/50))
#0
#>>> print (math.ceil(1/50))
#1
#>>> print (math.ceil(49/50))
#1
#>>> print (math.ceil(50/50))
#1
#>>> print (math.ceil(51/50))
# test ceiling, floor, round