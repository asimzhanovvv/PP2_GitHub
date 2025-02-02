def get_permutations(s):
    permutations = [""]
    for char in s:
        new_perms = []
        for perm in permutations:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + char + perm[i:])
        permutations = new_perms
    return permutations

# Пример использования
user_input = input("Enter a string:  ")
result = get_permutations(user_input)

print("All perutations:")
c = 1
for p in result:
    print(f"{c})  {p}")
    c += 1