def file_to_list(file):
    out = []
    rest_filename = 'restfile.txt'
    rest_file = open(rest_filename, 'r')
    sub_l = []
    for line in rest_file:
        if line != '\n':
            line = line.rstrip('\n')
            sub_l.append([line])
        else:
            out.append(sub_l)
            sub_l = []
    
    rest_file.close()
    return (out)

def name_cost(lst): 
    name_cost_dict = {'$':[], '$$':[],'$$$':[], '$$$$':[],}
	for key in name_cost_dict: 
	    for item in lst: 
		    if key == item[2]: 
			    name_cost_dict[key].append(item[0])
	return name_cost_dict
	
	
def name_rating(lst): 
    name_rat_dict = {}
	    for item in lst: 
		    if not item[0] in name_rat_dict: 
			    name_rat_dict[item[0]] = item[1]
	return name_rat_dict
		
def name_cuisine(lst): 
    name_cuis_dict = {}
	    for item in lst: 
		    if not item[0] in name_cuis_dict: 
			    name_cuis_dict[item[0]] = item[3].split(',')
	return name_cuis_dict
	
	
def recommend(file, cost, food_type):
	data = file_to_list(file)
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
	
## still needs ratings
## need to choose a return message if nothing matches the inputs