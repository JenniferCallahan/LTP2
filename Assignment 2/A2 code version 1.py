# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


  

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
        count = 0
        for i in maze:
            sprouts = i.count(SPROUT)
            count = count + sprouts
        self.num_sprouts_left = count    

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
        return k[col] == WALL


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
        >>> mazy.get_character(1,1)
        'J'
        """

        if self.rat1.row == row and self.rat1.col == col:
            return self.rat1.symbol
        elif self.rat2.row == row and self.rat2.col == col:
            return self.rat2.symbol
        else:
            k = self.maze[row]
            i = k[col]
            return i


    def move(self, rat, vert_change, horiz_change):
        """
        (Maze, Rat, int, int) -> bool

        Return True if and only if there wasn't a wall in the way.
        >>> mz = [['#','#','#','#',',#','#','#'],\
             ['#','.','.','.','.','.','#'],\
             ['#','.','#','#','#','.','#'],\
             ['#','.','.','@','#','.','#'],\
             ['#','@','#','.','@','.','#'],\
             ['#','#','#','#','#','#','#']]
        >>> mazy = Maze(mz, Rat('J', 1, 1), Rat('P', 3, 1))
        >>> mazy.move(mazy.rat1, 0, -1)
        False
        >>> mazy.move(mazy.rat2, 1, 0)
        True
        """
        new_row = rat.row + vert_change
        new_col = rat.col + horiz_change
        character = self.get_character(new_row, new_col)
        if character != WALL:
            if character == SPROUT:
                rat.eat_sprout()
                self.maze[new_row][new_col] = HALL
                self.num_sprouts_left -= 1
            rat.set_location(new_row, new_col)
            return True
        else:
            return False

    def __str__(self):
        """

        """
        string = ''
        for item in self.maze:
            substring = ''
            for item2 in item:
                substring += item2
            substring += '\n'
            string += substring
        string = string + self.rat1.__str__() + '\n' + self.rat2.__str__()
        return string
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
