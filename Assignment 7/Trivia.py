#Name: Hasin Shadab Rahman                                                             UID:U87513234
from trivia_questions import generate_questions
#Execute the trivia game based on a list of trivia questions.
def play_game():
    questions_list = generate_questions()

    player1_points = 0
    player2_points = 0

    for i in range(0, len(questions_list), 2):
        # Player 1's turn
        print(f"Question for the first player:\n{questions_list[i]}\n")
        player1_answer = int(input("Enter your solution (a number between 1 and 4): "))
        if player1_answer == questions_list[i].correct_answer:
            print("That is the correct answer.")
            player1_points += 1
        else:
            print(f"That is incorrect. The correct answer is {questions_list[i].correct_answer}")

        # Player 2's turn
        print(f"Question for the second player:\n{questions_list[i + 1]}\n")
        player2_answer = int(input("Enter your solution (a number between 1 and 4): "))
        if player2_answer == questions_list[i + 1].correct_answer:
            print("That is the correct answer.")
            player2_points += 1
        else:
            print(f"That is incorrect. The correct answer is {questions_list[i + 1].correct_answer}")

    print(f"\nThe first player earned {player1_points} points.")
    print(f"The second player earned {player2_points} points.")

    if player1_points > player2_points:
        print("The first player wins the game.")
    elif player1_points < player2_points:
        print("The second player wins the game.")
    else:
        print("The game is a tie.")

if __name__ == "__main__":
    play_game()


