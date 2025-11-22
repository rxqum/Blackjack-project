import random
cards = {"2 of Hearts" : 2,
         "2 of Spades" : 2,
         "2 of Diamonds": 2,
         "2 of Clubs": 2,
         "3 of Hearts" : 3,
         "3 of Spades" : 3,
         "3 of Diamonds": 3,
         "3 of Clubs": 3,
         "4 of Hearts" : 4,
         "4 of Spades" : 4,
         "4 of Diamonds": 4,
         "4 of Clubs": 4,
         "5 of Hearts" : 5,
         "5 of Spades" : 5,
         "5 of Diamonds": 5,
         "5 of Clubs": 5,
         "6 of Hearts" : 6,
         "6 of Spades" : 6,
         "6 of Diamonds": 6,
         "6 of Clubs": 6,
         "7 of Hearts" : 7,
         "7 of Spades" : 7,
         "7 of Diamonds": 7,
         "7 of Clubs": 7,
         "8 of Hearts" : 8,
         "8 of Spades" : 8,
         "8 of Diamonds": 8,
         "8 of Clubs": 8,
         "9 of Hearts" : 9,
         "9 of Spades" : 9,
         "9 of Diamonds": 9,
         "9 of Clubs": 9,
         "10 of Hearts" : 10,
         "10 of Spades" : 10,
         "10 of Diamonds": 10,
         "10 of Clubs": 10,
         "J of Hearts" : 10,
         "J of Spades" : 10,
         "J of Diamonds": 10,
         "J of Clubs": 10,
         "Q of Hearts" : 10,
         "Q of Spades" : 10,
         "Q of Diamonds": 10,
         "Q of Clubs": 10,
         "K of Hearts" : 10,
         "K of Spades" : 10,
         "K of Diamonds": 10,
         "K of Clubs": 10,
         "A of Hearts" : 11,
         "A of Spades" : 11,
         "A of Diamonds": 11,
         "A of Clubs": 11}
victory = 0
loses = 0
fairs = 0



def stat():
    print()
    print(f"Your wins: {victory}❇️")
    print(f"Your losses: {loses}⛔")
    print(f"Your fairs: {fairs}🟰")
    print()
    startgame()

def game():
    confirm = input('Press "Enter" to begin: ')
    if confirm == "":
        print("The game has begun💎")
        print()
        dealer_key = random.choice(list(cards.keys()))
        dealer_key2 = random.choice(list(cards.keys()))
        dealer_card = cards[dealer_key]
        dealer_card2 = cards[dealer_key2]
        dealer_sum = dealer_card + dealer_card2
        if dealer_sum == 22:
            dealer_sum -= 10
        print(f"Dealer's first card is {dealer_key} (value: {dealer_card})✔️")
        print("Dealer picked another card")
        print()
        player_key = random.choice(list(cards.keys()))
        player_key2 = random.choice(list(cards.keys()))
        player_card = cards[player_key]
        player_card2 = cards[player_key2]
        player_sum = player_card + player_card2
        if player_sum == 22:
            player_sum -= 10
        print(f"You got: {player_key} and {player_key2}, total: {player_sum} points🔅")
        print()
        print("1. Pick a card💎")
        print("2. Stop⛔")
        player_choice = input("Your choice: ")
        if player_choice == "1":
            player_key3 = random.choice(list(cards.keys()))
            player_card3 = cards[player_key3]
            player_sum += player_card3
            if player_sum > 21:
                print(f"You got {player_key3}, total: {player_sum} points. Bust 😭")
                pass
            else:
                print(f"You got {player_key3}, total: {player_sum} points🔅")
                print()
                print("1. To pick a card💎")
                print("2. To stop⛔")
                player_choice2 = input("Your choice: ")
                if player_choice2 == "1":
                    player_key4 = random.choice(list(cards.keys()))
                    player_card4 = cards[player_key4]
                    player_sum += player_card4
                    if player_sum > 21:
                        print(f"You got {player_key4}, total: {player_sum} points. Bust 😭")
                        pass
                    else:
                        print(f"You got {player_key4}, total: {player_sum} points🔅")
                        print()
                        print("1. To pick a card💎")
                        print("2. To stop⛔")
                        player_choice3 = input("Your choice: ")
                        if player_choice3 == "1":
                            player_key5 = random.choice(list(cards.keys()))
                            player_card5 = cards[player_key5]
                            player_sum += player_card5
                            if player_sum > 21:
                                print(f"You got {player_key5}, total: {player_sum} points. Bust 😭")
                                pass
                            else:
                                print(f"You got {player_key5}, total: {player_sum} points🔅")
                                print()
                                print("You cannot pick more cards.")

                        elif player_choice3 == "2":
                            pass
                        else:
                            print("Invalid answer")
                elif player_choice2 == "2":
                    pass
                else:
                    print("Invalid answer")
        elif player_choice == "2":
            pass
        else:
            print("Invalid answer")
        print()
        print(f"Dealer's second card is: {dealer_key2}, total: {dealer_sum} points🔅")
        if dealer_sum <= 15:
            dealer_key3 = random.choice(list(cards.keys()))
            dealer_card3 = cards[dealer_key3]
            dealer_sum += dealer_card3
            print(f"Dealer picks a card. It's {dealer_key3}, total: {dealer_sum} points🔅")
            if dealer_sum > 21:
                print(f"Dealer's card is: {dealer_key3}, total: {dealer_sum} points. Bust.")
                pass
            elif dealer_sum <= 15:
                dealer_key4 = random.choice(list(cards.keys()))
                dealer_card4 = cards[dealer_key4]
                dealer_sum += dealer_card4
                print(f"Dealer picks a card. It's {dealer_key4}, total: {dealer_sum} points🔅")
                if dealer_sum > 21:
                    print(f"Dealer's card is: {dealer_key4}, total: {dealer_sum} points🔅")
                    pass
                elif dealer_sum <= 15:
                    dealer_key5 = random.choice(list(cards.keys()))
                    dealer_card5 = cards[dealer_key5]
                    dealer_sum += dealer_card5
                    print(f"Dealer picks a card. It's {dealer_key5}, total: {dealer_sum} points🔅")
                    if dealer_sum > 21:
                        print("Bust.")
                        pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

        def check_result():
            global loses, victory, fairs
            if player_sum < dealer_sum <= 21:
                print("You lost😭")
                loses += 1
            elif dealer_sum < player_sum <= 21:
                print("You won!😀")
                victory += 1
            elif dealer_sum > 21 >= player_sum:
                print("You won!😀")
                victory += 1
            elif player_sum > 21 > dealer_sum:
                print("You lost😭")
                loses += 1
            elif dealer_sum > 21 and player_sum > 21:
                print("Fair✔️")
                fairs += 1
            elif dealer_sum == player_sum:
                print("Fair✔️")
                fairs += 1
            else:
                print("Unknow error")
                pass
            print()
        check_result()
        menu()

    else:
        menu()













def menu():
    print("Welcome to the game!💎")
    print()
    print("1. To launch blackjack🔅")
    print("2. To see your statistics📈")
    print("0. To leave⛔")
    choice = input("Pick a number: ")
    if choice == "1":
        game()
    elif choice == "2":
        stat()
    elif choice == "0":
        print("Thanks for playing!")
    else:
        menu()


def startgame():
    menu()

if __name__ == "__main__":
    startgame()