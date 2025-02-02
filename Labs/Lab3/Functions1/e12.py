def histogram(list):
    for i in list:
        for j in range(i):
            print("*", end="")
        print()




histogram([4, 9, 7]) # **** ********* *******
histogram([1, 2, 3, 4, 5]) # * ** *** **** *****