# Make blackjack game, 1-7 players, one 52 card deck.

import time
from random import randint
from enum import Enum

# Fix the maximum count for a hand before busting
MAX_CARD_COUNT = 21


# First define the deck.
deck = ["2 of hearts","3 of hearts","4 of hearts","5 of hearts","6 of hearts","7 of hearts","8 of hearts","9 of hearts","10 of hearts","Jack of hearts","Queen of hearts","King of hearts","Ace of of hearts","2 of clubs","3 of clubs","4 of clubs","5 of clubs","6 of clubs","7 of clubs","8 of clubs","9 of clubs","10 of clubs","Jack of clubs","Queen of clubs","King of clubs","Ace of clubs","2 of diamonds","3 of diamonds","4 of diamonds","5 of diamonds","6 of diamonds","7 of diamonds","8 of diamonds","9 of diamonds","10 of diamonds","Jack of diamonds","Queen of diamonds","King of diamonds","Ace of diamonds","2 of spades","3 of spades","4 of spades","5 of spades","6 of spades","7 of spades","8 of spades","9 of spades","10 of spades","Jack of spades","Queen of spades","King of spades","Ace of spades"]


# Define a counting function, takes input of a hand consisting of the above "cards" and returns the blackjack count.
def count_hand(hand):
    count = 0
    for j in range(len(hand)):
        if hand[j][:2] == "10" or hand[j][:2] == "Ja" or hand[j][:2] == "Qu" or hand[j][:2] == "Ki":
            count=count+10
        elif hand[j][:2] == "Ac":
            count=count+11
        else:
            count=count+int(hand[j][:1])
    if count > MAX_CARD_COUNT:
        if hand[0][:2] == "Ac" or hand[1][:2] == "Ac":
            count=count-10
    return count

# Define class for player, including player_id, name, game_state, hand, split hand.
class player:
    hand = []
    state = []

    @classmethod
    # Define function within class that deals a card to a hand
    def card_deal(cls, hand):
        randomcard_id = randint(0,len(deck)-1)
        hand.append(deck[randomcard_id])
        deck.remove(deck[randomcard_id]) 
    
    @classmethod
    # Define functon within class that amends state or split_state
    def state_changer(cls, player_state, new_state):
        player_state.append(new_state)
        player_state.remove(player_state[0])
        
    @classmethod
    # Define function within class that moves card from hand to split hand in case of split
    def hand_splitter(cls,hand,split_hand):
        split_hand.append(hand[1])
        hand.remove(hand[1])

    def __init__(self, player_id, name, state, split_state, hand, split_hand):
        self.player_id = player_id
        self.name = name
        self.state = state
        self.split_state = split_state
        self.hand = hand
        self.split_hand = split_hand

    
# Welcome message, input request for number of players.
print("Welcome to Blackjack.\n")
time.sleep(1)


# Only accept valid inputs (integer between 1 and 7).
while True:
    print("Input the number of players (1-7):\n")
    number_of_players = input()
    print("")
    if number_of_players in [str(1), str(2), str(3), str(4), str(5), str(6), str(7)]:
        break
    else:
        print("Number of players must be an integer between 1 and 7.\n")

time.sleep(0.5)
number_of_players = int(number_of_players)
print("Starting a %d player game.\n"% number_of_players)


# Make list to hold player objects.
players_list = []
for player_counter in range(number_of_players):
    players_list.append([])

# For loop to make a class for each player (id, name, hand, split hand), putting them in above list.
for player_counter in range(number_of_players):
    print("Player %i, what is your name?\n" % int(player_counter+1))
    name = input()
    print("")
    players_list[player_counter] = player(player_counter, name, ["in_play"], ["out_of_play"], [], [])

# Define a unique player class for the dealer
dealer = player("dealer", "dealer", ["in_play"], ["out_of_play"], [], [])

# Give everyone 2 cards.
for player_id in range(number_of_players):
    for j in range(2):

        players_list[player_id].card_deal(players_list[player_id].hand)

# Give dealer 1 card.
dealer.card_deal(dealer.hand)

# The main game loop.
# Checks if can split, offers if can.
# Should run through each player, asking hit or stand.
# If hit, checks if bust.
# If all stand or bust, dealer draws until winner is found.
for player_id in range(number_of_players):
    time.sleep(1)
    print("_________________________\n")
    time.sleep(1)
    print("%s's turn.\n" % players_list[player_id].name)
    time.sleep(1)
    print("The dealer has %s.\n" % dealer.hand)
    time.sleep(1)
    print("%s has %s.\n" % (players_list[player_id].name, players_list[player_id].hand))
    time.sleep(1)

    # Check if hand is splittable, offer split.
    # Put second card into new hand and deal both hands to 2 cards.
    if players_list[player_id].hand[0][:2] == players_list[player_id].hand[1][:2]:
        print("%s can split.\n" % players_list[player_id].name)
        time.sleep(1)

        while True:
            print("Would you like to split? Yes/No:\n")
            split_pair = str(input())
            print("")

            # If yes, split the hand.
            # If no, break and continue to main loop.
            if split_pair in ["Yes", "yes", "y", "Y"]:
                players_list[player_id].state_changer(players_list[player_id].split_state, "in_play")
                time.sleep(1)
                print("%s splits their pair and is given extra cards.\n" % players_list[player_id].name)
               

                # Move the second card in players hand to a different hand.
                players_list[player_id].hand_splitter(players_list[player_id].hand, players_list[player_id].split_hand)
                
                
                # Randomly deal 1 card to both hands for the player.
                players_list[player_id].card_deal(players_list[player_id].hand)
                players_list[player_id].card_deal(players_list[player_id].split_hand)
                time.sleep(1)   
                print("%s's first hand is %s.\n" % (players_list[player_id].name, players_list[player_id].hand))
                time.sleep(1)
                print("%s's second hand is %s.\n" % (players_list[player_id].name, players_list[player_id].split_hand))
                time.sleep(1)
                break
            elif split_pair in ["No", "no", "n", "N"]:
                print("%s does not split their hand.\n" % players_list[player_id].name)
                break
            else:
                time.sleep(0.5)
                print("Must enter 'yes' or 'no'!!\n")

    # Check if player has split, if not do first loop.
    if players_list[player_id].split_state[0] != "in_play":   
        while True:
            print("%s: Hit or stand?\n" % players_list[player_id].name)
            hit_or_stand = str(input()) 
            print("")
            time.sleep(0.5)

            if hit_or_stand in ["hit", "Hit"]:
                print("%s has hit.\n"% players_list[player_id].name)
                # Add random card from deck to player i's hand.
                players_list[player_id].card_deal(players_list[player_id].hand)
                time.sleep(1)
                # Print their new hand.                
                print("%s's hand is now %s.\n" % (players_list[player_id].name, players_list[player_id].hand))
                time.sleep(0.75)

                # Check if new hand is bust.
                if count_hand(players_list[player_id].hand) > MAX_CARD_COUNT:
                    # If count > 21, set state to bust and print.
                    players_list[player_id].state_changer(players_list[player_id].state, "bust")
                    print("%s has bust!" % players_list[player_id].name)
                    break

            # If player stands, set state to stood and print.
            elif hit_or_stand in ["stand", "Stand"]:
                players_list[player_id].state_changer(players_list[player_id].state, "stood")
                print("%s stands with a count of %s." %(players_list[player_id].name, count_hand(players_list[player_id].hand)))
                break
            # If invalid input (not hit or stand), repeat loop
            else:
                print("Must enter 'hit' or 'stand'!!\n")
                time.sleep(1)

    # If player has split, perform these loops instead.
    else: 
        # First hand loop
        while True:
            print("%s, first hand: Hit or stand?\n" % players_list[player_id].name)
            hit_or_stand = str(input()) 
            print("")
            time.sleep(0.5)

            if hit_or_stand in ["hit", "Hit"]:
                print("%s hits their first hand.\n" % players_list[player_id].name)
                # Add random card from deck to player i's hand.
                players_list[player_id].card_deal(players_list[player_id].hand)
                # Print their new hand.
                time.sleep(1)
                print("%s's first hand is %s.\n" % (players_list[player_id].name, players_list[player_id].hand))
                time.sleep(0.75)

                 # Check if new hand is bust.
                if count_hand(players_list[player_id].hand) > MAX_CARD_COUNT:
                    # If count > 21, set state to bust and print.
                    players_list[player_id].state_changer(players_list[player_id].state, "bust")
                    print("%s's first hand has bust!" % players_list[player_id].name)
                    break

            elif hit_or_stand in ["stand", "Stand"]:
                players_list[player_id].state_changer(players_list[player_id].state, "stood")
                print("%s stands their first hand with a count of %s.\n" %(players_list[player_id].name, count_hand(players_list[player_id].hand)))
                break
            # If invalid input (not hit or stand), repeat loop
            else:
                print("Must enter 'hit' or 'stand'!!\n")
                time.sleep(1)

        # Second hand loop
        print("%s's second hand is %s.\n" % (players_list[player_id].name,players_list[player_id].split_hand))
        time.sleep(1)

        while True:
            print("%s, second hand: Hit or stand?\n" % players_list[player_id].name)
            hit_or_stand = str(input()) 
            print("")
            time.sleep(0.5)

            if hit_or_stand in ["hit", "Hit"]:
                print("%s hits their second hand.\n" % players_list[player_id].name)
                # Add random card from deck to player i's hand.
                players_list[player_id].card_deal(players_list[player_id].split_hand)
                # Print their new hand.
                time.sleep(1)
                print("%s's second hand is %s." % (players_list[player_id].name, players_list[player_id].split_hand))
                time.sleep(0.75)

                 # Check if new hand is bust.
                if count_hand(players_list[player_id].split_hand) > MAX_CARD_COUNT:
                    # If count > 21, set state to bust and print.
                    players_list[player_id].state_changer(players_list[player_id].split_state, "bust")
                    print("%s's first hand has bust!" % players_list[player_id].name)
                    break

            elif hit_or_stand in ["stand", "Stand"]:
                players_list[player_id].state_changer(players_list[player_id].split_state, "stood")
                print("%s stands their second hand with a count of %s." %(players_list[player_id].name, count_hand(players_list[player_id].split_hand)))
                break
            # If invalid input (not hit or stand), repeat loop
            else:
                print("Must enter 'hit' or 'stand'!!\n")
                time.sleep(1)



# Now all players have completed turns and hands are in state 'stood' or 'bust'.
# Can now give dealer cards, stopping when count \geq 17.
time.sleep(1)
print("_________________________\n")
time.sleep(1)
print("The dealer has %s.\n" % dealer.hand)
# Randomly give the dealer cards until their count is => 17
while count_hand(dealer.hand) < 17:
    dealer.card_deal(dealer.hand)
    time.sleep(1)
    print("Dealer draws %s.\n" % dealer.hand[len(dealer.hand)-1])
    time.sleep(1)
    print("Dealer's hand is now %s.\n" % dealer.hand)
    time.sleep(1)
print("Dealer's final count is %i!" % count_hand(dealer.hand))
time.sleep(1)
print("_________________________\n")
dealer_count = count_hand(dealer.hand)



# If statements for the different scenarios.
# If dealer goes bust, tell non-bust players they are winners, and bust players they are losers.
if dealer_count > MAX_CARD_COUNT:
    print("Dealer is bust with a count of %i!" % dealer_count)
    print("_________________________\n")
    time.sleep(1)
    for player_id in range(number_of_players):
        # First check if player has split.
        if players_list[player_id].split_state[0] in ["stood", "bust"]:
            # Now run through possibilities.
            if players_list[player_id].state[0] == "stood":
                print("%s's first hand wins!\n" % players_list[player_id].name)
                time.sleep(1)

            if players_list[player_id].state[0] == "bust":
                print("%s's first hand loses!\n" % players_list[player_id].name)
                time.sleep(1)

            if players_list[player_id].split_state[0] == "stood":
                print("%s's second hand wins!\n" % players_list[player_id].name)
                time.sleep(1)

            if players_list[player_id].split_states[0] == "bust":
                print("%s's second hand loses!\n" % players_list[player_id].name)
                time.sleep(1)
        else:
            if players_list[player_id].state[0] == "stood":
                print("%s wins!\n" % players_list[player_id].name)
                time.sleep(1)

            if players_list[player_id].state[0] == "bust":
                print("%s loses!\n" % players_list[player_id].name)
                time.sleep(1)

else:
# If dealer count \leq 21, compare count to non-bust players and decide win or push.
    for player_id in range(number_of_players):
        # First check if player has split
        if players_list[player_id].split_state[0] in ["stood", "bust"]:
            # Now run through possibilities, with Push meaning a draw
            if players_list[player_id].state[0] == "bust":
                print("%s's first hand loses!\n" % players_list[player_id].name)
                time.sleep(1)
            else:
                if count_hand(players_list[player_id].hand) == dealer_count:
                    print("%s's first hand is a push!\n" % players_list[player_id].name)
                    time.sleep(1)
                if count_hand(players_list[player_id].hand) < dealer_count:
                    print("%s's first hand loses!\n" % players_list[player_id].hand)
                    time.sleep(1)
                if count_hand(players_list[player_id].hand) > dealer_count:
                    print("%s's first hand wins!\n" % players_list[player_id].name)
                    time.sleep(1)

            if players_list[player_id].split_state[0] == "bust":
                print("%s's second hand loses!\n" % players_list[player_id].name)
                time.sleep(1)
            else:
                if count_hand(players_list[player_id].split_hand) == dealer_count:
                    print("%s's second hand is a push!\n" % players_list[player_id].name)
                    time.sleep(1)
                if count_hand(players_list[player_id].split_hand) < dealer_count:
                    print("%s's second hand loses!\n" % players_list[player_id].name)
                    time.sleep(1)
                if count_hand(players_list[player_id].split_hand) > dealer_count:
                    print("%s's second hand wins!\n" % players_list[player_id].name)
                    time.sleep(1) 
        
        else:
            if players_list[player_id].state[0] == "bust":
                print("%s loses!\n" % players_list[player_id].name)
                time.sleep(1)
            else:
                if count_hand(players_list[player_id].hand) == dealer_count:
                    print("%s's hand is a push!\n" % players_list[player_id].name)
                    time.sleep(1)
                if count_hand(players_list[player_id].hand) < dealer_count:
                    print("%s loses!\n" % players_list[player_id].name)
                    time.sleep(1)
                if count_hand(players_list[player_id].hand) > dealer_count:
                    print("%s wins!\n" % players_list[player_id].name)
                    time.sleep(1)

print("Thanks for playing!\n")