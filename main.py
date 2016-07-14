import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
						"Toy Story is an animated movie about toys come to life.",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

shawshank = media.Movie("Shawshank Redemption",
						"Andy Dufresne is sentenced to a life in the Shawshank Prison despite being innocent.",
						"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
						"https://www.youtube.com/watch?v=6hB3S9bIaco",
						"http://www.imdb.com/title/tt0111161/",
						"1994")

happy_gilmore = media.Movie("Happy Gilmore",
							"A funny story about a hockey player who becomes a successful golf professional with an"
							" extraordinarily long drive.",
							"https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",
							"https://www.youtube.com/watch?v=aa0hSPPW1so",
							"",
							"1996")

reservoir_dogs = media.Movie("Reservoir Dogs",
							 "Quentin Tarantino's first movie: A group of gangters try to find out why their bank robbery"
							 " failed.",
							 "https://upload.wikimedia.org/wikipedia/en/7/79/Reservoir_Dogs_Game_PS2_Front_Cover.JPG",
							 "https://www.youtube.com/watch?v=vayksn4Y93A")

dark_knight = media.Movie("The Dark Knight Rises",
						  "In his fight against crime in Gotham City, Batman is challenged by criminal mastermind \"The Joker\".",
						  "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
						  "https://www.youtube.com/watch?v=EXeTwQWrcwY",
						  "http://www.imdb.com/title/tt1345836/")

pianist = media.Movie("The Pianist",
					  "The movie depicts the survival of polish pianist Wladislav Szpilman "
					  "during World War II.",
					  "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Pianist_movie.jpg",
					  "https://www.youtube.com/watch?v=CIRLLPa-j9o")


movies_list = [toy_story, shawshank, happy_gilmore, reservoir_dogs, dark_knight, pianist]

fresh_tomatoes.open_movies_page(movies_list)
