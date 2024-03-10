import random

class GuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        print("Welcome to the Guessing Game!")
        while True:
            guess = self.get_user_input()
            self.attempts += 1

            if guess == self.secret_number:
                print(f"Congratulations! You guessed the number in {self.attempts} attempts.")
                break
            elif guess < self.secret_number:
                print("Too low. Try again!")
            else:
                print("Too high. Try again!")

    def get_user_input(self):
        while True:
            try:
                guess = int(input("Enter your guess (1-100): "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = GuessingGame()
    game.play()
