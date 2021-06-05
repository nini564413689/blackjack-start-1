import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cards_player = cards
cards_dealer = cards
dealer = []
player = []
over_21_value = 0

def dealer_start_card():
    for start_cards in range (2):
        dealer.append(random.choice(cards))
    return dealer

def player_start_cards():
    for start_cards in range (2):
        player.append(random.choice(cards))
    return player

def pending_A (role,cards_in_use):
    over_21 = True
    while over_21 == True:
        for A_value in range (len(role)):
            if role [A_value] == 11 and sum(role)>21:
                role [A_value] = 1
                cards_in_use [0] = 1
            else:
                over_21 = False
    return role

def player_final_cards():
    stop_dealing = False
    while stop_dealing == False:
        hit_or_stand = input ("Do you want HIT (more card) or STAND (stop dealing)? --> H or S \n").upper()
        if hit_or_stand == "S":
            print (f" you have {player}, final value is: {sum(player)}.")
            stop_dealing = True
            return sum(player)
        elif hit_or_stand == "H":
            player.append (random.choice(cards_player))
            if sum (player) < 21:
                print (f" you have {player}, you have total value: {sum(player)}.")
            else:
                pending_A(player,cards_player)
                if sum(player) > 21:
                    print (f"you have {player}, {sum(player)} it is over 21, BOOM!!!")                   
                    stop_dealing = True
                    return over_21_value                
                else:
                    print (f"you have {player}, you have total value: {sum(player)}")
    return sum(player)



def dealer_final_cards():
    print ("\nDealer's turn \n")
    print (f"Dealer have{dealer}, total is: {sum(dealer)}")
    dealer_stop = False
    while dealer_stop == False:
        if sum(dealer) > 21:
            pending_A(dealer,cards_dealer)
            if sum(dealer) > 21:
                print (f"Dealer have {dealer}, BOOM!")
                dealer_stop = True
                return over_21_value
            elif sum(dealer) >= 17:
                print (f"Dealer have{dealer}, total is: {sum(dealer)}")
                dealer_stop = True
            else:
                dealer.append (random.choice(cards_dealer))
                print (f"Dealer have{dealer}, total is: {sum(dealer)}")
        elif sum(dealer) == 21:
            print (f"Dealer have {dealer}, Black Jack!")
            return 21
        elif sum(dealer) >= 17:
            dealer_stop = True
        else:
            dealer.append (random.choice(cards_dealer))
            print (f"Dealer have{dealer}, total is: {sum(dealer)}")
    return sum(dealer)



print (f"Your cards are: {player_start_cards()}")
print (f"The dealer has 2 cards, one of them is {dealer_start_card()[1]}")
player_score = player_final_cards()
dealer_score = dealer_final_cards()
if player_score > dealer_score:
    print ("You Win!!!")
elif player_score == dealer_score:
    print ("Draw")
else:
    print ("You Loss :(")