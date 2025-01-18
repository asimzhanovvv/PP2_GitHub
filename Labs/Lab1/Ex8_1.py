# Python Strings

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("We are the so-called \"Vikings\" from the north.")
print()


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a, "\n")


print("First Letter is - ",a[0], "\n")


for x in "banana":
    print(x) 


a = "Hello, World!"
print('In "', a , '" -',len(a), "letters", "\n")


txt = "The best things in life are free!"
print(txt)
if "free" in txt:
    print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")