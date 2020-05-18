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
    return count

import numpy
from random import randint

#Welcome message, input request for number of players
print("")
print("Welcome to Blackjack.")
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
        print("Number of players must be an integer between 1 and 7.")
        print("")
        print("Input the number of players (1-7):")
        number_of_players = input()

number_of_players = int(number_of_players)
print("")
print("Starting a %d player game."% number_of_players)
print("")

#generate empty lists to hold enough hands for number of players +1 for dealer's hand
hands=[]
for m in range(number_of_players+1):
    hands.append([])

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



#the main game loop
#should run through each player, asking hit or stand
#if hit, checks if bust
#if all stand or bust, dealer draws until winner is found





#make list of states for each player
#state 0 means in play, can hit or stand
#state 1 means has manually stood
#state 2 means bust
states=[]
for m in range(number_of_players):
    states.append(int(0))

for i in range(number_of_players):
    print("_________________________")
    print("")
    print("Player %i's turn." % int(i+1))
    print("")
    print("The dealer has %s." % hands[number_of_players])
    print("")
    print("Player %i has %s." % (int(i+1), hands[i]))
    print("")
    print("Player %i: Hit or stand?" % int(i+1))
    print("")
    
    while True:       
        hit_or_stand = str(input()) 
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
                print("Player %i has %s." % (int(i+1), hands[i]))
                #check if bust
                if count_func(hands[i]) > 21:
                    #if count > 21, set state to 2 (bust) and print
                    states[i]=2
                    print("")
                    print("Player %i has bust!" % int(i+1))
                    print("_________________________")
                    break
            elif hit_or_stand == "stand" or hit_or_stand == "Stand":
                #if player stands, set state to 1 (stand) and print
                states[i]=1
                print("")
                print("Player %i stands with a count of %s." %(int(i+1),count_func(hands[i])))
                print("_________________________")
                break
            else:
                #invalid code if neither hit nor stand to force exception below
                x=2/0
        except:
            #exception to guaruntee either hit or stand strings as inputs
            print("")
            print("Must enter 'hit' or 'stand'!!")
            print("")
            print("Hit or stand:")
            print("")
            hit_or_stand = str(input())

#now all players have completed turns and are either in state 1 or 2 (stand or bust)
#can now give dealer cards, stopping when count \geq 17
print("")
print("The dealer has %s." % hands[number_of_players])
while count_func(hands[number_of_players]) < 17:
    x = randint(0,len(deck)-1)
    hands[number_of_players].append(deck[x])
    print("")
    print("Dealer draws %s." % deck[x])
    print("")
    deck.remove(deck[x])
    print("Dealer's hand is now %s." % hands[number_of_players])
print("_________________________")
print("")
print("Dealer's final count is %i!" % count_func(hands[number_of_players]))
print("_________________________")
print("")
dealer_count = count_func(hands[number_of_players])


#if statements for the different scenarios

#if dealer goes bust, tell non-bust players they are winners, and bust players they are losers
if dealer_count > 21:
    print("Dealer is bust with a count of %i!" % dealer_count)
    for i in range(len(states)):
        if states[i] == 1:
            print("Player %i is a winner!" % int(i+1))
        if states[i]==2:
            print("Player %i is a loser!" % int(i+1))

#if dealer count \leq 21, compare count to non-bust players and decide win or push.
if dealer_count < 22:
    for i in range(number_of_players):
        if states[i] == 2:
            print("Player %i is a loser!" % int(i+1))
        else:
            if count_func(hands[i]) == dealer_count:
                print("Player %i's hand is a push!" % int(i+1))
            if count_func(hands[i]) < dealer_count:
                print("Player %i is a loser!" % int(i+1))
            if count_func(hands[i]) > dealer_count:
                print("Player %i is a winner!" % int(i+1))

