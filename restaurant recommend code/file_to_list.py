def file_to_list(file):
    out = [] #itemized list as described below
    rest_filename = 'restfile.txt'
    rest_file = open(rest_filename, 'r')
    #line = rest_file.readline()
    sub_l = []
    for line in rest_file:
        if line != '\n':# this should break the loop at 'stanzas' of the file
            line = line.rstrip('\n') # removes newline from list item
            sub_l.append([line])
            #print (sub_l)
        else:
            out.append(sub_l)
            sub_l = []
			# will this atttach the cuisines appropriately -- looks like
			# this might just add comma-separated cuisines to the end, which
			# will make some lists 4-item and others 5-item
    out.append(sub_l)
    rest_file.close()
    return (out)
# this is breaking because there is no newline character at the
# very end of the file, so for the last group of lines the else
# case in the loop will never be hit. The last entry will be skipped.
			
			

			
# make restaurant file into restaurant list take each 4-line 'unit' (stanza) 
# of the file and convert it into a 4-item list: 
#
# Georgie Porgie
# 87%
# $$$
# Canadian, Pub Food
#
# should become ['Georgie Porgie', '87%', '$$$', ['Canadian', 'Pub Food']], or possibly
# [['Georgie Porgie'], ['87%'], ['$$$'], ['Canadian', 'Pub Food']]
# then use the functions in rest1.py to make the dictionaries needed for the 
# recommendation function

# then write the recommendation function
