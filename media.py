# import required libraries.
import webbrowser

# This class will be used to list details of my favourite movies. I will use this class to define
# instances like matrix, avatar. 

class Movie():
        # All Classes need to be started with __init__. Each of my movies will have thesse instances.
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

        # This instance method will open a brower. 
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
