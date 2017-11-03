import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_story, poster_url, trailer_url):
        # Initialize movie related information
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        # Open movie trailer url link on a web browser
        webbrowser.open(self.trailer_youtube_url)

