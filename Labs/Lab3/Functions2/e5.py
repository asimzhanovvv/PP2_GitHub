from movies import movies

def cat_average_imdb(category):
    avrg = 0
    count = 0
    for i in range(len(movies)):
        if movies[i]["category"] == category :   
            avrg += movies[i]["imdb"]
            count += 1
    return avrg/count

print(cat_average_imdb(str(input("Choose category:  "))))