import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    random_num = random.randint(1, 20)
    ges = 0
    while True:
        print("Take a guess.")
        g = int(input())
        ges += 1
        if g < random_num:
            print("Your guess is too low.")
        elif g > random_num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {ges} guesses!")
            break

guess_the_number()
