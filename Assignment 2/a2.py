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
        
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row_loc, col_loc):
        
        self.row = row_loc
        self.col = col_loc

    def eat_sprout(self):
        
        self.num_sprouts_eaten += 1
        

    def __str__(self):
    
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row,\
                self.col, self.num_sprouts_eaten)
#######################
class Maze:
    def __init__(self, maze, rat_1, rat_2):
       
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol
        count = 0
        for i in maze:
            sprouts = i.count(SPROUT)
            count = count + sprouts
        self.num_sprouts_left = count    

    def is_wall(self, row, col):
        
        k = self.maze[row] 
        return k[col] == WALL


    def get_character(self, row, col):

        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol
        else:
            k = self.maze[row]
            i = k[col]
            return i


    def move(self, rat, vert_change, horiz_change):
        
        new_row = rat.row + vert_change
        new_col = rat.col + horiz_change
        character = self.get_character(new_row, new_col)
        
        if character != WALL:
            self.maze[rat.row][rat.col] = HALL
            if character == SPROUT:
                rat.eat_sprout()
                
                self.num_sprouts_left -= 1
            self.maze[new_row][new_col] = rat.symbol
            rat.set_location(new_row, new_col)
            return True
        else:
            return False

    def __str__(self):
        
        string = ''
        for item in self.maze:
            substring = ''
            for item2 in item:
                substring += item2
            substring += '\n'
            string += substring
        string = string + self.rat_1.__str__() + '\n' + self.rat_2.__str__()
        return string
            

