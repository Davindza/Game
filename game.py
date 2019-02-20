secret = 29

guess = int(input("Guess the secret number (0-40)"))

if guess == secret:
    print("Congratulations! The number is 29")
else:
    print("You're wrong, I'm sorry. The secret number is not " + str(guess))