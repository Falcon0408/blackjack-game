# Make blackjack game, 1-7 players, one 52 card deck.

import numpy
import time
from random import randint

# First define deck.
deck = ["2 of hearts","3 of hearts","4 of hearts","5 of hearts","6 of hearts","7 of hearts","8 of hearts","9 of hearts","10 of hearts","Jack of hearts","Queen of hearts","King of hearts","Ace of of hearts","2 of clubs","3 of clubs","4 of clubs","5 of clubs","6 of clubs","7 of clubs","8 of clubs","9 of clubs","10 of clubs","Jack of clubs","Queen of clubs","King of clubs","Ace of clubs","2 of diamonds","3 of diamonds","4 of diamonds","5 of diamonds","6 of diamonds","7 of diamonds","8 of diamonds","9 of diamonds","10 of diamonds","Jack of diamonds","Queen of diamonds","King of diamonds","Ace of diamonds","2 of spades","3 of spades","4 of spades","5 of spades","6 of spades","7 of spades","8 of spades","9 of spades","10 of spades","Jack of spades","Queen of spades","King of spades","Ace of spades"]

# Define a counting function, takes input of a hand consisting of the above "cards" and returns the blackjack count.
def count_hand(hand):
    count=0
    for j in range(len(hand)):
        if hand[j][:2] == "10" or hand[j][:2] == "Ja" or hand[j][:2] == "Qu" or hand[j][:2] == "Ki":
            count=count+10
        elif hand[j][:2] == "Ac":
            count=count+11
        else:
            count=count+int(hand[j][:1])
    if count>21:
        if hand[0][:2] == "Ac" or hand[1][:2] == "Ac":
            count=count-10
    return count



# Welcome message, input request for number of players.

print("Welcome to Blackjack.\n")
time.sleep(1.25)
print("Input the number of players (1-7):\n")
number_of_players = input()
print("")

# Lists the acceptable inputs for use below, not accepting anything but these.
acceptable_inputs = [1,2,3,4,5,6,7]

# Only accept valid inputs (integer between 1 and 7).
while True:
    try:
        number_of_players = int(number_of_players)
        if int(number_of_players) in acceptable_inputs:
            break
        else:
            x=2/0
    except:
        print("Number of players must be an integer between 1 and 7.\n")
        time.sleep(1)
        print("Input the number of players (1-7):\n")
        number_of_players = input()
        print("")
time.sleep(0.5)
number_of_players = int(number_of_players)
print("Starting a %d player game."% number_of_players)

# Generate empty lists to hold enough hands for number of players +1 for dealer's hand.
hands=[]
for m in range(number_of_players+1):
    hands.append([])

# Generate empty list to hold potential split hands.
hands_split=[]
for m in range(number_of_players+1):
    hands_split.append([])

# Give everyone 2 cards, give dealer one card (dealers hand is held in last element of list).
for i in range(number_of_players):
    for j in range(2):
        x = randint(0,len(deck)-1)
        hands[i].append(deck[x])
        deck.remove(deck[x]) 
for i in range(number_of_players,number_of_players+1):
    x = randint(0,len(deck)-1)
    hands[i].append(deck[x])
    deck.remove(deck[x]) 

# Make list of states for each player.
# State 0 means in play, can hit or stand.
# State 1 means has manually stood.
# State 2 means bust.
states=[]
for m in range(number_of_players):
    states.append(int(0))
# Generate states of split hands.
states_split=[]
for m in range(number_of_players):
    states_split.append("")

# The main game loop.
# Checks if can split, offers if can.
# Should run through each player, asking hit or stand.
# If hit, checks if bust.
# If all stand or bust, dealer draws until winner is found.

for i in range(number_of_players):
    time.sleep(1)
    print("_________________________\n")
    time.sleep(1)
    print("Player %i's turn.\n" % int(i+1))
    time.sleep(1)
    print("The dealer has %s.\n" % hands[number_of_players])
    time.sleep(1)
    print("Player %i has %s.\n" % (int(i+1), hands[i]))
    time.sleep(1)

    # Check if hand is splittable, offer split.
    # Put second card into new hand and deal both hands to 2 cards.
    if hands[i][0][:2] == hands[i][1][:2]:

        print("Player %i can split.\n" % int(i+1))
        time.sleep(1)
      
        while True:
            
            print("Would you like to split? Yes/No:\n")
            split_pair = str(input())
            print("")
            # If yes, split the hand.
            # If no, break and continue to main loop.
            # Else invalid to proceed to exception.
            if split_pair in ["Yes", "yes", "y", "Y"]:
                states_split[i] = 0
                time.sleep(1)
                print("Player %i splits their pair and is given extra cards.\n" % int(i+1))
                # Move the second card in players hand to a different hand.
                hands_split[i].append(hands[i][1])
                hands[i].remove(hands[i][1])
                # Randomly deal 1 card to both hands for the player.
                x = randint(0,len(deck)-1)
                hands[i].append(deck[x])
                deck.remove(deck[x]) 
                x = randint(0,len(deck)-1)
                hands_split[i].append(deck[x])
                deck.remove(deck[x]) 
                time.sleep(1)   
                print("Player %i's first hand is %s.\n" % (int(i+1),hands[i]))
                time.sleep(1)
                print("Player %i's second hand is %s.\n" % (int(i+1),hands_split[i]))
                time.sleep(1)
                break
            elif split_pair in ["No", "no", "n", "N"]:
                print("Player %i does not split their hand.\n" % int(i+1))
                break
            else:
                # Exception to guaruntee appropriate input.
                time.sleep(0.5)
                print("Must enter 'yes' or 'no'!!\n")



    
    
    # Check if player has split, if not do first loop.
    if states_split[i] != 0:   
        while True:
            print("Player %i: Hit or stand?\n" % int(i+1))
            hit_or_stand = str(input()) 
            print("")
            time.sleep(0.5)

            if hit_or_stand in ["hit", "Hit"]:
                print("Player %i has hit.\n"% int(i+1))
                # Add random card from deck to player i's hand.
                x = randint(0,len(deck)-1)
                hands[i].append(deck[x])
                deck.remove(deck[x]) 
                time.sleep(1)
                # Print their new hand.                
                print("Player %i has %s.\n" % (int(i+1), hands[i]))
                time.sleep(0.75)

                # Check if new hand is bust.
                if count_hand(hands[i]) > 21:
                    # If count > 21, set state to 2 (bust) and print.
                    states[i]=2
                    print("Player %i has bust!\n" % int(i+1))
                    break

            # If player stands, set state to 1 (stand) and print.
            elif hit_or_stand in ["stand", "Stand"]:
                states[i]=1
                print("Player %i stands with a count of %s.\n" %(int(i+1),count_hand(hands[i])))
                break
            # If invalid input (not hit or stand), repeat loop
            else:
                print("Must enter 'hit' or 'stand'!!\n")
                time.sleep(1)

    # If player has split, perform these loops instead.
    else: 
        # First hand loop
        while True:
            print("Player %i, first hand: Hit or stand?\n" % int(i+1))
            hit_or_stand = str(input()) 
            print("")
            time.sleep(0.5)

            if hit_or_stand in ["hit", "Hit"]:
                print("Player %i has hit their first hand.\n"% int(i+1))
                # Add random card from deck to player i's hand.
                x = randint(0,len(deck)-1)
                hands[i].append(deck[x])
                deck.remove(deck[x]) 
                # Print their new hand.
                time.sleep(1)
                print("Player %i's first hand is %s.\n" % (int(i+1), hands[i]))
                time.sleep(0.75)

                # Check if bust.
                if count_hand(hands[i]) > 21:
                    states[i]=2
                    print("Player %i's first hand has bust!\n" % int(i+1))
                    break

            elif hit_or_stand in ["stand", "Stand"]:
                # If player stands, set state to 1 (stand) and print.
                states[i]=1
                print("Player %i stands their first hand with a count of %s.\n" %(int(i+1),count_hand(hands[i])))
                break
            else:
                print("Must enter 'hit' or 'stand'!!\n")
                time.sleep(1)

        # Second hand loop
        print("Player %i's second hand is %s.\n" % (int(i+1),hands_split[i]))
        time.sleep(1)
        while True:
            print("Player %i, second hand: Hit or stand?\n" % int(i+1))
            hit_or_stand = str(input()) 
            print("")
            time.sleep(0.5)
            if hit_or_stand in ["hit", "Hit"]:
                print("Player %i has hit their second hand.\n"% int(i+1))
                # Add random card from deck to player i's hand.
                x = randint(0,len(deck)-1)
                hands_split[i].append(deck[x])
                deck.remove(deck[x]) 
                # Print their new hand.
                time.sleep(1)
                print("Player %i's second hand is %s.\n" % (int(i+1), hands_split[i]))
                time.sleep(0.75)
                # Check if bust.
                if count_hand(hands_split[i]) > 21:
                    # If count > 21, set state to 2 (bust) and print.
                    states_split[i]=2
                    print("Player %i's second hand has bust!\n" % int(i+1))
                    break
            elif hit_or_stand in ["stand", "Stand"]:
                # If player stands, set state to 1 (stand) and print.
                states_split[i]=1
                print("Player %i stands their second hand with a count of %s.\n" %(int(i+1),count_hand(hands_split[i])))
                break
            else:
                print("Must enter 'hit' or 'stand'!!\n")
                time.sleep(1)

# Now all players have completed turns and are either in state 1 or 2 (stand or bust).
# Can now give dealer cards, stopping when count \geq 17.
time.sleep(1)
print("_________________________\n")
time.sleep(1)
print("The dealer has %s.\n" % hands[number_of_players])
while count_hand(hands[number_of_players]) < 17:
    x = randint(0,len(deck)-1)
    hands[number_of_players].append(deck[x])
    time.sleep(1)
    print("Dealer draws %s.\n" % deck[x])
    deck.remove(deck[x])
    time.sleep(1)
    print("Dealer's hand is now %s.\n" % hands[number_of_players])
    time.sleep(1)
print("_________________________\n")
time.sleep(1)
print("Dealer's final count is %i!" % count_hand(hands[number_of_players]))
time.sleep(1)
print("_________________________\n")
dealer_count = count_hand(hands[number_of_players])


# If statements for the different scenarios.

# If dealer goes bust, tell non-bust players they are winners, and bust players they are losers.
if dealer_count > 21:
    print("Dealer is bust with a count of %i!\n" % dealer_count)
    print("_________________________")
    time.sleep(1)
    for i in range(len(states)):
        if states_split[i] ==1 or states_split[i] == 2:
            if states[i] == 1:
                print("Player %i's first hand wins!\n" % int(i+1))
                time.sleep(1)
            if states[i]==2:
                print("Player %i's first hand loses!\n" % int(i+1))
                time.sleep(1)
            if states_split[i] == 1:
                print("Player %i's second hand wins!\n" % int(i+1))
                time.sleep(1)
            if states_split[i]==2:
                print("Player %i's second hand loses!\n" % int(i+1))
                time.sleep(1)
        else:
            if states[i] == 1:
                print("Player %i wins!\n" % int(i+1))
                time.sleep(1)
            if states[i]==2:
                print("Player %i loses!\n" % int(i+1))
                time.sleep(1)

#####done above, complete below

#if dealer count \leq 21, compare count to non-bust players and decide win or push.
if dealer_count < 22:
    for i in range(number_of_players):
        if states[i] == 2:
            print("Player %i loses!" % int(i+1))
            print("")
            time.sleep(1)
        else:
            if count_hand(hands[i]) == dealer_count:
                print("Player %i's hand is a push!" % int(i+1))
                print("")
                time.sleep(1)
            if count_hand(hands[i]) < dealer_count:
                print("Player %i loses!" % int(i+1))
                print("")
                time.sleep(1)
            if count_hand(hands[i]) > dealer_count:
                print("Player %i wins!" % int(i+1))
                print("")
                time.sleep(1)



#add split functionality

