import random

def guess_the_number():
    upperlimit = int(input("Number between 1 and: "))
    number = random.randint(1, upperlimit)
    attempts = 0
    print(f"Guess the number between 1 and {upperlimit}")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number: 
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()