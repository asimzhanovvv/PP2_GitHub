from movies import movies

def names(movies):
    for i in movies:
        print(i["name"])

names(movies)