# Name: Hasin Shadab Rahman                                                                                           UID:U87513234
#This code uses comments to explain each part of the program, making it easier to understand:

# It imports the random module to generate a random number.
# It generates a random secret number between 1 and 100.
# It initializes a variable tries to keep track of the number of guesses made by the user.
# The program enters a while loop, which continues as long as tries is less than 10.
# Inside the loop, it attempts to get the user's guess as an integer and validates if it's within the valid range.
# It compares the user's guess with the secret number and provides feedback on whether it's too high or too low.
# If the user guesses correctly, it congratulates them and displays the number of tries taken, then breaks out of the loop.
# If the user uses all their tries without guessing correctly, it reveals the correct number.
# Finally, it displays the result if the user couldn't guess the correct number.




import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of tries
tries = 0

# Start the game loop
while tries < 10:
    try:
        # Get user's guess as an integer
        user_guess = int(input("Enter a number between 1 and 100 (inclusive): "))

        # Checks if the guess is within the valid range
        if 1 <= user_guess <= 100:
            tries += 1

            # Compares the user's guess with the secret number
            if user_guess == secret_number:
                # Congratulates the user and display the number of tries taken
                print(f"You guessed it right!! You got it in {tries} {'guess' if tries == 1 else 'guesses'}!")
                break
            elif user_guess < secret_number:
                print("Too low. Enter another guess.")
            else:
                print("Too high. Enter another guess.")
        if user_guess < 0:
            # Prompt the user for a valid input within the specified range
            print("Really? Enter another guess between 1 to 100.")
        elif user_guess > 100:
            print("Very funny. Enter a number between 1 and 100 (inclusive).")  

    except ValueError:
        # Handle invalid input by informing the user to enter a valid number
        print("Invalid input. Please enter a valid number.")

# Display the result if the user couldn't guess the correct number
if tries == 10:
    # Inform the user about the correct number when they run out of tries
    print(f"Sorry, the number was {secret_number}.")
