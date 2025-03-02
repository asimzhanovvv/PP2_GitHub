str = input()
rev = "".join(reversed(str))
if str == rev:
    print("Yes")
else:
    print("No")