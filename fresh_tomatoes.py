import webbrowser
import os
import re
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_str(template, **params):
    # helper function which renders html from a template using jinja2

    t = jinja_env.get_template(template)
    return t.render(params)


def create_movie_tiles_content(movies):
    """
    Creates HTML content which will be placed into body of main HTML page

    :param movies: List of Movie objects
    :return: Raw HTML content to be built into main HTML page
    """

    # The HTML content for this section of the page

    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        content += render_str("movie_tile_content.html",
                              movie_title=movie.title,
                              poster_image_url=movie.poster_image_url,
                              trailer_youtube_id=trailer_youtube_id,
                              movie_story_line=movie.story_line,
                              imdb_link=movie.imdb_link,
                              year=movie.year)

    return content


def open_movies_page(movies):
    """
    open_movies_page(movies)
    Creates a movies gallery in html format from a list of Movie objects.
    The web browser is opened immediately and it navigates to the
    created local html file

    :param movies: list of Movie objects
    """

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # build HTML content from template
    # movie_tiles is not escaped!
    rendered_content = render_str("main_page.html",
                                  movie_tiles=create_movie_tiles_content(movies))  # noqa

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
