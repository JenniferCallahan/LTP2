def get_divisors(num, possible_divisors):
    ''' (int, list of int) -> list of int

    Return a list of the values from possible_divisors
    that are divisors of num.

    >>> get_divisors(8, [1, 2, 3])
    [1, 2]
    >>> get_divisors(4, [-2, 0, 2])
    [-2, 2]
    '''

    divisors = []
    # divisors = [num] -- this will cause testing errors, Fs, which are caused
    # by incorrect assertions in the test
    for item in possible_divisors:
        if item != 0 and num % item == 0:
        # if num % item == 0: gives 0 division error -- the test will fail, but it
        # will return E (not F), because the problem is not an incorrect assertion
        # because one of the function calls (the one that divides by 0) results
        # in an error
            divisors.append(item)

    return divisors


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print('tested') -- will show that tests have been run
    # when this module is run, the tests are executed
    # if everything passes, there's no output in the shell
