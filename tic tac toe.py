import random

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() in ['yes', 'y']

def play_game():
    print("Welcome to classic Rock, Paper, Scissors game!")
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
    if player_choice in choices:
        Ai_choice = random.choice(choices)
        print("Ai chose:", Ai_choice)
        if player_choice == Ai_choice:
            print("draw better luck next time")
        elif (player_choice == "paper" and Ai_choice == "rock") or \
             (player_choice == "rock" and Ai_choice == "scissors") or \
             (player_choice == "scissors" and Ai_choice == "paper"):
            print("You won! Congratulations! party time ")
        else:
            print("Ai wins!Sorry for the loss")
    else:
        print("Sorry, that's not a valid choice. Please choose from Rock, Paper, or Scissors.")
    return play_again()

while play_game():
    pass