###Write a function that has one parameter, a list of integers, 
###and returns the sum of those integers.
def add(items):
    return sum(items)
   
items = (1, 2, 3)
print (add(items))

###Write a function that has one parameter, a list of integers, 
###and returns the sum of the positive integers.
def add_pos(items):
    pos = []
    for item in items:
        if item % 2 == 0: 
            pos.append(item)
    return sum(pos)
   
items = (1, 2, 3,4,5,6)
print (add_pos(items))

###Write a function that has one parameter, a dictionary of {str: int}, 
###and returns the sum of the integers that appear as values.
def add(diction): 
   #return diction['one'] -- gives back 1; returns value for key
   #return 'lithium' in diction -- returns False (rather than error)
   x = list(diction.values())
   return sum(x)
    
diction = {'one':1, 'two':2, 'three':3}
print (add(diction))


###Write a function that has one parameter, a dictionary of {str: int}, 
###and returns the sum of the integers whose str keys start with a 
###lowercase vowel.
def add_lowers(diction):
    vals = []
    for key in diction: 
        if key[0] in 'aeiou':
            vals.append(diction[key])
    return sum(vals)
        
diction = {'Orange':1, 'ogre':2, 'ugly':3, 'Ant':4, 'alligator':5}
print (add_lowers(diction))
### returns 10

###Write a function that has one parameter, a file opened for reading, 
###and returns the number of characters in that file.
ani = '/Users/Jennifer/Desktop/animals.txt'
a_file = open(ani, 'r')

def num_char(file):
	cnts = []
	for line in file:
		cnts.append(len(line))
	return sum(cnts)

### in a file containing
### c a
### d o
### this program returns 7 -- c, space, a, newline,d, space, o


### Write a function that has one parameter, a file opened for reading, 
###and returns the number of characters on lines that begin with a 
###lowercase letter.

### this will reuse the function above, inside
### def low_letter(file):
###     for line in file: 
###         cnt = []
###         if line[0] in 'abcdefghijklmnopqrstuvwxyz': 
###            return len(line)
### ?? but how to get it to return this -- total number of char on such lines,
### ?? just append len(line) for each such line to cnt, and then sum
### ?? but what if the point is to return or print a count for EACH such line
### ?? as an individual output value -- maybe just print len(line) for each

>>> def low_lines(file):
    lines = []
	for line in file:
		#if line[0] in 'abcdefghijklmnopqrstuvwxyz':
		if line[0].islower():
			lines.append(len(line))
	return lines
			
>>> let = '/Users/Jennifer/Desktop/letters.txt'
>>> l_file = open(let, 'r')
returns [5,4]

### file content for above is 
#pips
#Pop
#Lows
#Dog
#gags


### other version for total count
def all_low_lines(file):
	cnts = []
	for line in file:
		#if line[0] in 'abcdefghijklmnopqrstuvwxyz':
		if line[0].islower():
			cnts.append(len(line))
	return sum(cnts)

>>> print (all_low_lines(l_file))
9
