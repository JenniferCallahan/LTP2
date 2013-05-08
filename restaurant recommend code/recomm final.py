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

