from movies import movies

def average_imdb ():
    avrg = 0
    count = 0
    for i in range(len(movies)):
       avrg += movies[i]["imdb"]
       count += 1
    return avrg/count

print(average_imdb(str(input("Choose category:  "))))