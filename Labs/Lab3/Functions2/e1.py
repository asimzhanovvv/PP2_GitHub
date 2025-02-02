from movies import movies

def great_movie(title):
    for i in range(len(movies)):
        if movies[i]["name"] == title and movies[i]["imdb"] > 5.5:
            return True


print(movies[0])
print(great_movie(str(input("Enter the movie title:  "))))