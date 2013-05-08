def add_greeting(L=[]):
    """ (list) -> NoneType

    Append 'hello' to L and print L.

    >>> L = ['hi', 'bonjour']
    >>> f(L)
    >>> L
    ['hi', 'bonjour', 'hello']
    """

    L.append('hello')
    print(L)
	
	# note that each time this is called, L has changed --
	# the first call prints hello, the second prints hello hello, etc.

    
