import random
secret_number = random.randint(1, 100)
guess = None
print("Welcome to the guess number game")
print("I have selected a number beteween 1 and 100. Try to guess it!")
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
else:
    print(f"Congragulations! You have guessed the correct number:{secret_number}.")        