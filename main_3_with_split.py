from basic_deck import deck 
import random


starting_deck = deck()
print("Welcome to the Blackjack card counting app!")
num_decks = int(input("How many decks would you like to use? Enter a number between 1 and 8.\n"))
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


# Robot players will be dealt 2 cards each at the beginning of a turn. They won't hit or double down>
# Robot players are there to allow the real player to see and count more cards per turn
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
        card_index = 0
        # Only returns true if there is an ace that has not already had its value changed from 11 to 1
        if (cards[0]) == "Ace" and cards[2] == 11:
            return [True, card_index]
        card_index += 1
    return [False, 999]

def player_card_reader(p_hand, split_cards_hands):
    points = hand_points(p_hand)
    hand_number = split_cards_hands.index(p_hand) + 1
    start_string = "Your hand number " +  str(hand_number) + " is the "
    for cards in p_hand:
        start_string += cards[0] + " of " + cards[1] + " and the "
    final_string = start_string[:-9] + ". That's " + str(points) + " points." 
    print(final_string)

# printing hands when splitting
def read_multiple_hands(split_cards_hands, will_split_list, hand_points_list):
    if len(split_cards_hands) > 0:
        player_card_reader(split_cards_hands[0], split_cards_hands)
    if len(split_cards_hands) > 1:
        player_card_reader(split_cards_hands[1], split_cards_hands)
    if len(split_cards_hands) > 2:
        player_card_reader(split_cards_hands[2], split_cards_hands)
    if len(split_cards_hands) > 3:
        player_card_reader(split_cards_hands[3], split_cards_hands)

def dealer_card_reader(d_hand, add_length):
    points_showing = d_hand[0][2]
    start_string = "The dealer has the "
    start_string += d_hand[0][0] + " of " + d_hand[0][1]
    final_string = start_string + " showing. That's " + str(points_showing) + " points."
    hand_length = add_length
    if hand_length > 2:
        for i in range(1,len(d_hand)):
            points_showing += d_hand[i][2]
            start_string += " and the " + d_hand[i][0] + " of " + d_hand[i][1] 
            final_string = start_string + " showing. That's " + str(points_showing) + " points."
    print(final_string)

def double_down(p_hand, bet, player_points, split_cards_hands, multiple_hand_bets, hand_points_list):
    global count
    
    index_of_hand = split_cards_hands.index(p_hand)
    if bet * 2 > money:
        bet_question = input("You don't have enough money to double your bet. Would you like to bet all you have? Enter YES or NO.").upper()
        if bet_question == "YES":
            bet = money
        else:
            bet = bet
    else:
        bet *= 2
    multiple_hand_bets[index_of_hand] = bet
    p_hand.append(new_decks.pop())
    player_points = hand_points(p_hand)
    hand_points_list[index_of_hand] = player_points
    count += p_hand[2][3]
    player_card_reader(p_hand, split_cards_hands)
    print(get_count())
    return player_points

    # ace handling code modifies an ace's point value from 11 to 1 if the total hand value is > 21
    # and the hand contains an ace that hasn't yet had its value decreased from 11 to 1
    # removing following lines bc they arent needed
    """ace = contains_ace(p_hand)
    has_ace = ace[0]
    for i in range(2):
        if player_points > 21 and has_ace == True:
            index_of_ace = ace[1]
            p_hand[index_of_ace][2] = 1
            player_points -= 10
            ask_to_hit_again = False
        ace = contains_ace(p_hand)                    
        has_ace = ace[0]
    """
    


def hit(p_hand, player_points, will_hit, split_cards_hands, hand_points_list):
    global count
    player_index = 2
    hand_index = split_cards_hands.index(p_hand)
    while will_hit.upper() == "YES" and player_points < 21:
        ask_to_hit_again = True
        #trying to get it to append to next hand
        p_hand.append(new_decks.pop())
        player_points = hand_points(p_hand)
        count += p_hand[player_index][3]
        player_index += 1
        #hand_index += 1
        #split_cards_hands[hand_index].append(new_decks.pop())

        player_card_reader(p_hand, split_cards_hands)
        if player_points > 21:
            will_hit = "NO"
            ask_to_hit_again = False
        if player_points < 21:    
            will_hit = input("Would you like to hit? Enter YES or NO\n")
        elif player_points == 21:
            print("Congrats! You have 21. No more hitting for you.")
            will_hit = "NO"
            ask_to_hit_again = False
            print(get_count())
        elif player_points < 21 and ask_to_hit_again == True:
            player_card_reader(p_hand, split_cards_hands)
            print("For hand number " + str(hand_index + 1))
            will_hit = input("Would you like to hit? Enter YES or NO\n")
        hand_points_list[hand_index] = player_points
        #player_card_reader(p_hand, split_cards_hands)
    return player_points

def who_won(player_points, dealer_points, bet, player_name, player_blackjack, dealer_blackjack, will_surrender):
    global money
    if will_surrender == "YES":
        bet *= 0.5
        print(player_name + " surrendered and lost half of your bet. Thats " + str(int(bet)) + " dollars. Good luck next hand.\n")
        money -= bet
    elif player_points > 21:
        print(player_name + " busted and the dealer didn't." + player_name + " lost " + str(int(bet)) + " dollars.")
        money -= bet
    elif player_blackjack and not dealer_blackjack:
        print("Congratulations! You have Blackjack and the dealer doesn't. You automatically win 150% of your bet! That's " + str(int(1.5 * bet)) + " dollars!")
        money += 1.5 * bet
    elif dealer_blackjack and not player_blackjack:
        print("The dealer has Blackjack and you dont. You lost " + str(int(bet)) + " dollars. Good luck next hand.")
        money -= bet
    elif dealer_blackjack and player_blackjack:
        print("You and the dealer both got Blackjack. No money is won or lost.")
    elif dealer_points > 21:
        print("The dealer busted and you didn't. " + player_name + " won " + str(int(bet)) + " dollars!\n")
        money += bet
    elif dealer_points > player_points:
        print(player_name + " lost " + str(int(bet)) + " dollars. Good luck next hand.\n")
        money -= bet
    elif dealer_points == player_points:
        print("The dealer and " + player_name + " tied. Nobody loses or wins any money.\n")
    else:
        print(player_name + " won " + str(int(bet)) + "!\n")
        money += bet
    print("You have " + str(int(money)) + " dollars.")

# removing for loop in can_split
def can_split(hand):
    #for hand in split_cards_hands:
    if hand[0][2] == hand[1][2] and len(hand) == 2:
        return True
    return False
    
def split_cards(split_cards_hands, will_split_list, hand_points_list):
    # hand_number = 0
    global count
    #testing removing initialization of will_split
    #will_split = "NO"
    for hand in split_cards_hands:
        # adding player_card_reader
        hand_index = split_cards_hands.index(hand)
        #will_split_list.append("YES")
        #for i in range(len(split_cards_hands)):
        i = hand_index
        print(str(i))
        h_points = hand_points(split_cards_hands[i])
        hand_points_list[i] = h_points
        read_multiple_hands(split_cards_hands, will_split_list, hand_points_list)
        #trying to make it ask for previous hands
        for j in range(i+1):
            if split_cards_hands[j][0][2] == split_cards_hands[j][1][2] and len(split_cards_hands) < 4 and will_split_list[j] == "YES":
                will_split = input("You can split hand " + str(j + 1) + " would you like to?\n").upper()
                will_split_list[j] = will_split
                #print(will_split)
                if will_split_list[j] == "YES":
                    new_card_1 = new_decks.pop()
                    count += new_card_1[3]
                    split_cards_hands.append([split_cards_hands[j][1], new_card_1])
                    new_card_2 = new_decks.pop()
                    count += new_card_2[3]
                    split_cards_hands[j][1] = new_card_2
                    print(split_cards_hands[j])
                    hand_points_list[j] = hand_points(split_cards_hands[j])
        print(count)
# need to modify to handle multiple aces
def hand_points(player_hand):
    hand_points = 0
    for cards in player_hand:
        #count
        hand_points += cards[2]
        #count += cards[3]
    for cards in player_hand:
        if cards[0] == "Ace" and hand_points > 21:
            hand_points -= 10
    return hand_points
    """hand_size = len(player_hand)
    for i in range(player_hand):
        if contains_ace(player_hand)[0] and hand_points > 21:
            hand_points -= 10
            contains_ace(player_hand)[1] = 1
    return hand_points"""
#comparing original below to above
def add_hand_count(hand):
    global count
    for cards in hand:
        count += cards[3]

# Main function called for each turn of blackjack
def deal():
    global count
    global money
    dealer_hand = []
    dealer_points = 0
    player_hand = []
    player_points = 0
    player_blackjack_list = [False, False, False, False]
    hand_points_list = [0, 0, 0, 0]
    split_cards_hands = [player_hand]
    will_split_list = ["YES", "YES", "YES", "YES"]
    will_surrender_list = ["NO", "NO", "NO", "NO"]
    split_cards_points = []
    charles_hand = []
    isaac_hand = []
    bet = int(input("How much do you want to bet?\n"))
    multiple_hand_points = [bet]
    while bet > money:
        print("AM I stuck?")
        bet = int(input("You don't have that much money. How much do you want to bet?\n"))
    multiple_hand_bets = [bet, bet, bet, bet]
    # Initializing the player's hand
    # uncomment 2 lines below
    #player_hand.append(new_decks.pop())
    #player_hand.append(new_decks.pop())
    # testing split with ten value cards delete two lines below after testing
    #player_hand.append(["Queen", "Spades", 10, -1])
    #player_hand.append(["King", "Clubs", 10, -1])
    # testing split with twos
    player_hand.append(["Three", "Diamonds", 3, 1])
    player_hand.append(["Three", "Hearts", 3, 1])
    print(player_hand)
    count += player_hand[0][3]
    count += player_hand[1][3]
       # following 9 lines commented out to try and replace with hand_point function
    for hands in split_cards_hands:
        index_of_hand = split_cards_hands.index(hands)
        hand_points_list[index_of_hand] = hand_points(hands)
        #add_hand_count(hands)
    player_card_reader(player_hand, split_cards_hands)

    #print(player_hand)

    #split_cards(split_cards_hands, will_split_list, hand_points_list) 

    print(get_count())
    deal_robot_players(charles_hand, isaac_hand)
    print(get_count())
    # Initializing dealer's hand. The second card is dealt face down so it is not added
    # to the card count until it is revealed to the player
    dealer_hand.append(new_decks.pop())
    dealer_hand.append(new_decks.pop())
    dealer_points = dealer_hand[0][2] + dealer_hand[1][2]
    count += dealer_hand[0][3]
    dealer_card_reader(dealer_hand, 0)
    print(get_count())
    # Blackjack is when a player or the dealer is dealt cards adding up to 21 in their opening hand
    dealer_blackjack = False
    if player_points == 21:
        player_blackjack_list[0] = True
    if dealer_points == 21:
        dealer_blackjack = True
    if player_blackjack_list[0] != True and dealer_blackjack != True:
        will_surrender_list[0] = input("Would you like to surrender?\n").upper()
    if  player_blackjack_list[0] != True and dealer_blackjack != True and will_surrender_list[0] != "YES":
        if can_split(player_hand) == True:
            split_cards(split_cards_hands, will_split_list, hand_points_list)    
        for hands in split_cards_hands:
            index_of_hand = split_cards_hands.index(hands)
            if len(split_cards_hands) > 1:
                print("For hand number " + str(index_of_hand + 1))
                will_surrender_list[index_of_hand] = input("Would you like to surrender?\n").upper()
            if player_blackjack_list[index_of_hand] != True and will_surrender_list[index_of_hand] != "YES" and dealer_blackjack != True:
                will_hit = "NO"
                print("For hand number " + str(index_of_hand + 1))
                will_double_down = input("Would you like to double down? Enter YES or NO.\n")
                # When a player doubles down their bet is doubled and they are dealt exactly 1 more card
                if will_double_down.upper() == "YES":
                    player_points = double_down(player_hand, bet, player_points, split_cards_hands, multiple_hand_bets, hand_points_list)
                else:
                    print("For hand number " + str(index_of_hand + 1))
                    will_hit = input("Would you like to hit? Enter YES or NO\n")
                if will_hit.upper() == "YES" and hand_points_list[index_of_hand] < 21 and will_double_down.upper() != "YES":
                    player_points = hit(split_cards_hands[index_of_hand], player_points, will_hit, split_cards_hands, hand_points_list)

    print("The dealer has flipped his concealed card.")
    dealer_card_reader(dealer_hand, 3)
    count += dealer_hand[1][3]
    print(get_count())
    dealer_index = 2
    # Rules require that if the dealer has < 17 points then he must hit until the value 
    # is 17 or greater. The dealer stops hitting once they reach or exceed 17
    while dealer_points < 17 and dealer_points < 21:
        dealer_hand.append(new_decks.pop())
        dealer_points = hand_points(dealer_hand)
        #dealer_points += dealer_hand[dealer_index][2]
        count += dealer_hand[dealer_index][3]
        dealer_index += 1
        print("The dealer has less than 17 and must hit.")
        dealer_card_reader(dealer_hand, 3)
        print(get_count())
    # line below has been unindented
    for hands in split_cards_hands:
        the_hand_index = split_cards_hands.index(hands)
        print("For hand number " + str(the_hand_index + 1))
        print(hand_points_list[the_hand_index])
        print(dealer_points)
        who_won(hand_points_list[the_hand_index], dealer_points, multiple_hand_bets[the_hand_index], "You", player_blackjack_list[the_hand_index], dealer_blackjack, will_surrender_list[the_hand_index])
    print("The count is " + str(count) + ".\n")
    new_hand = input("Would you like to play another hand? Enter YES or NO \n")
    if new_hand.upper() == "YES":
        deal()
    else:
        print("It has been nice playing with you!")
        exit

deal()