def file_to_list(file):
    out = [] #itemized list as described below
    rest_filename = 'restfile.txt'
    rest_file = open(rest_filename, 'r')
    #line = rest_file.readline()
    sub_l = []
    for line in rest_file:
        if line != '\n':# this should break the loop at 'stanzas' of the file
            line = line.rstrip('\n') # removes newline from list item
            sub_l.append(line)
        else:
            out.append(sub_l)
            sub_l = []
    out.append(sub_l)
	# this adds the last element (i.e. the four-line entry for Deep Fried
	# Everything) which would otherwise be omitted because of the lack of
	# a newline character at the end.
    rest_file.close()
    return (out)
## returns
## [['Georgie Porgie', '87%', '$$$', 'Canadian, Pub Food'],
## ['Queen St. Cafe', '82%', '$', 'Malaysian, Thai'],
## ['Dumplings R Us', '71%', '$', 'Chinese'], [
## 'Mexican Grill', '85%', '$$', 'Mexican']]
## note that these are strings, not list items; I think cuisines
## will be OK like this since the list of cusines is a single string

def name_cost(file):
    name_cost_dict = {'$':[], '$$':[],'$$$':[], '$$$$':[],}
    lst = file_to_list(file)
    for key in name_cost_dict:
        for item in lst:
            if key == item[2]:
                name_cost_dict[key].append(item[0])
    return name_cost_dict

## returns
## {'$$': ['Mexican Grill'], '$$$$': [],
## '$': ['Queen St. Cafe', 'Dumplings R Us'], '$$$': ['Georgie Porgie']}

def name_cuisine(file):
    name_cuis_dict = {}
    lst = file_to_list(file)
    for item in lst:
        if not item[0] in name_cuis_dict:
            #name_cuis_dict[item[0]] = item[3].split(',')
            name_cuis_dict[item[0]] = item[3]
	    ## split returns a list of cuisines in which each cuisine is an
            ## indexable item -- alternatively, this could be looked for a la
            ## 'ab' in 'option, abacus' , which returns True
            ## note that 'mexican' in ['mexican, thai'] == False
            ## but 'mexican' in 'mexican, thai' == True
    return name_cuis_dict

## returns
## {'Queen St. Cafe': 'Malaysian, Thai',
## 'Mexican Grill': 'Mexican', 'Georgie Porgie': 'Canadian, Pub Food',
##  'Dumplings R Us': 'Chinese'}
## with alternate item[3].split(',') line, returns 
## {'Queen St. Cafe': ['Malaysian', ' Thai'], 'Mexican Grill': ['Mexican'],
## 'Georgie Porgie': ['Canadian', ' Pub Food'], 'Dumplings R Us': ['Chinese']}

def name_rating(file):
    lst = file_to_list(file)
    name_rat_dict = {}
    for item in lst:
        if not item[0] in name_rat_dict:
            name_rat_dict[item[1].strip('%')] = item[0]
			# needs a step to strip % symbols
			# if we want name then number for some reason, just reverse
			# the 1 & the 0 in the step above
    return name_rat_dict

## returns
# {'87': 'Georgie Porgie', '85': 'Mexican Grill', 
# '82': 'Queen St. Cafe', '71': 'Dumplings R Us'}
# the rating is first so that the key:value pairs can be sorted
def recommend(file, cost, food_type):
    cost_dict = name_cost(file)
    rating_dict = name_rating(file)
    cuisine_dict = name_cuisine(file)
    venues_at_cost = []
    venues_with_cuisine =[]
    venue_ratings = []
    for k in cost_dict:
        #make list of restaurants that meet cost criterion
        if k == cost:
            venues_at_cost.append(cost_dict[k])
    for entry in venues_at_cost:
        #make list of restaurants that meet cuisine criterion
        for k in cuisine_dict:
            if k in entry:
                if food_type in cuisine_dict[k]:
                    venues_with_cuisine.append(k)  
    for entry in venues_with_cuisine:
        # return qualifying restaurants, sorted by rating
		# (happens at the end)
        for k in rating_dict:
            if rating_dict[k] == entry:
                venue_ratings.append([k, rating_dict[k]])
                
    if len(venues_at_cost) == 0: 
        return 'Sorry, no matches in the price range'
    else: 
        if len(venues_with_cuisine) == 0: 
            return 'Sorry, no matches for cuisine at that price'
        else:
            return sorted(venue_ratings, reverse= True)
