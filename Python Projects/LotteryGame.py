import random

def lottery_game():
    print("Welcome to the Python Lottery Winning Game!")

    # Define the rules and instructions
    print("Instructions: You will pick 6 numbers between 1 and 49.")
    print("If your numbers match the winning numbers, you win the lottery!")

    # Generate the winning numbers
    winning_numbers = random.sample(range(1, 50), 6)
    print("Winning numbers:", winning_numbers)

    # Prompt the player to select their numbers
    player_numbers = []
    for _ in range(6):
        while True:
            try:
                number = int(input(f"Enter a number ({len(player_numbers) + 1}/6): "))
                if 1 <= number <= 49 and number not in player_numbers:
                    player_numbers.append(number)
                    break
                else:
                    print("Please enter a valid number between 1 and 49, which you haven't already picked.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Announce the player's numbers
    print("Your numbers:", player_numbers)

    # Check for winning
    matching_numbers = set(winning_numbers).intersection(player_numbers)

    if len(matching_numbers) == 6:
        print("Congratulations! You've won the jackpot!")
    elif len(matching_numbers) >= 3:
        print(f"You've matched {len(matching_numbers)} numbers. You win a prize!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    lottery_game()
