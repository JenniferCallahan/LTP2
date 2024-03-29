class WordplayStr(str):
## defined as a sublass of str
## inherits all the features of str -- an object of type WordplayStr is a str,
## but with more features -- it has a method that compares first & last letters
    """A string that can report whether it has interesting properties."""

    
    def same_start_and_end(self):
        """ (WordplayStr) -> bool

        Precondition: len(self) != 0

        Return whether self starts and ends with the same letter.

        >>> s = WordplayStr('abracadabra')
        >>> s.same_start_and_end()
        True
        >>> s = WordplayStr('canoe')
        >>> s.same_start_and_end()
        False
        """

        return self[0] == self[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
