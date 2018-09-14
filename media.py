import webbrowser


class Movie():
    """
    This is a class which stores movies, including movie title, box art URL and a YouTube link.
                                                      
    Attributes:
        movie_title (str): It stores the title of the movie.
        movie_storyline (str): It stores the storyline of the movie.
        poster_image (str): It stores the box art URL of the movie.
        trailer_youtube (str): It stores the YouTube link to the movie trailer.
    """
                                                                                
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        The constructor for Movie class.

        Parameters:
            movie_title (str): It stores the title of the movie.
            movie_storyline (str): It stores the storyline of the movie. 
            poster_image (str): It stores the box art URL of the movie.
            trailer_youtube (str): It stores the YouTube link to the movie trailer.
        """
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        The function which opens the youtube link in the webpage.
        """
        
        webbrowser.open(self.trailer_youtube_url)
