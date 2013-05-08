import palindrome_v1
#importing here prevents duplication of reverse function
#if there's an error/change in reverse, then it only has to be
#dealt with in one location

def is_palindrome_v2(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """

    # The number of chars in s.
    n = len(s)

    # Compare the first half of s to the reverse of the second half.
    # Omit the middle character of an odd-length string.
    return s[:n // 2] == palindrome_v1.reverse(s[n - n // 2:])
        ## notice how the line above calls the reverse function
        ## from version 1, imported at the start of this file
        ## it's filename.functionname(arguments)

        ## note also that nothing here prints anything or asks for input --
        ## that's all coming from palindrome_v1

        ## to stop that code from running, we need to alter the code in
        ## palindrome_v1 -- this is the reason for the if statement at the end
        ## of palindrome_v1; it ensures that that part of the code is only
        ## deployed when plaindrome_v1 is __main__, NOT when it is imported
