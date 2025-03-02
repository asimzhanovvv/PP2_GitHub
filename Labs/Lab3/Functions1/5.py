# def word_permutations(sentence):
#     words = list(sentence.split())

#     if len(words) == 1:
#         return [sentence]
    
#     result = []
#     for i in range(len(words)):
#         for j in range(len(words)):
#             if i != j:
#                 words[i], words[j] = words[j], words[i]
#                 if words not in result : result.append(" ".join(words))
#                 words[i], words[j] = words[j], words[i]
    
#     return result

# # Input
# user_input = input("Enter a sentence: ")

# resultt = word_permutations(user_input)

# cc = 1
# for res in resultt:
#     print(cc, res)
#     cc += 1