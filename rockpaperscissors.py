import random

player_score = 0
CPU_score = 0

choice_list = ["Rock", "Paper", "Scissors"]

while True:
    random_index = random.randint(0, 2)
    CPU_choice = choice_list[random_index]

    if CPU_choice == "R":
        CPU_choice = "Rock"
    elif CPU_choice == "P":
        CPU_choice = "Paper"
    elif CPU_choice == "S":
        CPU_choice = "Scissors"

    # Player input
    player_choice = input(
        "Enter a choice; R for Rock, P for Paper, or S for Scissors: \n").upper()

    if player_choice == "R":
        player_choice = "Rock"
    elif player_choice == "P":
        player_choice = "Paper"
    elif player_choice == "S":
        player_choice = "Scissors"

    # Checking if user input is valid
    while player_choice not in choice_list:
        player_choice = input(
            "That is not a valid choice. Please try again: \n").upper()

    print(f"CPU : {CPU_choice}, Player : {player_choice}\n")

#

    # Logic for  Tie
    while player_choice == CPU_choice:
        print("It's a tie!\n")
        player_choice = input("Please choose again: \n").upper()

        # Change user choice from abbr. to full word
        if player_choice == "R":
            player_choice = "Rock"
        elif player_choice == "P":
            player_choice = "Paper"
        elif player_choice == "S":
            player_choice = "Scissors"

        while player_choice not in choice_list:
            player_choice = input(
                "That is not a valid choice. Please try again: \n").upper()
        print(f"CPU : {CPU_choice}, Player : {player_choice}\n")
        break
    if player_choice == "Rock":
        if CPU_choice == "Scissors":
            print("You win, You are good at this!\n")
            player_score += 1
        else:
            print("You lose! Try again :(\n")
            CPU_score += 1
    elif player_choice == "Paper":
        if CPU_choice == "Rock":
            print("You win, You are good at this!\n")
            player_score += 1
        else:
            print("You lose! Try again :(\n")
            CPU_score += 1
    elif player_choice == "Scissors":
        if CPU_choice == "Paper":
            print("You win, You are good at this!\n")
            player_score += 1
        else:
            print("You lose! Try again :(\n")
            CPU_score += 1

    print(f"Player score is {player_score} and the CPU score is {CPU_score}\n")

    repeat_choice = input("Would you like to play again? (Y/N): \n").upper()
    while repeat_choice not in ["Y", "N"]:
        repeat_choice = input(
            "That is not a valid choice. Please try again: \n").upper()

    if repeat_choice == "N":
        break

# End of the game
print(
    f"\nFinal score is Player: {player_score} and CPU: {CPU_score}\n\nThanks for playing! See you next time!")