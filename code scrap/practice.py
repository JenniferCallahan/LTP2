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
            name_rat_dict[item[0]] = item[1]
    return name_rat_dict

## returns
{## 'Queen St. Cafe': '82%',
 ## 'Mexican Grill': '85%', 'Georgie Porgie': '87%', 'Dumplings R Us': '71%'}

def recommend(file, cost, food_type):
    lst = file_to_list(file)
    cost_dict = name_cost(data)
    rating_dict = name_rating(data)
    cuisine_dict = name_cuisine(data)
    venues = []
    venues2 = []
    for k in cost_dict:
        if k == cost:
            venues.append(cost_dict[k])
    for k in cuisine_dict:
            if k in venues: 
		    if cuisine_dict[k] == food_type:
			    venues2.append(k)
	return venues2
