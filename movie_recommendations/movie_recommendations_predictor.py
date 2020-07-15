#!/usr/bin/python
#*********************************************************************#
# Date     : 15th July 2020
# Author   : Pavan Karthik 
# Function : Project to identify the user movie recommendations based 
#			 on their previous ratings
#*********************************************************************#

import datetime
from user_database import *

start_time = datetime.datetime.now()

#Populate the list of users
list_of_users = []
for keys in UserMovieRatings:
	list_of_users.append(keys)
#print(list_of_users)	

#Initializing a dictionary which has the min dist, movie recommendation list and recommended 
#user for all the users 
predictor_dict ={}	
for j in list_of_users:
	predictor_dict[j] = {"recommended_user": '', "dist":0, "recommended_list": []}
#print(predictor_dict)
		
	
#Populate the list of movies per user:
list_of_movies = [[]]* len(list_of_users)
for idx,i in enumerate(list_of_users):
	#print(idx,i)
	list_of_movies[idx] = []
	for keys in UserMovieRatings[i]:
		list_of_movies[idx].append(keys)
	#print(list_of_movies[idx])		


#Code to obtain the recommendation list
for idx,i in enumerate(list_of_users):
	#print(idx,i)
	min_dist = 0
	list_of_min_dist = []
	#print(list_of_movies)
	#print(type(list_of_movies))
	for sub_idx,j in enumerate(list_of_users):
		if idx == sub_idx:
			continue			
		temp_min_dist = 0
		for movie_name in list_of_movies[idx]:
			if movie_name in list_of_movies[sub_idx]:
				temp_min_dist = temp_min_dist + abs(UserMovieRatings[i][movie_name] - UserMovieRatings[j][movie_name])
				#print(temp_min_dist)
			else:
				continue
		if (predictor_dict[str(i)]["dist"] == 0) or (predictor_dict[str(i)]["dist"] > temp_min_dist):
			predictor_dict[str(i)]["dist"] = temp_min_dist
			predictor_dict[str(i)]["recommended_user"] = j

#print(predictor_dict)

print('"""""""""""Recommended movies""""""""""""')

#Update the recommended list based on the minimum distance :
for idx,user in enumerate(list_of_users):
	recommended_user = predictor_dict[str(user)]["recommended_user"]
	recommended_user_index = list_of_users.index(recommended_user)
	recommendation_list = []
	for j in list_of_movies[recommended_user_index]:
		if j == user:
			continue
		if j not in list_of_movies[idx]:
			new_movie_recommended =  (j, UserMovieRatings[recommended_user][j] )
			recommendation_list.append(new_movie_recommended)
	predictor_dict[str(user)]["recommended_list"] = recommendation_list
	print("{} : ".format(user), end = '')
	print(predictor_dict[str(user)]["recommended_list"])	
	
end_time = datetime.datetime.now()	

delta = end_time - start_time
#print(delta)
#print("Time taken in micro-seconds:")
#print(int(delta.total_seconds() * 1000000)) # microsseconds