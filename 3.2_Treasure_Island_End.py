print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

def game_over(message="Game Over."):
    print(message)
    exit()

def play_treasure_game():
    choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

    if choice1 == "left":
        choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()

            if choice3 == "red":
                game_over("It's a room full of fire.")
            elif choice3 == "yellow":
                print("You found the treasure! You Win!")
            elif choice3 == "blue":
                game_over("You enter a room of beasts.")
            else:
                game_over("You chose a door that doesn't exist.")
        else:
            game_over("You get attacked by an angry trout.")
    else:
        game_over("You fell into a hole.")

# Start the game
play_treasure_game()
