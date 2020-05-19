#make blackjack game, 1-7 players, one 52 card deck 

#first define deck
deck = ["2 of hearts","3 of hearts","4 of hearts","5 of hearts","6 of hearts","7 of hearts","8 of hearts","9 of hearts","10 of hearts","Jack of hearts","Queen of hearts","King of hearts","Ace of of hearts","2 of clubs","3 of clubs","4 of clubs","5 of clubs","6 of clubs","7 of clubs","8 of clubs","9 of clubs","10 of clubs","Jack of clubs","Queen of clubs","King of clubs","Ace of clubs","2 of diamonds","3 of diamonds","4 of diamonds","5 of diamonds","6 of diamonds","7 of diamonds","8 of diamonds","9 of diamonds","10 of diamonds","Jack of diamonds","Queen of diamonds","King of diamonds","Ace of diamonds","2 of spades","3 of spades","4 of spades","5 of spades","6 of spades","7 of spades","8 of spades","9 of spades","10 of spades","Jack of spades","Queen of spades","King of spades","Ace of spades"]

#define a counting function, takes input of a hand consisting of the above "cards" and returns the blackjack count
def count_func(a_hand):
    count=0
    for j in range(len(a_hand)):        
        if a_hand[j][:2] == "10" or a_hand[j][:2] == "Ja" or a_hand[j][:2] == "Qu" or a_hand[j][:2] == "Ki":
            count=count+10
        elif a_hand[j][:2] == "Ac":
            count=count+11
        else:
            count=count+int(a_hand[j][:1])
        if count>21:
            if a_hand[0][:2] == "Ac" or a_hand[1][:2] == "Ac":
                count=count-10
    return count

import numpy
import time
from random import randint

#Welcome message, input request for number of players
print("")
print("Welcome to Blackjack.")
time.sleep(1.25)
print("")
print("Input the number of players (1-7):")
print("")
number_of_players = input()

#lists the acceptable inputs for use below, not accepting anything but these
acceptable_inputs = [1,2,3,4,5,6,7]

#only accept valid inputs (integer between 1 and 7)
while True:
    try:
        number_of_players = int(number_of_players)
        if int(number_of_players) in acceptable_inputs:
            break
        else:
            x=2/0
    except:
        print("")
        print("Number of players must be an integer between 1 and 7.")
        print("")
        time.sleep(1)
        print("Input the number of players (1-7):")
        print("")
        number_of_players = input()
time.sleep(0.5)
number_of_players = int(number_of_players)
print("")
print("Starting a %d player game."% number_of_players)

#generate empty lists to hold enough hands for number of players +1 for dealer's hand
hands=[]
for m in range(number_of_players+1):
    hands.append([])

#generate empty list to hold split hands
hands_split=[]
for m in range(number_of_players+1):
    hands_split.append([])

#give everyone 2 cards, give dealer one card (dealers hand is held in last element of list)
for i in range(number_of_players):
    for j in range(2):
        x = randint(0,len(deck)-1)
        hands[i].append(deck[x])
        deck.remove(deck[x]) 
for i in range(number_of_players,number_of_players+1):
    x = randint(0,len(deck)-1)
    hands[i].append(deck[x])
    deck.remove(deck[x]) 

#make list of states for each player
#state 0 means in play, can hit or stand
#state 1 means has manually stood
#state 2 means bust
states=[]
for m in range(number_of_players):
    states.append(int(0))
#generate states of split hands
states_split=[]
for m in range(number_of_players):
    states_split.append(int(0))

#the main game loop
#checks if can split, offers if can
#should run through each player, asking hit or stand
#if hit, checks if bust
#if all stand or bust, dealer draws until winner is found

for i in range(number_of_players):
    time.sleep(1)
    print("_________________________")
    print("")
    time.sleep(1)
    print("Player %i's turn." % int(i+1))
    print("")
    time.sleep(1)
    print("The dealer has %s." % hands[number_of_players])
    print("")
    time.sleep(1)
    print("Player %i has %s." % (int(i+1), hands[i]))
    time.sleep(1)

    #check if hand is splittable, offer split, 
    # put second card into new hand and deal both hands to 2 cards
    if hands[i][0][:2] == hands[i][1][:2]:
        print("")
        print("Player %i can split." % int(i+1))
        print("")
        time.sleep(1)
        print("Would you like to split? Yes/No:")
        print("")
        split_pair = str(input())
        acceptable_split_inputs = ["Yes","yes","y","Y","No","no","n","N"]
        while True:
            try:
                #if yes, split the hand
                #if no, break and continue to main loop
                #else invalid to proceed to exception
                if split_pair in acceptable_split_inputs:
                    if split_pair == "Yes" or split_pair == "yes" or split_pair == "y" or split_pair == "Y":
                        time.sleep(1)
                        print("")    
                        print("Player %i splits their pair and is given extra cards." % int(i+1))
                        print("")
                        hands_split[i].append(hands[i][1])
                        hands[i].remove(hands[i][1])
                        x = randint(0,len(deck)-1)
                        hands[i].append(deck[x])
                        deck.remove(deck[x]) 
                        x = randint(0,len(deck)-1)
                        hands_split[i].append(deck[x])
                        deck.remove(deck[x]) 
                        break
                    else:
                        print("")
                        print("Player %i does not split their hand." % int(i+1))
                        print("")
                        break
                else:
                    x=2/0
            except:
                #exception to guaruntee appropriate input
                time.sleep(0.5)
                print("")
                print("Must enter 'yes' or 'no'!!")
                print("")
                time.sleep(1)
                print("Would you like to split!? Yes/No:")
                print("")
                split_pair = str(input())



    #the main loop
    while True:
        print("")    
        print("Player %i: Hit or stand?" % int(i+1))
        print("")
        hit_or_stand = str(input()) 
        time.sleep(0.5)
        try:
            if hit_or_stand == "hit" or hit_or_stand == "Hit":
                print("")
                print("Player %i has hit."% int(i+1))
                print("")
                #add random card from deck to player i's hand
                x = randint(0,len(deck)-1)
                hands[i].append(deck[x])
                deck.remove(deck[x]) 
                #print their new hand
                time.sleep(1)
                print("Player %i has %s." % (int(i+1), hands[i]))
                time.sleep(0.75)
                #check if bust
                if count_func(hands[i]) > 21:
                    #if count > 21, set state to 2 (bust) and print
                    states[i]=2
                    print("")
                    print("Player %i has bust!" % int(i+1))
                    break
            elif hit_or_stand == "stand" or hit_or_stand == "Stand":
                #if player stands, set state to 1 (stand) and print
                states[i]=1
                print("")
                print("Player %i stands with a count of %s." %(int(i+1),count_func(hands[i])))
                break
            else:
                #invalid code if neither hit nor stand to force exception below
                x=2/0
        except:
            #exception to guaruntee either hit or stand strings as inputs
            print("")
            time.sleep(1)
            print("Must enter 'hit' or 'stand'!!")
            print("")
            time.sleep(1)
            print("Hit or stand:")
            print("")
            hit_or_stand = str(input())

#now all players have completed turns and are either in state 1 or 2 (stand or bust)
#can now give dealer cards, stopping when count \geq 17
time.sleep(1)
print("_________________________")
print("")
time.sleep(1)
print("The dealer has %s." % hands[number_of_players])
while count_func(hands[number_of_players]) < 17:
    x = randint(0,len(deck)-1)
    hands[number_of_players].append(deck[x])
    time.sleep(1)
    print("")
    print("Dealer draws %s." % deck[x])
    print("")
    deck.remove(deck[x])
    time.sleep(1)
    print("Dealer's hand is now %s." % hands[number_of_players])
    time.sleep(1)
print("_________________________")
time.sleep(1)
print("")
print("Dealer's final count is %i!" % count_func(hands[number_of_players]))
time.sleep(1)
print("_________________________")
print("")
dealer_count = count_func(hands[number_of_players])


#if statements for the different scenarios

#if dealer goes bust, tell non-bust players they are winners, and bust players they are losers
if dealer_count > 21:
    print("Dealer is bust with a count of %i!" % dealer_count)
    print("")
    
    for i in range(len(states)):
        time.sleep(1)
        if states[i] == 1:
            print("Player %i is a winner!" % int(i+1))
            print("")
        if states[i]==2:
            print("Player %i is a loser!" % int(i+1))
            print("")

#if dealer count \leq 21, compare count to non-bust players and decide win or push.
if dealer_count < 22:
    for i in range(number_of_players):
        time.sleep(1)
        if states[i] == 2:
            print("Player %i is a loser!" % int(i+1))
            print("")
        else:
            if count_func(hands[i]) == dealer_count:
                print("Player %i's hand is a push!" % int(i+1))
                print("")
            if count_func(hands[i]) < dealer_count:
                print("Player %i is a loser!" % int(i+1))
                print("")
            if count_func(hands[i]) > dealer_count:
                print("Player %i is a winner!" % int(i+1))
                print("")



#add split functionality

#note splitting half implemented, not functional properly
#breaks loop early skipping main loop for non-split hands