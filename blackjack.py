import random
print( """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

def play_blackjack():
    # Define the deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Draw initial user cards
    first_user_card = random.choice(cards)
    second_user_card = random.choice(cards)
    user_cards = [first_user_card, second_user_card]

    # Calculate initial sum of user's cards
    sum_user_card = sum(user_cards)

    # Print user's initial cards
    print(f"Your cards: {user_cards}")

    # Draw initial computer cards
    first_computer_card = random.choice(cards)
    second_computer_card = random.choice(cards)
    computer_cards = [first_computer_card, second_computer_card]

    # Calculate initial sum of computer's cards
    sum_computer_card = sum(computer_cards)

    # Dealer draws additional cards until the total is at least 17
    while sum_computer_card < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        sum_computer_card = sum(computer_cards)

    # Print one of the dealer's cards and hide the other
    print(f"Dealer's cards: {first_computer_card}, X")

    # Ask user if they want to draw another card
    choice = input("Draw another card? y or n\n")
    if choice == "y":
        third_user_card = random.choice(cards)
        user_cards.append(third_user_card)
        sum_user_card = sum(user_cards)
        print(f"Your cards: {user_cards}")
    else:
        sum_user_card = sum(user_cards)

    # Reveal dealer's cards
    print(f"Dealer's cards: {computer_cards}")

    # Determine the result of the game
    if sum_user_card == 21:
        print("You win!")
    elif sum_user_card > 21:
        print("Bust! You lose!")
    elif sum_computer_card == 21:
        print("Dealer wins!")
    elif sum_computer_card > 21:
        print("Dealer busts! You win!")
    elif sum_user_card > sum_computer_card:
        print("You win!")
    elif sum_user_card < sum_computer_card:
        print("You lose!")
    else:
        print("It's a draw!")

def main():
    while True:
        play_blackjack()
        play_again = input("Do you want to play again? y or n\n")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
