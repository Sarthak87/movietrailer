import media
import fresh_tomatoes

# first instance of class Movie
justice_league = media.Movie("Justice League",
                             "A group of superheroes unite",
                             "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=r9-DM9uBtVI")

# second instance of class Movie
thor_ragnarok = media.Movie("Thor Ragnarok",
                            "Thor must stop Hela and ragnarok should occur",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

# third instance of class Movie
dunkirk = media.Movie("Dunkirk",
                      "Allied Forces rescue mission from the Dunkirk",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

# fourth instance of class Movie
spiderman_homecoming = media.Movie("Spiderman Homecoming",
                                   "Spiderman fights to protect the home",
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=U0D3AOldjMU")  # NOQA

# these objects stored in a list data structure named movies
movies = [justice_league, dunkirk, spiderman_homecoming, thor_ragnarok]
# open_movies_page() function takes as input list of movies()
fresh_tomatoes.open_movies_page(movies)
