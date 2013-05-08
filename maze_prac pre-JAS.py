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
        """ (Rat, int, int) -> NoneType

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
#######################
class Maze:
    def __init__(self, maze, rat1, rat2):
        """
        (Maze, list of list of str, Rat, Rat) -> NoneType
        
        Initialize this maze's four instance variables

        ##unit tests are being super uncooperative here
        """
        self.maze = maze
        self.rat1 = rat1
        self.rat2 = rat2
        def get_num_sprouts(maze):
            """(list of list of str) -> int
            Counts the instances of '@' in a given maze.
            """
            count = 0
            for i in maze:
                sprouts = i.count('@')
                count = count + sprouts
            return count
        self.num_sprouts_left = get_num_sprouts(maze)

    

    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool

        Return True iff there is a wall at the given row and column
        of the maze. NB: row 1 is at the top

        >>> mz = [['#','#','#','#',',#','#','#'],\
             ['#','.','.','.','.','.','#'],\
             ['#','.','#','#','#','.','#'],\
             ['#','.','.','@','#','.','#'],\
             ['#','@','#','.','@','.','#'],\
             ['#','#','#','#','#','#','#']]

        >>> mazy = Maze(mz, Rat('J', 1, 1), Rat('P', 1, 4))
        >>> mazy.is_wall(2, 2)
        True
        """
        k = self.maze[row] 
        return k[col] == '#'
    # note that list indexing starts at 0, whereas positioning numbers start
    # at 1 -- however, it's also the case that the rat cannot occupy the outermost
    # rows or the outermost columns, since these are walls -- anyhow, how to deal
    # with this issue?? Do the walls cancel it??


    def get_character(self, row, col):
        """
        (Maze, int, int) -> str

        Return the character in the maze at the given row and column.
        If there is a rat at that location, then its character should be returned
        rather than HALL.

        >>> mz = [['#','#','#','#',',#','#','#'],\
             ['#','.','.','.','.','.','#'],\
             ['#','.','#','#','#','.','#'],\
             ['#','.','.','@','#','.','#'],\
             ['#','@','#','.','@','.','#'],\
             ['#','#','#','#','#','#','#']]
        >>> mazy = Maze(mz, Rat('J', 1, 1), Rat('P', 1, 4))
        >>> mazy.get_character(1,2)
        '.'
        """
        k = self.maze[row]
        i = k[col]
        return i
##        if self.row == row and self.col == col:
##            return self.symbol
##        else:
##            k = self.maze[row]
##            i = k[col]
##            return i
    ##need to modify tests for if/else
    ##>>> mazy.get_character(1,1)
    ##'J'

        # this needs to return the rat symbol (i.e., letter) if the rat's
        # on that square -- how to make sure it does that?? Maybe if/else loop
        # that first checks whether rat's(row, col) location is the same as the
        # character's & if so returns the symbol, else returns the char ?
        # But how to get this data (e.g., self.row) from Rat, when we're in Maze??


    #def move(self, rat, vert_change, horiz_change):
        """
        (Maze, Rat, int, int) -> bool

        The first parameter represents a maze, the second represents a rat,
        the third represents a vertical direction change (UP, NO_CHANGE or DOWN),
        and the fourth represents a horizontal direction change (LEFT, NO_CHANGE or RIGHT).

        Move the rat in the given direction, unless there is a wall in the way.
        Also, check for a Brussels sprout at that location and, if present: (1)
        have the rat eat the Brussels sprout, (2) make that location a HALL, and
        (3)decrease the value that num_sprouts_left refers to by one.

        Return True if and only if there wasn't a wall in the way.
        """


    ##def __str__():        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
