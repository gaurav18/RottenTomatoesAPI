"""
This file provides a simple way of retreveing data using the RottenTomatoes API
"""
import requests

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
	def getSimilarMoviesJSON (movie_id, limit = 5):
		resp = requests.get(RottenTomatoes.getSimilarMoviesURL(movie_id, limit))
		return resp.json()


def main():
    print RottenTomatoes.getMoviesJSON(query_terms = "star", page = 10)
    print "\n"
    print RottenTomatoes.getSimilarMoviesJSON(movie_id = "770672122")


if  __name__ =='__main__':
    main()