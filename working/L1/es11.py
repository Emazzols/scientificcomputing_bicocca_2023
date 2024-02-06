import random

# List of tools (rock, paper, scissors)
tools = ["rock", "paper", "scissors"]

# Initialize counters for wins and spares
pc_wins = 0
spares = 0
user_wins = 0

# Initialize the variable to control the game loop
going_on = "y"

# Main game loop
while going_on == "y":
    # User chooses rock, paper, or scissors
    user_choice = input("Choose: rock, paper, or scissors (other inputs will make the PC win)?\n")

    # PC randomly chooses one from the list
    pc_choice = random.choice(tools)
    print(pc_choice)

    # Check the result of the game
    if user_choice == pc_choice:
        # If choices are the same, it's a spare
        print("Spare!")
        spares += 1
    elif (
        (user_choice == "rock" and pc_choice == "scissors") or
        (user_choice == "paper" and pc_choice == "rock") or
        (user_choice == "scissors" and pc_choice == "paper")
    ):
        # User wins under specific conditions
        print("You win!")
        user_wins += 1
    else:
        # PC wins if none of the above conditions are met
        print("PC win!")
        pc_wins += 1

    # Ask if the user wants to continue playing
    going_on = input("If you don't want to play anymore, type 'q'. To keep playing, type 'y'\n")
    
    # If 'q' is entered, exit the loop
    if going_on == "q":
        break

# Print the final results
print("PC won", pc_wins, "times!")
print("You won", user_wins, "times!")
print("There were", spares, "spares!")
