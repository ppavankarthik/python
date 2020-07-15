#!/usr/bin/python
#*********************************************************************#
# Date     : 15th July 2020
# Author   : Pavan Karthik 
# Function : Project to identify the user movie recommendations based 
#			 on their previous ratings
#*********************************************************************#

import datetime
from user_database import *

#Populate the list of users
def get_list_of_users(user_movie_ratings):
	list_of_users = []
	for keys in user_movie_ratings:
		list_of_users.append(keys)
	return list_of_users

#Initializing a dictionary which has the min dist, movie recommendation list and recommended 
#user for all the users 
def init_predictor_dict(list_of_users):	
	predictor_dict = {}
	for user in list_of_users:
		predictor_dict[user] = {"recommended_user": '', "dist": 0, "recommended_list": []}
	return predictor_dict
		
	
#Populate the list of movies per user:
def movies_rated_per_user(user_movie_ratings,list_of_users):
	list_of_movies = [[]]* len(list_of_users)
	for idx,user in enumerate(list_of_users):
		#print(idx,user)
		list_of_movies[idx] = []
		for keys in user_movie_ratings[user]:
			list_of_movies[idx].append(keys)
	   #print(list_of_movies[idx])		
	return list_of_movies

#Code to obtain the recommendation list
def get_nearest_user_by_calculating_manhattand(user_movie_ratings, list_of_users, list_of_movies, predictor_dict):
	for idx,user_1 in enumerate(list_of_users):
		#print(idx,user_1)
		min_dist = 0
		list_of_min_dist = []
		#print(list_of_movies)
		#print(type(list_of_movies))
		for sub_idx,user_2 in enumerate(list_of_users):
			if idx == sub_idx:
				continue			
			temp_min_dist = 0
			for movie_name in list_of_movies[idx]:
				if movie_name in list_of_movies[sub_idx]:
					temp_min_dist = temp_min_dist + abs(user_movie_ratings[user_1][movie_name] - user_movie_ratings[user_2][movie_name])
					#print(temp_min_dist)
				else:
					continue
			if (predictor_dict[str(user_1)]["dist"] == 0) or (predictor_dict[str(user_1)]["dist"] > temp_min_dist):
				predictor_dict[str(user_1)]["dist"] = temp_min_dist
				predictor_dict[str(user_1)]["recommended_user"] = user_2
	#print(predictor_dict)
	return 	predictor_dict	


#Update the recommended list based on the minimum distance :
def get_movie_recommendations(predictor_dict, user_movie_ratings, list_of_movies, list_of_users):
	for idx,user in enumerate(list_of_users):
		recommended_user = predictor_dict[str(user)]["recommended_user"]
		recommended_user_index = list_of_users.index(recommended_user)
		recommendation_list = []
		for movie in list_of_movies[recommended_user_index]:
			if movie not in list_of_movies[idx]:
				new_movie_recommended =  (movie, user_movie_ratings[recommended_user][movie] )
				recommendation_list.append(new_movie_recommended)
		predictor_dict[str(user)]["recommended_list"] = recommendation_list
		print("{} : ".format(user), end = '')
		print(predictor_dict[str(user)]["recommended_list"])	
	


def main():
	#start_time = datetime.datetime.now()
	
	list_of_users = get_list_of_users(user_movie_ratings)
	predictor_dict = init_predictor_dict(list_of_users)
	list_of_movies = movies_rated_per_user(user_movie_ratings,list_of_users)
	predictor_dict = get_nearest_user_by_calculating_manhattand(user_movie_ratings, list_of_users, list_of_movies, predictor_dict)
	get_movie_recommendations(predictor_dict, user_movie_ratings, list_of_movies, list_of_users)
	
	#end_time = datetime.datetime.now()	
	#delta = end_time - start_time
	#print(delta)
	#print("Time taken in micro-seconds:")
	#print(int(delta.total_seconds() * 1000000)) # microsseconds

if __name__ == "__main__":
	main()