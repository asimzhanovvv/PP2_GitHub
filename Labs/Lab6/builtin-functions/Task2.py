s = input()

upper_count = len(list(filter(str.isupper, s)))
lower_count = len(list(filter(str.islower, s)))

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")