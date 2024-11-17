import p1_random as p1
rng = p1.P1Random()

player_win = 0
dealer_win = 0
game_ties = 0
game_num = 0
in_progress = True
a = "ACE"
j = "JACK"
q = "QUEEN"
k = "KING"

while in_progress:
    #New game loop

    print(f"\nSTART GAME #{game_num + 1}")

    card = rng.next_int(13) + 1
    if card == 1:
        hand = card
        print(f"\nYour card is a {a}!")
        print(f"Your hand is: {hand}")
    elif 2<= card <= 10:
        hand = card
        print(f"\nYour card is a {card}!")
        print(f"Your hand is: {hand}")
    elif card == 11:
        hand = 10
        print(f"\nYour card is a {j}!")
        print(f"Your hand is: {hand}")
    elif card == 12:
        hand = 10
        print(f"\nYour card is a {q}!")
        print(f"Your hand is: {hand}")
    elif card == 13:
        hand = 10
        print(f"\nYour card is a {k}!")
        print(f"Your hand is: {hand}")

    while True:
        choice = input("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: ")
        if choice == "1":
            card = rng.next_int(13) + 1
            if card == 1:
                hand += 1
                print(f"Your card is a {a}!")
                print(f"Your hand is: {hand}")
            elif 2<=card<= 10:
                hand += card
                print(f"Your card is a {card}!")
                print(f"Your hand is: {hand}")
            elif card == 11:
                hand += 10
                print(f"Your card is a {j}!")
                print(f"Your hand is: {hand}")
            elif card == 12:
                hand += 10
                print(f"Your card is a {q}!")
                print(f"Your hand is: {hand}")
            elif card == 13:
                hand += 10
                print(f"Your card is a {k}!")
                print(f"Your hand is: {hand}")

            if hand == 21:
                player_win += 1
                game_num += 1
                print("BLACKJACK! You win!")
                break
            elif hand > 21:
                dealer_win += 1
                game_num += 1
                print("You exceeded 21! You lose.")
                break


        elif choice == "2":
            #dealer's draw
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {hand}")
            if dealer_hand == 21:
                dealer_win += 1
                game_num += 1
                print("Dealer wins!")
                break
            elif dealer_hand > 21:
                player_win += 1
                game_num += 1
                print("You win!")
                break
            elif hand == dealer_hand:
                print("It's a tie! No one wins!")   #check all these prints
                game_ties += 1
                game_num += 1
                break
            elif hand > dealer_hand:
                player_win += 1
                game_num += 1
                print("You win!")
                break
            elif dealer_hand > hand:
                dealer_win += 1
                game_num += 1
                print("Dealer wins!")
                break

        elif choice == "3":
            print(f"\nNumber of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {game_ties}")
            print(f"Total # of games played is: {game_num}")

            if game_num > 0:
                percentage_player_wins = (player_win / game_num) * 100
            else:
                percentage_player_wins = 0.0
            print(f"Percentage of Player wins: {percentage_player_wins:.1f}%")

        elif choice == "4":
            in_progress = False
            break
        else:
            print("Invalid input!\nPlease enter an integer value between 1 and 4.")
            continue
