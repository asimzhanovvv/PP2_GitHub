import random

def random_number(name):
 
    print (f"Well, {name}, I am thinking of a number between 1 and 20.")
    rnum = random.randint(1, 21)
    guess = 0
    count = 0

    while guess != rnum:
        count += 1
        guess = int(input("Take a guess. "))

        if guess < rnum:
            print ("Your guess is too low.") 

        else:
            print("Your guess is too high.")
    else:
        print(f"Good job, KBTU! You guessed my number in {count} guesses!")

random_number(str(input("Hello! What is your name? ")))