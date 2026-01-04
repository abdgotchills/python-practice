import random, sys
print("Welcome To Rock, Paper, Scissors")

player_victory = 0
computer_victory = 0
while True:

    user_choice = input("Enter any key to play [Enter Q to Quit]: ")
    if user_choice == "Q" or user_choice == "q":
        sys.exit()
    else:
        print("Enter Choice: (R)ock, (P)aper, (S)cissors")
        break
while True:
    print("Player: " + str(player_victory) + " Computer: " + str(computer_victory))
    player_move = input("Enter Choice: ")
    if player_move == 'r' or player_move == "R":
        print("Player Choice: Rock \nvs.")
    elif player_move == "p" or player_move == "P":
        print("Player Choice: Paper \nvs.")
    elif player_move == "s" or player_move == "S":
        print("Player Choice: Scissors \nvs.")
    else:
        print("You must enter R,P or S")
        continuea

    move_number = random.randint(1,3)
    if move_number == 1:
        print("Computer Choice: Rock")
    elif move_number == 2:
        print("Computer Choice: Paper")
    elif move_number == 3:
        print("Computer Choice: Scissors")

    if player_move == move_number:
        print("IT'S A TIE")
    elif (player_move == "R" or player_move == "r") and move_number == 2:
        print("Computer Wins")
        computer_victory += 1
    elif (player_move == "R" or player_move == "r") and move_number == 3:
        print("Player Wins")
        player_victory += 1
    elif (player_move == "S" or player_move == "s") and move_number == 1:
        print("Computer Wins")
        computer_victory += 1
    elif (player_move == "S" or player_move == "s") and move_number == 2:
        print("Player Wins")
        player_victory += 1
    elif (player_move == "P" or player_move == "p") and move_number == 1:
        print("Player Wins")
        player_victory += 1
    elif (player_move == "P" or player_move == "p") and move_number == 3:
        print("Computer Wins")
        computer_victory += 1




