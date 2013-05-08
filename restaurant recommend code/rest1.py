#create name_rating dictionary
#create name_cost dictionary
#creat name_cuisine dictionary

## all tests below use this list
## rest_lst = [['Georgie Porgie', '87%', '$$$', 'Canadian, Pub Food'],['Queen St. Cafe', '82%', '$', 'Malaysian, Thai'], ['Dumplings R Us', '71%', '$', 'Chinese'],
## ['Mexican Grill', '85%', '$$', 'Mexican'], ['Deep Fried Everything', '52%', '$','Pub Food']] 

def name_cost(lst): 
    name_cost_dict = {'$':[], '$$':[],'$$$':[], '$$$$':[],}
	for key in name_cost_dict: 
	    for item in lst: 
		    if key == item[2]: 
			    name_cost_dict[key].append(item[0])
	return name_cost_dict

## gives back {'$$': ['Mexican Grill'], '$$$': ['Georgie Porgie'], 
## '$': ['Queen St Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
## '$$$$': []}

def name_rating(lst): 
    name_rat_dict = {}
	    for item in lst: 
		    if not item[0] in name_rat_dict: 
			    name_rat_dict[item[0]] = item[1]
		return name_rat_dict
## gives back {'Queen St Cafe': '82%', 'Georgie Porgie': '87%', 
## 'Deep Fried Everything': '52%', 'Dumplings R Us': '71%', 
## 'Mexican Grill': '85%'}

def name_cuisine(lst): 
    name_cuis_dict = {}
	    for item in lst: 
		    if not item[0] in name_cuis_dict: 
			    name_cuis_dict[item[0]] = item[3].split(',')
				## split returns a list of cuisines in which each cuisine
				## is an indexable item (vs. a string containing commas
				## which can't readily bea searched unless one already
				## knows the substrings sought
		return name_cuis_dict
## gives back {'Mexican Grill': ['Mexican'], 
## 'Georgie Porgie': ['Canadian', ' Pub Food'], 
## 'Queen St Cafe': ['Malaysian', ' Thai'], 
## 'Deep Fried Everything': ['Pub Food'], 'Dumplings R Us': ['Chinese']}

