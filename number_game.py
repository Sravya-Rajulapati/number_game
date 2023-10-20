import random

def main():
    print("\n welcome to number guessing game :) \n ")
    guess_number()
    guessing_game()

def guess_number():
    return random.randint(1,100)

def guessing_game():
    number = guess_number()
    while True:
        try:
            guess = int(input("guess the number between 1 to 100: "))
            if 100 < guess or guess < 1:
                print("Invalid Input. Please enter a number between 1 and 100")
            elif guess < number :
                print ("Too low! try again ")
            elif guess > number :
                print("Too high! try again")
            else:
                print(f"you have guessed the correct number {number}")
                break
        except ValueError:
            print("Invalid Input. Only numbers ae allowed.")


if __name__ == '__main__':
  main()

