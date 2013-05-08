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

print (recommend('$', 'Chinese'))