import random

print(r"""
          --..,_                     _,.--.
             `'.'.                .'`__ o  `;__.
                '.'.            .'.'`  '---'`  `
                 '.`'--....--'`.'
                   `'--....--'`
""")
print("Welcome to Rattlesnake Jake")
print("You will either get rich or die trying!\n")
print("Each player gets a chance to take a golden nugget during their turn.")
print("If you survive, you can flip a coin to try to get a second turn!")
print("But be careful, Greed has been the end of many cowboys and cowgirls!\n")
def login():
    while True:
        try:
            player_count = int(input("Enter the number of players that wish to play: "))
            if player_count <= 0:
                print("The number of players must be a positive integer. Try again...")
                continue

            print("The number of players is: ", player_count)
            player_info = {}


            for i in range(1, player_count + 1):
                while True:
                    name = input(f"\nWhat is player {i}'s name? ").strip()
                    if name:
                        player_info[name] = 0
                        print(f'Welcome, {name}! You have been successfully logged in.')
                        break
                    else:
                        print("Player cannot be empty. Please enter a valid name.")

            return player_info

        except ValueError:
            print("Oops! That was not a valid number. Try again...")

def single_turn(player, player_info, extra_turn_taken):
    print(f"It's {player}'s turn.")
    input("Press enter to take your turn...")
    nugget_value = [1, 1, 1, 1, 1, 2]
    nugget = random.choice(nugget_value)

    if nugget == 1:
        player_info[player] += 1
        print(f"{player} grabbed a golden nugget!\n")

        if not extra_turn_taken[player]:
            flip_choice = input(f"{player}, do you want to flip a coin for an extra turn? (yes/no): ").lower()
            if flip_choice == 'yes':
                coin = random.choice(['heads', 'tails'])
                print(f"The coin landed on {coin}.")
                if coin == 'heads':
                    print("You get an extra turn!\n")
                    extra_turn_taken[player] = True  # Mark that the player has taken an extra turn in this round
                    return True
                else:
                    print("No extra turn for you this time.\n")
        else:
            print(f"{player}, you've already had your extra turn this round.\n")
    elif nugget == 2:
        player_info[player] = 'out'
        print(f"{player} was bitten and is out of the game!\n")

    return False

def game_round(player_info):
    extra_turn_taken = {player: False for player in player_info}  # Reset at the start of each round

    for player, score in list(player_info.items()):
        if score == 'out':
            continue

        extra_turn = single_turn(player, player_info, extra_turn_taken)
        while extra_turn:
            extra_turn = single_turn(player, player_info, extra_turn_taken)

def game_loop(player_info):
    round_number = 1

    while True:
        print(f"\nRound {round_number}")
        game_round(player_info)

        # Count players who are still in the game
        players_in_game = [player for player in player_info if player_info[player] != 'out']

        # Check if only one player remains
        if len(players_in_game) == 1:
            print(f"Game over! {players_in_game[0]} is the winner!\n")
            break
        elif len(players_in_game) == 0:
            print("All players are out of the game! No winner this time.")
            break

        # Print scores for players still in the game
        for player in players_in_game:
            print(f"{player}'s score: {player_info[player]}")

        round_number += 1
def main():
    while True:  # Start of the loop for the entire game
        player_info = login()
        game_loop(player_info)

        # Ask if the players want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        while play_again not in ["yes", "no"]:
            print("Please answer 'yes' or 'no'.")
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again == "no":
            print("Thanks for playing Rattlesnake Jake!")
            break  # Break out of the loop to end the game

if __name__ == "__main__":
    main()





















