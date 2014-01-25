"""
This file provides a simple way of retreveing data using the RottenTomatoes API
"""
import requests
import json

class RottenTomatoes ():

	apikey = "d2ruyfuf5mfj7fnvywb3meck"

	@staticmethod
	def getMoviesURL (query_terms, page_limit = 30, page = 1):
		
		search_term = RottenTomatoes.__getURLStyleQuery (query_terms)
		url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey="+RottenTomatoes.apikey+"&q="+search_term+"&page_limit="+str(page_limit)+"&page="+str(page)
		return url

	@staticmethod
	def getSimilarMoviesURL (movie_id, limit = 5):
		url = "http://api.rottentomatoes.com/api/public/v1.0/movies/"+str(movie_id)+"/similar.json?apikey="+RottenTomatoes.apikey+"&limit="+str(limit)
		return url

	@staticmethod
	def __getURLStyleQuery (query_terms):
		terms = query_terms.split( )
		search_term = ""
		search_delim = ""

		for term in terms:
			search_term = search_term+search_delim+term
			search_delim = "+"

		return search_term

	@staticmethod
	def getMoviesJSON (query_terms, page_limit = 30, page = 1):
		resp = requests.get(RottenTomatoes.getMoviesURL(query_terms, page_limit, page))
		return resp.json()

	@staticmethod
	def getMoviesText (query_terms, page_limit = 30, page = 1):
		resp = requests.get(RottenTomatoes.getMoviesURL(query_terms, page_limit, page))
		return resp.text
		
	@staticmethod
	def getSimilarMoviesJSON (movie_id, limit = 5):
		resp = requests.get(RottenTomatoes.getSimilarMoviesURL(movie_id, limit))
		return resp.json()

	@staticmethod
	def getSimilarMoviesText (movie_id, limit = 5):
		resp = requests.get(RottenTomatoes.getSimilarMoviesURL(movie_id, limit))
		return resp.text


def main():
	"""
	Example usage of the api
	"""
	my_json = RottenTomatoes.getSimilarMoviesText(movie_id = "770672122")
	parsed = json.loads(my_json)
	print json.dumps(parsed, indent=4, sort_keys=True)
	#print type(parsed)
	print type(parsed['movies'])
	print ("This is the start of movies")
	count = 1
	for value in parsed['movies']:
		print value,"\n"
		print type (value), "\n"
		print ("Movie "+str(count))
		count = count + 1
		for smaller_key,smaller_value in value.items():
			print smaller_value, "\n"
		
	#print json.dumps(parsed, indent=4, sort_keys=True)
    #print RottenTomatoes.getMoviesJSON(query_terms = "star", page = 10)
    #print "\n"
    


if  __name__ =='__main__':
    main()