import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer = []
player = []

def dealer_start_card():
    for start_cards in range (2):
        dealer.append(random.choice(cards))
    return dealer

def player_start_cards():
    for start_cards in range (2):
        player.append(random.choice(cards))
    return player

def pending_A ():
    for A_value in range (len(player)):
        if player [A_value] == 11:
            player [A_value] = 1
            cards [0] = 1
            return player

def player_final_cards():
    stop_dealing = False
    while stop_dealing == False:
        hit_or_stand = input ("Do you want HIT (more card) or STAND (stop dealing)? --> H or S \n").upper()
        if hit_or_stand == "S":
            print (f" you have {player}, final value is: {sum(player)}.")
            stop_dealing = True
            return sum(player)
        elif hit_or_stand == "H":
            player.append (random.choice(cards))
            if sum (player) < 21:
                print (f" you have {player}, final value is: {sum(player)}.")
            else:
                pending_A()
                if sum(player) > 21:
                    print (f"you have {player}, {sum(player)} it is over 21, BOOM!!!")
                    stop_dealing = True
                else:
                    print (f"you have {player}, your total value is {sum(player)}")
    return sum(player)


print (f'Your cards are: {player_start_cards()}')
player_final_cards()