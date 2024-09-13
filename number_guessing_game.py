import random

def number_guessing_game():
    number = random.randint(1, 10)

    player_name = input("Hello! What's your name? ")
    number_of_guesses = 0
    print("==welcome==🤗😄🙏 to the Number guessing game.")

    print(f"Welcome, {player_name}! I'm thinking of a number between 1 and 10. You have 5 tries to guess it.")

    while number_of_guesses < 5:
        try:
            guess = int(input(f"Try {number_of_guesses + 1}: "))
            number_of_guesses += 1
            print(f"Debug: Number is {number}, Guess is {guess}")  # Keep this for debugging purposes

            if guess < number:
                print("Your guess is too low. Try a higher number.")
            elif guess > number:
                print("Your guess is too high. Try a lower number.")
            else:
                print(f"Congratulations🎉👏, {player_name}! You guessed the number in {number_of_guesses} tries!")
                break
        except ValueError:
            print("Please enter a valid number.")

    # Check if the guess was correct within the loop
    if number_of_guesses >= 5 and guess != number:
        print(f"Sorry, {player_name}. The number was {number}. Better luck next time!")

number_guessing_game()
