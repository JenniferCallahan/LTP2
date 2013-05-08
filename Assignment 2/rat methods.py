class Rat:
    """ A rat caught in a maze. """

    # methods have self as first parameter, by convention -- this refers to 
	#the object being initialized, here a rat
	
    def __init__(self, symbol, row, col):
	""" (Rat, str, int, int) -> NoneType
	The first parameter represents the rat to be initialized, the second 
	parameter represents the 1-character symbol for the rat, the third 
	parameter represents the row where the rat is located, and the fourth 
	parameter represents the column where the rat is located.
	
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
	
	# Initialize the rat's 4 instance variables -- create a variable by this
	# name inside the object that 'self' refers to
	
	    self.symbol = symbol
	    self.row = row
	    self.col = col
	    self.num_sprouts_eaten = 0

    def set_location(self, row_loc, col_loc):
	"""(Rat, int, int) -> NoneType 
	The first parameter represents a rat, the second represents a row, 
	and the third represents a column.""" 
	
	#Set the rat's row and col instance variables to the given row 
	#and column.
	    self.row = row_loc
        self.col = col_loc


	def eat_sprout(self):
    """(Rat) -> NoneType 
	The first parameter represents a rat. Add one to the rat's instance 
	variable num_sprouts_eaten."""
	     self.num_sprouts_eaten += 1

    def __str__(self):
	"""(Rat) -> str
	The first parameter represents a rat. Return a string representation 
	of the rat, in this format:
	symbol at (row, col) ate num_sprouts_eaten sprouts.
	
	>>>rat1 = Rat('R', 1, 3)
	>>>rat1.__str__()
	'R at (1,3) ate 2 sprouts.'
	"""
	return '{0} at ({1},{2}) ate {3} sprouts.'.format(self.symbol, self.row,\
                self.col, self.num_sprouts_eaten)
    # Do not put a newline character ('\n') at the end of the string
	# how do I check this?
	
#>>> ratty = Rat('L', 1 ,3)
#>>> ratty.row
#1
#>>> ratty.symbol
#'L'
#>>> ratty.col
#3
#>>> ratty.num_sprouts_eaten
#0
#>>> ratty.eat_sprout()
#>>> ratty.num_sprouts_eaten
#1
#>>> ratty.eat_sprout()
#>>> ratty.num_sprouts_eaten
#2
#>>> ratty.set_location(2,4)
#>>> ratty.row
#2
#>>> ratty.col
#4
#>>> ratty.__str__()
#'L at (2,4) ate 2 sprouts.'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
	
	    