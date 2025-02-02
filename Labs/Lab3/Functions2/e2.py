from movies import movies

def great_movies(rate=5.5):
    great_list = []
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            great_list.append(movies[i]["name"])
    return great_list

print(great_movies())