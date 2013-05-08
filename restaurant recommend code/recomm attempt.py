def recommend(cost, food_type):
    cost_dict = {'$$': ['Mexican Grill'], '$$$$': [],'$': ['Queen St. Cafe', 'Dumplings R Us'], '$$$': ['Georgie Porgie']}
	#rating_dict = name_rating(data)
    cuisine_dict ={'Queen St. Cafe': 'Malaysian, Thai', 'Mexican Grill': 'Mexican', 'Georgie Porgie': 'Canadian, Pub Food','Dumplings R Us': 'Chinese'}
    venues = []
    venues2 = []
    for k in cost_dict:
        if k == cost:
            print ('key in cost_dict ==', cost_dict[k])
            venues.append(cost_dict[k])
            print ('venues lists ==', venues)
    for item in venues:
        print('item in venues is ==', item)
        print('venues[0] is==', venues[0])
        print('venues[0][0] is ==', venues[0][0])
        for k in cuisine_dict:
            print ('k in cuisine dict is ==', k)
            if k == item:
                if food_type in cuisine_dict[k]:
                    venues2.append(k)
    return venues2

print(recommend('$$', 'Mexican'))

## returns
# key in cost_dict == ['Mexican Grill']
# venues lists == [['Mexican Grill']]
# item in venues is == ['Mexican Grill']
# venues[0] is== ['Mexican Grill']
# venues[0][0] is == Mexican Grill
# k in cuisine dict is == Mexican Grill
# k in cuisine dict is == Queen St. Cafe
# k in cuisine dict is == Dumplings R Us
# k in cuisine dict is == Georgie Porgie
# []

## why doesn't k == item at line 18 above?? 
## note that the values of cost_dict are lists, whereas the keys of 
## cuisine_dict are strings -- I think this is the source of the problem, 
## but why is this happening -- I am looking at items in lists that make 
## up cost_dict, which shoudl be strings
---------------------------
# VERSION 2 -- WORKS, but doesn't do rating or return error message


def recommend(cost, food_type):
    cost_dict = {'$$': ['Mexican Grill'], '$$$$': [],'$': ['Queen St. Cafe', 'Dumplings R Us'], '$$$': ['Georgie Porgie']}
	#rating_dict = name_rating(data)
    cuisine_dict ={'Queen St. Cafe': 'Malaysian, Thai', 'Mexican Grill': 'Mexican', 'Georgie Porgie': 'Canadian, Pub Food','Dumplings R Us': 'Chinese'}
    venues = []
    venues2 = []
    for k in cost_dict:
        if k == cost:
            #print ('key in cost_dict ==', cost_dict[k])
            venues.append(cost_dict[k])
            #print ('venues lists ==', venues)
    for item in venues:
        #print('item in venues is ==', item)
        #print('venues[0] is==', venues[0])
        #print('venues[0][0] is ==', venues[0][0])
        for k in cuisine_dict:
            print ('k in cuisine dict is ==', k)
            if k == item[0]:
			# note that the change is here -- it's item[0] now instead of item
                if food_type in cuisine_dict[k]:
                    venues2.append(k)
    return venues2

print(recommend('$$', 'Mexican'))


#key in cost_dict == ['Mexican Grill']
#venues lists == [['Mexican Grill']]
#item in venues is == ['Mexican Grill']
#venues[0] is== ['Mexican Grill']
#venues[0][0] is == Mexican Grill
#k in cuisine dict is == Mexican Grill
#k in cuisine dict is == Dumplings R Us
#k in cuisine dict is == Georgie Porgie
#k in cuisine dict is == Queen St. Cafe
#['Mexican Grill']
_____________________________________
#VERSION 3
def recommend(cost, food_type):
    cost_dict = {'$$': ['Mexican Grill'], '$$$$': [],'$': ['Queen St. Cafe', 'Dumplings R Us'], '$$$': ['Georgie Porgie']}
    rating_dict = {'87': 'Georgie Porgie', '85': 'Mexican Grill', '82': 'Queen St. Cafe', '71': 'Dumplings R Us'}
    cuisine_dict ={'Queen St. Cafe': 'Malaysian, Thai, Chinese', 'Mexican Grill': 'Mexican', 'Georgie Porgie': 'Canadian, Pub Food','Dumplings R Us': 'Chinese'}
    # added chinese to QSC so that there were 2 $ Chinese places
    venues_at_cost = []
    venues_with_cuisine = []
    for k in cost_dict:
        if k == cost:
            venues_at_cost.append(cost_dict[k])
    for item in venues_at_cost:
        for k in cuisine_dict:
            if k in item:
                if food_type in cuisine_dict[k]:
                    venues_with_cuisine.append(k)
    if len(venues_at_cost) == 0: 
        return 'Sorry, no matches in the price range'
    else: 
        if len(venues_with_cuisine) == 0: 
            return 'Sorry, no matches for cuisine at that price'
        else:
            return venues_with_cuisine

