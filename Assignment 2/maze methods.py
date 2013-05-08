class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
	
    def __init__(self, maze, rat1, rat2):
    """ (Maze, list of list of str, Rat, Rat) -> NoneType
	The first paramter represents the maze to be initialized, 
	the second parameter represents the contents of the maze, 
	the third parameter represents the first rat in the maze, 
	and the fourth parameter represents the second rat in the maze."""

	#Initialize this maze's four instance variables:

        self.maze = maze  
		# a maze (list of lists of str) with contents specified by the 
		# second parameter
        self.rat1 = rat1
		# the first rat in the maze, as symbol/row/col
	    self.rat2 = rat2
		# the second rat in the maze, as symbol/row/col
        self.num_sprouts_left = num_sprouts_left
		# the number of uneaten sprouts in this maze
		# this variable needs to be set equal to thew value derived below
		# but I'm not sure how to do this
			count = 0
			for i in lst:
				sprouts = i.count('@')
				count = count + sprouts
			return count


    def is_wall(self, row, col):
    """ (Maze, int, int) -> bool
	
	The first parameter represents a maze, the second represents a row, 
	and the third represents a column.Return True if and only if there 
	is a wall at the given row and column of the maze. NB: row 1 is at the 
	tops of the maze"""
	
	    k = lst[row] 
        return k[col] == '#'
		
	#since list indexing starts at 0, but the location data appears to
	# start at 1, how to compensate for this?? 

    def get_character(self, row, col):
    """ (Maze, int, int) -> str
	The first parameter represents a maze, the second represents a row, and
	the third represents a column. Return the character in the maze at the 
	given row and column. If there is a rat at that location, then its 
	character should be returned rather than HALL."""

	def move(self, rat, vert, horiz):
    """ (Maze, Rat, int, int) -> bool 
	The first parameter represents a maze, the second represents a rat, the
	third represents a vertical direction change (UP, NO_CHANGE or DOWN),
	and the fourth represents a horizontal direction change (LEFT, NO_CHANGE or RIGHT).
	Move the rat in the given direction, unless there is a wall in the way. 
	Also, check for a Brussels sprout at that location and, if present: have
	the rat eat the Brussels sprout,make that location a HALL, and decrease 
	the value that num_sprouts_left refers to by one.

    Return True if and only if there wasn't a wall in the way. """

    def __str__(self):
    """" (Maze) -> str 
	The first parameter represents a maze. Return a string representation 
	of the maze, using the format maze, rat descr string 1, rat descr 
	string 2. Do not put a newline character ('\n') at the end of the string. """"
if __name__ == '__main__':
    import doctest
    doctest.testmod()