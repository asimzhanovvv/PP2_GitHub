def reverse_string(s):
    norm_words = s.split()
    norm_words.reverse()
    for word in norm_words:
        print(word, end=" ")
    
reverse_string("We are redy")               # → "redy are We"