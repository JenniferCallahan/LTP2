def swap_k(L, k):
    """ (list) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
	start_list = L[:k]
    end_list = L[len(L)-k:]
    L[len(L)-k:] = []
    L[:k] = []
    for item in start_list:
        L.append(item)
    end_list.reverse()
	# this allows the code below to insert 5,6 rather than 6,5
    for item in end_list:
        L.insert(0,item)
		# insert (index, value to be inserted)
    # return L -- note that description does not specify a return value --
	# the point here is list mutation and comparison of pre & post mutated
	# lists in the test
    
	