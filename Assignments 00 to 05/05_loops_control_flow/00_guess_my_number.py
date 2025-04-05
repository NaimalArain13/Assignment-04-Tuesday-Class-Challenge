# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48
import random
def guess_number():
    secret_number = random.randint(0,99)
    print("Guess My Number")
    print("I am thinking of a number between 0 and 99...")
    guess = int(input("Enter a guess: "))
    print(secret_number)
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print()
        guess = int(input("Enter a new guess: "))   

    return f"Congratulation you guessed the number correctly, It is {secret_number}"
    
def main():
    print(guess_number())
main()