class Rat:
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        Initialize the rat's 4 instance variables
         
        >>> ratty = Rat('L', 1, 3)
	>>> ratty.symbol
	'L'
	>>> ratty.row
	1
	>>> ratty.col
	3
	>>> ratty.num_sprouts_eaten
	0
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row_loc, col_loc):
        """ Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row 
	and column.

        >>> ratty = Rat('L', 1, 3)
        >>> ratty.row
        1
        >>> ratty.col
        3
        >>> ratty.set_location(2,4)
        >>> ratty.row
        2
        >>> ratty.col
        4
        """
        self.row = row_loc
        self.col = col_loc

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Add one to the rat's instance variable num_sprouts_eaten.

        >>> ratty = Rat('L', 1, 3)
        >>> ratty.num_sprouts_eaten
        0
        >>> ratty.eat_sprout()
        >>> ratty.eat_sprout()
        >>> ratty.num_sprouts_eaten
        2
        """
        self.num_sprouts_eaten += 1
        

    def __str__(self):
        """(Rat) -> str

        Return a string representation of the rat, in this format:
	symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> rat1 = Rat('R', 1, 3)
	>>> rat1.__str__()
	'R at (1,3) ate 0 sprouts.'
        """
        return '{0} at ({1},{2}) ate {3} sprouts.'.format(self.symbol, self.row,\
                self.col, self.num_sprouts_eaten)



        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
