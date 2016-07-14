import webbrowser


class Movie:
	""" class Movie:
		Class representing a movie

	    Attributes:
	        movie_title: Title of the movie
	        movie_storyline: Short description of the movie
	        poster_image: URL of the movie poster (in jpg format)
	        trailer_youtube: URL of the trailer in Youtube
	        imdb_link (optional): URL of movie's IMDB link (default: empty string)
	        year (optional): Year of appearance (default: empty string)
	"""

	def __init__(self,
				 movie_title,
				 movie_storyline,
				 poster_image,
				 trailer_youtoube,
				 imdb_link="",
				 year=""):
		"""
		Class Constructor

		:param movie_title: Title of the movie
		:param movie_storyline: Short description of the movie
		:param poster_image: URL of the movie poster (in jpg format)
		:param trailer_youtoube: URL of the trailer in Youtube
		:param imdb_link (optional): URL of movie's IMDB link (default: empty string)
		:param year (optional): Year of appearance (default: empty string)
		"""

		self.title = movie_title
		self.story_line = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtoube
		self.imdb_link = imdb_link
		self.year = year

	def show_trailer(self):
		"""
		show_trailer(self):
		Opens the webbrowser and navigates to the trailer URL in Youtube
		"""

		webbrowser.open(self.trailer_youtube_url)



