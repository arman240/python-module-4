import random
random_number = random.randint(1, 10)
guessed_correctly = False

while not guessed_correctly:
    user_guess = int(input("Guess the number (between 1 and 10): "))
    if user_guess < random_number:
        print("Too low. Try again.")
    elif user_guess > random_number:
        print("Too high. Try again.")
    else:
        print("Correct! You guessed the number.")
        guessed_correctly = True