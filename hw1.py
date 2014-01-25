import RottenTomatoes
import json
import time

"""
Method to retreive contents of a page and append them to the file
"""

def moviesDataToFile (query_terms, file_name, movie_id_list, page_limit = 30, page = 1):
	my_json = RottenTomatoes.RottenTomatoes.getMoviesText(query_terms, page_limit, page)
	parsed = json.loads(my_json)

	time.sleep(0.2)
	f = open (file_name, "a")
	for movie in parsed['movies']:
		f.write(movie['id']+","+movie['title']+"\n")
		movie_id_list.append(movie['id'])
	f.close()

def getSimilarMovies (movie_id, limit = 5):
	my_json = RottenTomatoes.RottenTomatoes.getSimilarMoviesText(movie_id = movie_id, limit = limit)
	parsed = json.loads(my_json)
	similar_movies_list = []
	time.sleep(0.2)
	for value in parsed['movies']:
		similar_movies_list.append(value['id'])
	return similar_movies_list

def removeDuplicates (similar_movies_dict):
	for key in similar_movies_dict:
		similar_movies_list = similar_movies_dict.get(key)
		for movie in similar_movies_list:
			if similar_movies_dict.get(movie, None) != None :
				movie_temp = similar_movies_dict.get(movie)
				if key in movie_temp:
					similar_movies_dict.get(movie).remove(key)

def writeDictToFile (similar_movies_dict, file_name):
	f = open (file_name, "w")
	for key in similar_movies_dict:
		similar_movies_list = similar_movies_dict.get(key)
		for movie in similar_movies_list:
			f.write(key+","+movie+"\n")
	f.close()


def main():

	"""
	This section solves part 1.b and 1.d.1 of homework 1
	"""
	movie_id_list = []
	open ("movie_ID_name.txt","w").close()
	for i in range (0,10):
		moviesDataToFile (query_terms = "star", file_name = "movie_ID_name.txt", movie_id_list = movie_id_list, page = (i+1))

	"""
	This section solves part 1.c and 1.d.2 of homework 1
	"""
	similar_movies_dict = {}
	for movie in movie_id_list:
		similar_movies_dict[movie] = getSimilarMovies (movie_id = movie)

	removeDuplicates (similar_movies_dict = similar_movies_dict)
	writeDictToFile (similar_movies_dict = similar_movies_dict, file_name = "movie_ID_sim_movie_ID.txt")
	

if  __name__ =='__main__':
    main()