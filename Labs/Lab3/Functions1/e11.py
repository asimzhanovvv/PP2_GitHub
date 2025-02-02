def is_polindrome(s):
    return s == s[::-1]

print(is_polindrome("madam"))                # → True
print(is_polindrome("hello"))                # → False
print(is_polindrome("hello olleh"))          # → True