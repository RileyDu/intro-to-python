current_movies = {
    "Inception": "10:00am",
    "Interstellar": "11:00am",
    "The Dark Knight": "12:00pm",
    "Super 8": "1:00pm",
}

print("We're showing the following movies:")
for movie in current_movies:
    print(movie)

chosen_movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(chosen_movie)

if showtime == None:
    print("We don't have that movie")
else:
    print("Showtime is", showtime, "for the movie", chosen_movie)