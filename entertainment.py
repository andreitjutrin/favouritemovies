# import required files, located in the same folder as this file
import media
import fresh_tomatoes

# creating instances of movies for media class file.
# 1st Movie name, 2nd Description of the movie, 3rd poster image, 4th url of the video

matrix = media.Movie("Matrix", 
                     "A man wakes up and discovers he is in another word", 
                     "https://uk.movieposter.com/posters/archive/main/9/A70-4902", 
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

avatar = media.Movie("Avatar",
                     "A marine on an alient plannet",
                     "http://www.impawards.com/2009/posters/avatar_ver5.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                              "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                              "https://www.youtube.com/watch?v=TQfcgaNdBCA")

fight_club = media.Movie("Fight Club", 
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more...",
                         "http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

# create a list of movives for fresh motatoes file

movies = [matrix, avatar, the_dark_knight, fight_club]
fresh_tomatoes.open_movies_page(movies)
