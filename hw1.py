import RottenTomatoes
import json
import time

"""
Method to retreive contents of a page and append them to the file
"""

def moviesDataToFile (query_terms, file_name, page_limit = 30, page = 1):
	my_json = RottenTomatoes.RottenTomatoes.getMoviesText(query_terms, page_limit, page)
	parsed = json.loads(my_json)

	time.sleep(1)
	f = open (file_name, "a")
	for movie in parsed['movies']:
		f.write(movie['id']+","+movie['title']+"\n")
	f.close()




def main():

	"""
	This section solves part 1.b and 1.d.1 of homework 1
	"""
	open ("movie_ID_name.txt","w").close()
	for i in range (0,10):
		moviesDataToFile (query_terms = "star", file_name = "movie_ID_name.txt", page = (i+1))

	"""
	This section solves part 1.c and 1.d.2 of homework 1
	"""
	

if  __name__ =='__main__':
    main()