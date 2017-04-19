##Import module
import random

##Helper function for the game
def deal_single_card(decks):
    random_pick = random.randint(0, len(decks)-1)
    return decks.pop(random_pick)

def hands_value(hands):
    for i in range(len(hands)-1):
        if len(hands[0]) == 1:
            if hands[i+1][-1] == "A":
                for score in deck_value["A"]:
                    hands[0].append(score + hands[0][0])
                hands[0].pop(0)
            else:
                hands[0][0] += deck_value[hands[i+1][-1]]
        else:
            if hands[i+1][-1] == "A":
                temp = set()
                for score in hands[0]:
                    for value in deck_value["A"]:
                        temp.add(score + value)
                hands[0] = list(temp)
            else:
                for k in range(len(hands[0])):
                    hands[0][k] += deck_value[hands[i+1][-1]]
    return hands[0]

def find_winner(dealer, players):
    winner_list = []
    if 21 in dealer[0]:
        winner_list.append("Dealer")
    for player in players:
        if 21 in players[player][0]:
            winner_list.append("Player " + str(player+1))
    return winner_list

def deck_shoe(number_of_deck):
    ##Define a regular deck: Spades, Hearts, Clubs, Diamonds
    deck = ["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK",\
         "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",\
         "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",\
         "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK"]

    return deck * number_of_deck
    
def game_end(dealer, players):
    winner = []

    dealer_best = 0
    for score in dealer[0]:
        if score == 21:
            dealer_best = 21
            winner.append("Dealer")
            break
        elif score < 21 and score > dealer_best:
            dealer_best = score
    
    for player in players:
        for score in players[player][0]:
            if score == 21:
                winner.append("Player " + str(player+1))
                break
            elif score < 21 and score > dealer_best:
                winner.append("Player " + str(player+1))
                break
    return winner

deck_value ={"A": (1,11), "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9,\
             "0": 10, "J": 10, "Q": 10, "K": 10}

##############################INITIALIZE GAME SETTINGS####################################
##DECKS
##Initialize the deck with eight decks in total
##Create eight decks for the game
decks8 = deck_shoe(8)

##PLAYERS
##Initialize the game by asking number of players
print()
print("-" * 30, "Initializing BlackJack", "-" * 30)
print()

while True:
    try:
        num_players = eval(input("Enter the number of players: "))
        print()
    except:
        print("*" * 30, "Please enter a valid number!!!", "*" * 30)
        print()
    else:
        if not (num_players >= 1 and num_players <= 7):
            print("*" * 30, "Players must be in between 1 - 7.", "*" * 30)
            print()
        else:
            break

##HANDS: DEALERS        
##Initialize the game by setting up the dealer
dealer = [[0]]

##HANDS: PLAYERS
##Initialize the players deck
players = {}
for i in range(num_players):
    players[i] = [[0]]

print()
print(num_players, "BlackJack Players, Let's Play!")
###########################################################################################

########################################GAME PLAY##########################################

def game_play(deck, dealer, players):

    ##First Flop
    while True:
        start_game = input("\nEnter START to start a game or EXIT to stop: ")
        print()
        
        if start_game.upper() == "START":
            ##First Deal
            for i in range(num_players):
                players[i].append(deal_single_card(decks8))
            dealer.append(deal_single_card(decks8))

            ##Second Deal
            for i in range(num_players):
                players[i].append(deal_single_card(decks8))
            dealer.append(deal_single_card(decks8))

            print("Dealer has:", dealer[1], "Hole-Card")
            hands_value(dealer)
            
            for player in players:
                first_card, second_card = players[player][1], players[player][2]
                hands_total = hands_value(players[player])
                print("Player", player + 1, "has:", first_card, second_card, "\tHands Value:", hands_total)
            print()
        
            ##First Flop Check for BlackJack
            first_flop_check = find_winner(dealer, players)

            if len(first_flop_check) == 0:
                print("No BlackJack from dealer or any player!! Moving onto individual play!!\n")

                for player in players:
                    while True:
                        print("Player " + str(player+1)+ "'s Turn")
                        print("Current Hands:", players[player][1:])
                        player_decision = input("Enter HIT to take another card from the dealer or STAND to take no more cards: ")

                        if player_decision.upper() == "STAND":
                            print("\nFINAL HANDS for" + " Player " + str(player+1) + ": " + " ".join(players[player][1:]))
                            print()
                            break
                            
                        elif player_decision.upper() == "HIT":
                            next_card = deal_single_card(decks8)
                            print("\nYour card from the dealer:", next_card)
                            players[player][0] = [0]
                            players[player].append(next_card)
                            hands_total = hands_value(players[player])
                                            
                            print("Current Hands:", players[player][1:], "\tHands Value:", hands_total)

                            checker = False
                            for total in hands_total:
                                if total < 21:
                                    checker = True
                                elif total == 21:
                                    checker = True
                                    print("WHOAAAA! BLACKJACK!!!!! SEE WHAT YOU GOT PLAYERS AND DEALERS!!!!")
                                    print()
                                    break
                                
                            if checker == False:
                                print("BUSTED: OUT OF THE GAME!!!!!!")
                                print()
                                break
                            elif checker and 21 in hands_total:
                                break
                            print()
                            
                        else:
                            print("*" * 30, "Invalid Input!!", "*" * 30)
                            print()
                            
                ##Dealer Play
                print("Turn for the Dealer!!!")
                print("Current Hands:", dealer[1:])
                while True:
                    player_decision = input("Enter HIT to take another card from the dealer or STAND to take no more cards: ")
                    if player_decision.upper() == "STAND":
                        print("\nFINAL HANDS for Dealer: " + " ".join(dealer[1:]))
                        print()
                        break
                            
                    elif player_decision.upper() == "HIT":
                        next_card = deal_single_card(decks8)
                        print("\nYour card from the shoe:", next_card)
                        dealer[0] = [0]
                        dealer.append(next_card)
                        hands_total = hands_value(dealer)
                                                        
                        print("Current Hands:", dealer[1:], "\tHands Value:", hands_total)

                        checker = False
                        for total in hands_total:
                                if total < 21:
                                        checker = True
                                elif total == 21:
                                        checker = True
                                        print("WHOAAAA! BLACKJACK FROM DEALER! PROTECT THE HOUSE!!!!!!!!")
                                        print()
                                        break
                                
                        if checker == False:
                                print("BUSTED: OUT OF THE GAME!!!!!!")
                                print()
                                break
                        elif checker and 21 in hands_total:
                                break
                        print() 
                           
                    else:
                        print("*" * 30, "Invalid Input!!", "*" * 30)
                        print()
                break
                            
            elif len(first_flop_check) > 1:
                print("*" * 40, "GAME OVER", "*" * 40)
                result_str = ", ".join(first_flop_check)
                print("**The lucky winners from the first draw are:", result_str)
                print("*" * 40, "GAME OVER", "*" * 40)
                break

            elif len(first_flop_check) == 1:
                print("*" * 40, "GAME OVER", "*" * 40)
                print("** The lucky and only winner from the first draw is:", first_flop_check[0])
                print("*" * 40, "GAME OVER", "*" * 40)
                break

        elif start_game.upper() == "EXIT":
            print( "*" * 20, "GAME TERMINATED: BYE!", "*" * 20)
            break

        else:
            print("*" * 30, "Invalid Input!!", "*" * 30)


        #resultLevel
    result = game_end(dealer, players)
    return result
        

##MAIN
print(game_play(decks8, dealer, players))
        
        
          


