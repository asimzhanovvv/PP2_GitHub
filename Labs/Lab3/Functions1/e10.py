def unique(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))            # → [1, 2, 3, 4, 5]