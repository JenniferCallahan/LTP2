def remove_shared(L1, L2):
    """ (list list)
    Remove items from L1 that are in both L1 and L2.

    >>> list_1 = [1, 2, 3, 4, 6]
    >>> list_2 = [2, 4, 5, 7]
    >>> remove_shared(list_1, list_2)
    >>> list_1
    [1, 3, 6]
    >>> list_2
    [2, 4, 5, 7]
    """
    ## here, no spaces in expected output was enough to make the doctest fail
    ## e.g., [1,3,6] vs. [1, 3, 6]
    ## the unittest did not fail for unspaced lists
    for v in L2:
        if v in L1:
            L1.remove(v)
            # no return statement -- produces 'None'; no useful return value to
            # examine in test; instead we examine list_1 and list_2 -- make sure
            # that list_1 has been mutated properly and that list_2 has NOT been
            # mutated

if __name__ == '__main__':
    import doctest
    doctest.testmod()
