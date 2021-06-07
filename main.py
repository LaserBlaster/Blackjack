from basic_deck import deck 
import random
starting_deck = deck()
print("Welcome to the Blackjack card counting app!")
num_decks = int(input("How many decks would you like to use? Enter a number between 1 and 7.\n"))
new_decks = []
money = 1000
count = 0
def shuffle_decks(num_decks):
    for i in range(num_decks):
        new_decks.extend(starting_deck)
    random.shuffle(new_decks)
shuffle_decks(num_decks)
decks_left = round((num_decks * 52 - len(new_decks)) / 52)
def get_count():
    return count
def get_decks_left():
    return decks_left
def get_true_count():
    true_count = round(count / decks_left)
    return true_count
def get_player_hand():
    return player_hand
def get_dealer_hand():
    return dealer_hand
def deal_robot_players(charles_hand, isaac_hand):
    global count
    isaac_hand.append(new_decks.pop())
    isaac_hand.append(new_decks.pop())
    print("Isaac has been dealt the " + isaac_hand[0][0] + " of " + isaac_hand[0][1] + " and the " + isaac_hand[1][0] + " of " + isaac_hand[1][1] + "." )
    charles_hand.append(new_decks.pop())
    charles_hand.append(new_decks.pop())
    print("Charles has been dealt the " + charles_hand[0][0] + " of " + charles_hand[0][1] + " and the " + charles_hand[1][0] + " of " + charles_hand[1][1] + "." )
    count += isaac_hand[0][3] + isaac_hand[1][3] + charles_hand[0][3] + charles_hand[1][3]
def contains_ace(lst):
    for cards in lst:
        count = 0
        if (cards[0]) == "Ace" and cards[2] == 11:
            return [True, count]
        count += 1
    return [False, 99]
def player_card_reader(p_hand, points):
    points = points 
    start_string = "You've been dealt: the "
    for cards in p_hand:
        start_string += cards[0] + " of " + cards[1] + " and the "
    if points > 21 and contains_ace(p_hand)[0]:
        points -= 10
    final_string = start_string[:-9] + ". That's " + str(points) + " points." 
    print(final_string)
def dealer_card_reader(d_hand, starting_index):
    points_showing = 0
    start_string = "The dealer has: the "
    for i in range(starting_index, len(d_hand)):
        start_string += d_hand[i][0] + " of " + d_hand[i][1] + " and the "
        points_showing += d_hand[i][2]
    final_string = start_string[:-9] + " showing. That's " + str(points_showing) + " points."
    print(final_string)
def dealer_card_reader_2(d_hand):
    points_showing = d_hand[0][2]
    start_string = "The dealer has the "
    start_string += d_hand[0][0] + " of " + d_hand[0][1] + " and the "
    final_string = start_string[:-9] + " showing. That's " + str(points_showing) + " points."
    #print(final_string)
    #final_string = start_string + d_hand[0][0] + " of " + d_hand[0][1] + " and the "
    if len(d_hand) > 2:
        for i in range(1,len(d_hand)):
            points_showing += d_hand[i][2]
            start_string += " and the " + d_hand[i][0] + " of " + d_hand[i][1] + " and the "
            final_string = start_string[:-9] + " showing. That's " + str(points_showing) + " points."
            print(final_string)
    else:
        print(final_string)
def who_won(player_points, dealer_points, bet, player_name, player_blackjack, dealer_blackjack):
    global money
    if player_points > 21:
        print(player_name + " busted. " + player_name + " lost " + str(bet) + " dollars.")
        money -= bet
    elif player_blackjack and not dealer_blackjack:
        money += 1.5 * bet
    elif dealer_points > 21:
        print("The dealer busted and you didn't. " + player_name + " won " + str(bet) + " dollars!\n")
        money += bet
    elif dealer_points > player_points:
        print(player_name + " lost " + str(bet) + " dollars. Good luck next hand.\n")
        money -= bet
    elif dealer_points == player_points:
        print("The dealer and " + player_name + " tied. Nobody loses or wins any money.\n")
    else:
        print(player_name + " won " + str(bet) + "!\n")
        money += bet
    print("You have " + str(money) + " dollars.")
def deal():
    global count
    global money
    dealer_hand = []
    dealer_points = 0
    player_hand = []
    player_points = 0
    charles_hand = []
    isaac_hand = []
    bet = int(input("How much do you want to bet?\n"))
    # Initializing the player's hand
    player_hand.append(new_decks.pop())
    player_hand.append(new_decks.pop())
    
    for cards in player_hand:
        count
        player_points += cards[2]
        count += cards[3]
    player_card_reader(player_hand, player_points)
    print(str(count))
    print(get_count())
    #print(player_hand)
    #print(player_points)
    #print(count)
    deal_robot_players(charles_hand, isaac_hand)
    print(str(count))
    #dealer_hand.append(new_decks[0])
    #dealer_hand.append(new_decks.pop())
    #dealer_points = dealer_hand[0][2] + dealer_hand[1][2]
    #count += dealer_hand[1][3]
    dealer_hand.append(new_decks.pop())
    dealer_hand.append(new_decks[0])
    dealer_points = dealer_hand[0][2] + dealer_hand[1][2]
    count += dealer_hand[0][3]
    print(str(count))
    #print(dealer_hand[1])
    #print(dealer_points)
    #print(count)
    dealer_card_reader_2(dealer_hand)
    print(str(count))
    player_blackjack = False
    dealer_blackjack = False
    if player_points == 21 and dealer_points != 21:
        print("Congratulations! You have Blackjack and automatically win 150% of your bet! That's " + str(1.5 * bet) + " dollars!")
        player_blackjack = True
        dealer_hand[0] = new_decks.pop(0)
        count += dealer_hand[0][3]
        print(dealer_hand)
    elif player_points != 21 and dealer_points == 21:
        print("The dealer has Blackjack and you dont. You lost " + str(bet) + " dollars. Good luck next hand.")
        dealer_blackjack = True
        dealer_hand[0] = new_decks.pop(0)
        count += dealer_hand[0][3]
        player_points = -1
    elif player_points < 21 and dealer_points != 21:
        hit = "NO"
        double_down = input("Would you like to double down? Enter YES or NO.\n")
        if double_down == "YES":
            bet *= 2
            player_hand.append(new_decks.pop())
            player_points += player_hand[2][2]
            count += player_hand[2][3]
            print(player_hand)
            player_card_reader(player_hand, player_points)
            print(str(count))
        else:
            hit = input("Would you like to hit? Enter YES or NO\n")
            player_index = 2
            while hit == "YES" and player_points < 21 and double_down != "YES":
                ask_to_hit_again = True
                player_hand.append(new_decks.pop())
                player_points += player_hand[player_index][2]
                count += player_hand[player_index][3]
                player_index += 1
                ace = contains_ace(player_hand)
                has_ace = ace[0]
                print(player_hand)
                player_card_reader(player_hand, player_points)
                if (player_points > 21 and has_ace == False) or player_points > 31 :
                    hit = "NO"
                    ask_to_hit_again = False
                elif player_points > 21 and has_ace == True:
                    index_of_ace = contains_ace(player_hand)[1]
                    player_hand[index_of_ace][2] = 1
                    player_points -= 10
                    ask_to_hit_again = False
                    hit = input("Would you like to hit? Enter YES or NO\n")
                elif player_points == 21:
                    print("Congrats! You have 21. No more hitting for you.")
                    hit = "NO"
                    ask_to_hit_again = False
                if player_points < 21 and ask_to_hit_again == True:
                    hit = input("Would you like to hit? Enter YES or NO\n")
                print(str(count))
        #dealer_hand[0] = new_decks.pop(0)
        dealer_hand[1] = new_decks.pop(0)
        print("The dealer has flipped his concealed card.")
        #dealer_card_reader(dealer_hand, 0)
        dealer_card_reader_2(dealer_hand)
        #count += dealer_hand[0][3]
        count += dealer_hand[1][3]
        print(str(count))
        #print(dealer_hand)
        dealer_index = 2
        while dealer_points < 17 and dealer_points < 21:
            dealer_hand.append(new_decks.pop())
            dealer_points += dealer_hand[dealer_index][2]
            count += dealer_hand[dealer_index][3]
            dealer_index += 1
        #    print(dealer_hand)
            print("The dealer has less than 17 and must hit.")
            dealer_card_reader_2(dealer_hand, 0)
            print(str(count))
        """if player_points > 21:
            print("You busted. You lost " + str(bet) + " dollars.")
            money -= bet
        elif player_blackjack and not dealer_blackjack:
            money += 1.5 * bet
        elif dealer_points > 21:
            print("The dealer busted. You won " + str(bet) + " dollars!\n")
        elif dealer_points > player_points:
            print("You lost " + str(bet) + " dollars. Good luck next hand.\n")
            money -= bet
        elif dealer_points == player_points:
            print("We tied. Nobody loses or wins any money.\n")
        """
        who_won(player_points, dealer_points, bet, "You", player_blackjack, dealer_blackjack)
    #print(player_hand)
    #print(player_points)
    print("The count is " + str(count) + ".\n")
    new_hand = input("Would you like to play another hand? Enter YES or NO \n")
    if new_hand == "YES":
        deal()
    else:
        print("It has been nice playing with you!")
        exit



deal()
