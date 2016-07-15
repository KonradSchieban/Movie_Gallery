Movie Gallery (v1.0)

Movie_Gallery is a Python project which creates a movie gallery in HTML format.

<h1> 1. Content: </h1>

Movie_Gallery<br />
|-- main.py<br />
|-- fresh_tomatoes.py<br />
|-- media.py<br />
|-- Readme.txt<br />
|-- templates/<br />
?ts=4    |-- main_page.html<br />
?ts=4    |-- movie_tile_content.html<br />

2. Prerequisites:
    - Movie_Gallery uses Jinja2 to render dynamic HTML content. To install Jinja2 and make it available to Python
      open a terminal and type
        > pip install Jinja2

3. Run the programm:
    Open a terminal, navigate in the folder Movie_Gallery and type
        > python main.py

4. How to change the list of displayed movies:
    Open the file main.py with an editor. A couple of movie objects are created in the main() function. Additional
    movie objects can be created with the syntax

    movie_obj = media.Movie("A title",
							"some description",
							"link_to_poster.jpg",
							"link_to_youtube_trailer",
							"link_to_imdb_site",
							"year_of_appearence")

	Example:
	shawshank = media.Movie("Shawshank Redemption",
							"Andy Dufresne is sentenced to a life in the Shawshank Prison despite being innocent.",
							"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
							"https://www.youtube.com/watch?v=6hB3S9bIaco",
							"http://www.imdb.com/title/tt0111161/",
							"1994")

	Note, that the IMDB link and year of appearance are optional parameters and are only displayed if explicitly
	defined.

	After creation of the object, the object need to be added to the list "movies_list".