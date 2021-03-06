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
def read_miltiple_hands(split_cards_hands, will_split_list, hand_points_list):
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

def double_down(p_hand, bet, hand_points_list, split_cards_hands):
    global count
    hand_index = split_cards_hands.index(p_hand)
    if bet * 2 > money:
        bet_question = input("You don't have enough money to double your bet. Would you like to bet all you have? Enter YES or NO.").upper()
        if bet_question == "YES":
            bet = money
        else:
            bet = bet
    else:
        bet *= 2
    p_hand.append(new_decks.pop())
    hand_points_list[hand_index] = hand_points(p_hand)
    #player_points += p_hand[2][2]
    print(p_hand)
    count += p_hand[2][3]

    # ace handling code modifies an ace's point value from 11 to 1 if the total hand value is > 21
    # and the hand contains an ace that hasn't yet had its value decreased from 11 to 1
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
    player_card_reader(p_hand, split_cards_hands)"""
    print(get_count())
    #return player_points


#trying to redefine using hand_points(player_hand)
def hit_2(p_hand, split_cards_hands, will_hit, hand_points_list):
    global count
    player_index = 2
    player_hand_index = split_cards_hands.index(p_hand)
    print("For hand number " + str(player_index -1) + " ")
    player_hand_points = hand_points(p_hand)
    player_card_reader(p_hand, split_cards_hands)
    while will_hit.upper() == "YES" and player_hand_points < 21:
        ask_to_hit_again = True
        p_hand.append(new_decks.pop())
        #player_hand_points += p_hand[player_index][2]
        count += p_hand[player_index][3]
        player_index += 1
        ace = contains_ace(p_hand)
        has_ace = ace[0]
        player_hand_points = hand_points(p_hand)
        #player_card_reader(p_hand, split_cards_hands)
        if (player_hand_points > 21 and has_ace == False) or player_hand_points > 31 :
            will_hit = "NO"
            ask_to_hit_again = False
        elif player_hand_points > 21 and has_ace == True:
            """index_of_ace = ace[1]
            p_hand[index_of_ace][2] = 1
            player_hand_points -= 10
            ask_to_hit_again = False
            """
            ask_to_hit_again = True
            player_hand_points = hand_points(p_hand)
            print(get_count())
        #elif player_hand_points < 21:    
        #    will_hit = input("Would you like to hit? Enter YES or NO\n")
        elif player_hand_points == 21:
            print("Congrats! You have 21. No more hitting for you.")
            will_hit = "NO"
            ask_to_hit_again = False
            print(get_count())
        elif player_hand_points < 21 and ask_to_hit_again == True:
                will_hit = input("Would you like to hit? Enter YES or NO\n")
        hand_points_list[player_hand_index] = hand_points(p_hand)
        player_card_reader(p_hand, split_cards_hands)
        return player_hand_points
"""def hit(p_hand, player_points, will_hit, split_cards_hands):
    global count
    player_index = 2
    print("For hand number " + str(player_index -1) + " ")
    while will_hit.upper() == "YES" and player_points < 21:
        ask_to_hit_again = True
        p_hand.append(new_decks.pop())
        player_points += p_hand[player_index][2]
        count += p_hand[player_index][3]
        player_index += 1
        ace = contains_ace(p_hand)
        has_ace = ace[0]
        player_card_reader(p_hand, split_cards_hands)
        if (player_points > 21 and has_ace == False) or player_points > 31 :
            will_hit = "NO"
            ask_to_hit_again = False
        elif player_points > 21 and has_ace == True:
            index_of_ace = ace[1]
            p_hand[index_of_ace][2] = 1
            player_points -= 10
            ask_to_hit_again = False
            print(get_count())
        if player_points < 21:    
            will_hit = input("Would you like to hit? Enter YES or NO\n")
        elif player_points == 21:
            print("Congrats! You have 21. No more hitting for you.")
            will_hit = "NO"
            ask_to_hit_again = False
            print(get_count())
        elif player_points < 21 and ask_to_hit_again == True:
                will_hit = input("Would you like to hit? Enter YES or NO\n")
        return player_points
"""
def who_won(player_points, dealer_points, bet, player_name, player_blackjack, dealer_blackjack, will_surrender):
    global money
    print(player_points)
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

def can_split(split_cards_hands):
    for hand in split_cards_hands:
        if hand[0][2] == hand[1][2] and len(hand) == 2:
            return True
    return False
    
def split_cards(split_cards_hands, will_split_list, hand_points_list):
    # hand_number = 0
    global count
    #testing removing initialization of will_split
    #will_split = "NO"
    print("test1")
    for hand in split_cards_hands:
        print("test2")
        # adding player_card_reader
        hand_index = split_cards_hands.index(hand)
        #will_split_list.append("YES")
        #for i in range(len(split_cards_hands)):
        i = hand_index
        print(str(i))
        h_points = hand_points(split_cards_hands[i])
        hand_points_list[i] = h_points
        read_miltiple_hands(split_cards_hands, will_split_list, hand_points_list)
        #trying to make it ask for previous hands
        for j in range(i + 1):
            
            if j < 4 and split_cards_hands[j][0][2] == split_cards_hands[j][1][2] and len(split_cards_hands) < 4 and will_split_list[j] == "YES":
                will_split = input("You can split hand " + str(j + 1) + " would you like to?\n").upper()
                will_split_list[j] = will_split
                #print(will_split)
                if will_split_list[j] == "YES":
                    new_card_1 = new_decks.pop()
                    count += new_card_1[3]
                    split_cards_hands[j].append([split_cards_hands[j][1], new_card_1])
                    new_card_2 = new_decks.pop()
                    count += new_card_2[3]
                    split_cards_hands[j][1] = new_card_2
                    print(split_cards_hands[j])
                    hand_points_list[j] = hand_points(split_cards_hands[j])
            #read_miltiple_hands(split_cards_hands, will_split_list, hand_points_list)
        print(count)

def hand_points(player_hand):
    hand_points = 0
    for cards in player_hand:
        #count
        hand_points += cards[2]
        #count += cards[3]
    if contains_ace(player_hand)[0] and hand_points > 21:
        hand_points -= 10
        contains_ace(player_hand)[1] = 1
    return hand_points
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
    hand_points_list = [0, 0, 0, 0]
    split_cards_hands = [player_hand]
    will_split_list = ["YES", "YES", "YES", "YES"]
    split_cards_points = []
    charles_hand = []
    isaac_hand = []
    bet = int(input("How much do you want to bet?\n"))
    multiple_hand_points = [bet]
    while bet > money:
        bet = int(input("You don't have that much money. How much do you want to bet?\n"))
    
    # Initializing the player's hand
    # uncomment 2 lines below
    #player_hand.append(new_decks.pop())
    #player_hand.append(new_decks.pop())
    # testing split delete two lines below after testing
    player_hand.append(["Queen", "Spades", 10, -1])
    player_hand.append(["King", "Clubs", 10, -1])
    count += player_hand[0][3]
    count += player_hand[1][3]
    hand_points_list[0] = hand_points(split_cards_hands[0])
    player_card_reader(player_hand, split_cards_hands)
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
    #commenting block below out 
    """player_blackjack = False
    dealer_blackjack = False
    will_surrender = "NO"
    if player_points == 21:
        player_blackjack = True
    if dealer_points == 21:
        dealer_blackjack = True
    if player_blackjack != True and dealer_blackjack != True:
        will_surrender = input("Would you like to surrender?\n").upper()
    if will_surrender != "YES":
        split_cards(split_cards_hands, will_split_list, hand_points_list)
    """
    this_index = 0
    # block below is commented out to test using for loop w/ numbers
    """for hands in split_cards_hands:
        player_blackjack = False
        dealer_blackjack = False
        will_surrender = "NO"
        this_index += 1
        if player_points == 21:
            player_blackjack = True
        if dealer_points == 21:
            dealer_blackjack = True
        if player_blackjack != True and dealer_blackjack != True:
            will_surrender = input("Would you like to surrender?\n").upper()
        
        hand_points_list[this_index - 1] = hand_points(hands)
        #trying to replace [this_index -1] with [this_index]
        if hand_points_list[this_index] < 21 and will_surrender != "YES" and dealer_blackjack != True:
            will_hit = "NO"
            print("For hand number " + str(this_index) + " ")
            will_double_down = input("would you like to double down? Enter YES or NO.\n")
            # When a player doubles down their bet is doubled and they are dealt exactly 1 more card
            if will_double_down.upper() == "YES":
                #player_points = 
                double_down(player_hand, bet, hand_points_list, split_cards_hands)
            elif hand_points_list[this_index - 1] < 21:
                print("For hand number " + str(this_index) + " ")
                will_hit = input("would you like to hit? Enter YES or NO\n")
            if will_hit.upper() == "YES" and hand_points_list[this_index - 1] < 21 and will_double_down.upper() != "YES":
                #testing hit_2
                #player_points = hit(player_hand, hand_points_list[this_index], will_hit, split_cards_hands)
                hand_points_list[this_index - 1] = hit_2(hands, split_cards_hands, will_hit, hand_points_list)
                print(hand_points_list[this_index - 1])
        player_card_reader(hands, split_cards_hands)
        """
    player_blackjack = False
    dealer_blackjack = False
    will_surrender = "NO"
    """
    if dealer_points == 21:
        dealer_blackjack == True
    if hand_points_list[0] == 21:
        player_blackjack = True
    if player_blackjack != True and dealer_blackjack != True:
        will_surrender = input("Would you like to surrender?\n").upper()
    if will_surrender != "YES":
        split_cards(split_cards_hands, will_split_list, hand_points_list)
    """
    if player_blackjack != True and dealer_blackjack != True and will_surrender != "YES":  
        for i in range(4):
            if len(split_cards_hands) > i and len(split_cards_hands[i]) > 1:
                player_blackjack = False
                dealer_blackjack = False
                will_double_down = "NO"
                will_hit = "NO"
                #will_surrender = "NO"
                if dealer_points == 21:
                    dealer_blackjack == True
                if hand_points_list[i] == 21:
                    player_blackjack = True
                if len(split_cards_hands) == 1 and player_blackjack != True and dealer_blackjack != True and will_surrender != "YES":
                    print("For hand number " + str(i + 1))
                    will_surrender = input("Would you like to surrender?\n").upper()
                if will_surrender != "YES":
                    split_cards(split_cards_hands, will_split_list, hand_points_list)
                if len(split_cards_hands) > 1 and hand_points_list[i] == 21:
                    print("For hand number " + str(i + 1))
                    will_surrender = input("Would you like to surrender?\n").upper()
                if hand_points_list[i] < 21 and will_surrender != "YES" and dealer_blackjack != True:
                    will_hit = "NO"
                    print("For hand number " + str(i + 1) + " ")
                    will_double_down = input("would you like to double down? Enter YES or NO.\n")
                # When a player doubles down their bet is doubled and they are dealt exactly 1 more card
                if will_double_down.upper() == "YES":
                    #player_points = 
                    double_down(player_hand, bet, hand_points_list, split_cards_hands)
                elif hand_points_list[i] < 21 and will_surrender != "YES":
                    print("For hand number " + str(i + 1) + " ")
                    will_hit = input("would you like to hit? Enter YES or NO\n")
                if will_hit.upper() == "YES" and hand_points_list[i] < 21 and will_double_down.upper() != "YES":
                    #testing hit_2
                    #player_points = hit(player_hand, hand_points_list[this_index], will_hit, split_cards_hands)
                    hand_points_list[this_index - 1] = hit_2(hands, split_cards_hands, will_hit, hand_points_list)
                    print(hand_points_list[this_index - 1])
            #player_card_reader(split_cards_hands[i], split_cards_hands)


    # Everything below stays the same
    print("The dealer has flipped his concealed card.")
    dealer_card_reader(dealer_hand, 3)
    count += dealer_hand[1][3]
    print(get_count())
    dealer_index = 2
    # Rules require that if the dealer has < 17 points then he must hit until the value 
    # is 17 or greater. The dealer stops hitting once they reach or exceed 17
    while dealer_points < 17 and dealer_points < 21:
        dealer_hand.append(new_decks.pop())
        dealer_points += dealer_hand[dealer_index][2]
        count += dealer_hand[dealer_index][3]
        dealer_index += 1
        print("The dealer has less than 17 and must hit.")
        dealer_card_reader(dealer_hand, 3)
        print(get_count())
    # line below has been unindented
    index_of_current_hand = 0
    for hands in split_cards_hands:
        if len(hands) > 1:
            index_of_current_hand += 1
            p_points = hand_points_list[index_of_current_hand - 1]
            print("For your hand number " + str(index_of_current_hand) + ":")
            who_won(p_points, dealer_points, bet, "You", player_blackjack, dealer_blackjack, will_surrender)
    print("The count is " + str(count) + ".\n")
    new_hand = input("Would you like to play another hand? Enter YES or NO \n")
    if new_hand.upper() == "YES":
        deal()
    else:
        print("It has been nice playing with you!")
        exit

deal()

