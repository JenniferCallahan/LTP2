def is_palindrome_v1(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """

    return reverse(s) == s


def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''

    # For each character in s, add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev

    return rev
print ('In version 1, the module name is ', __name__)

if __name__ == '__main__':
## this if statement keeps the code that follows it from being run
## unless this program is actually main program -- it blocks code from
## being run when this module is imported
    word = input('Enter a word: ')
    if is_palindrome_v1(word):
        print(word, 'is a palindrome.')
    else:
        print(word, 'is not a palindrome.')
