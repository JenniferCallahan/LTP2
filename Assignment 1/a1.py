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


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([-0.01, -0.12, -0.15])
    (0, -0.28)
    >>> stock_price_summary([0.02, 0.56, 0.43])
    (1.01, 0)
    >>> stock_price_summary([-0.01, 0.99])
    (0.99, -0.01)
    """
    loss_list = []
    gain_list = []
    for item in price_changes:
        if item < 0:
            loss_list.append(item)
        else:
            gain_list.append(item)
    losses = sum(loss_list)
    gains = sum(gain_list)
    return (gains, losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2 -- k is between 0 and half the length
	of the list

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    start_list = L[:k]
    end_list = L[-k:]
    L[-k:] = []
    L[:k] = []
    for item in start_list:
        L.append(item)
    end_list.reverse()
	# this allows the code below to insert 5,6 rather than 6,5
	# omitting this line would produce a good failing version
    for item in end_list:
        L.insert(0,item)
	# insert (index, value to be inserted)
    # return L -- note that description does not specify a return value --
	# the point here is list mutation and comparison of pre & post mutated
	# lists in the test


if __name__ == '__main__':
    import doctest
    doctest.testmod()
