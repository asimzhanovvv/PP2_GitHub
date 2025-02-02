from movies import movies

def category (category):
    sub_list = []
    for i in range(len(movies)):
        if movies[i]["category"] == category:
            sub_list.append(movies[i]["name"])
    return sub_list

print(category(str(input("Choose category:  "))))