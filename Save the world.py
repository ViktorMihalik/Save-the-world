import random

# ///Welcoming screen///

print("""
Ooooh welcome unknown player. I'm going to destroy all humans! But of course I have to give you a change to defend yourself.
So you suppose to be the savior of the earth? Let ma laugh- HA-HA-HA.
If you would like to save the earth you have to beat me in 4 games. Okay than let's play a game.
""")

player_name = input("But at first 'savior' tell my your name: ")

# /// Game over///

game_over = ("""World will be destroyed and it's your fault {}

 ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄  
█ ▄▀   █ █      █ █      █ █  █ ▀  █ ▐  ▄▀   ▐ █ ▄▀   █ 
▐ █    █ █      █ █      █ ▐  █    █   █▄▄▄▄▄  ▐ █    █ 
  █    █ ▀▄    ▄▀ ▀▄    ▄▀   █    █    █    ▌    █    █ 
 ▄▀▄▄▄▄▀   ▀▀▀▀     ▀▀▀▀   ▄▀   ▄▀    ▄▀▄▄▄▄    ▄▀▄▄▄▄▀ 
█     ▐                    █    █     █    ▐   █     ▐  
▐                          ▐    ▐     ▐        ▐        

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
""".format(player_name))

good= ("""
        ..--+++--..
     .-'     |     `-.
   +'        |        `+
  '          |          `
 '           |           `
:            |            :
:          +'|`+          :
.        +'  |  `+        ;
 +     +'    |    `+     +
  `. +'      |      `+ .'
    `._      |      _.'
       `--.._|_..--' 
I decided not to destroy the world...
""")
# ///rock, paper, scissors///
# header

print("""

######  #######  #####  #    #       ######     #    ######  ####### ######      #####   #####  ###  #####   #####  ####### ######   #####  
#     # #     # #     # #   #        #     #   # #   #     # #       #     #    #     # #     #  #  #     # #     # #     # #     # #     # 
#     # #     # #       #  #         #     #  #   #  #     # #       #     #    #       #        #  #       #       #     # #     # #       
######  #     # #       ###          ######  #     # ######  #####   ######      #####  #        #   #####   #####  #     # ######   #####  
#   #   #     # #       #  #         #       ####### #       #       #   #            # #        #        #       # #     # #   #         # 
#    #  #     # #     # #   #        #       #     # #       #       #    #     #     # #     #  #  #     # #     # #     # #    #  #     # 
#     # #######  #####  #    #       #       #     # #       ####### #     #     #####   #####  ###  #####   #####  ####### #     #  #####  

""")

maxpoints_rsp = 3 # We can set higher points for win
print("{}, in this first game called rock, paper, scissor the one who scores {} points first wins ".format(player_name,maxpoints_rsp))

# Game mechanics
def player_wins(i,j):  
    
    if (i == "rock" and j == "scissors") or (i == "scissors" and j == "paper") or (i == "paper" and j == "rock"):
        return True
    elif (i == "rock" and j == "paper") or (i == "scissors" and j == "rock") or (i == "paper" and j == "scissors"):
        return False

#game body

player_point_RPS = 0
computer_points_RSP = 0

while computer_points_RSP or player_point_RPS != maxpoints_rsp:
    player_choice= input("Comon choose rock, paper or scissors: ")
    rsp= "rock","paper","scissors"
    computer_choice = random.choice(rsp)

    if player_choice  not in rsp:
        player_choice= input("You can choose only choose rock, paper or scissors: ")
    
    if player_wins(player_choice,computer_choice) is True:
        player_point_RPS += 1
        print("I choose {} so point for you.".format(computer_choice))


    if player_wins (player_choice,computer_choice) is False:
        computer_points_RSP += 1
        print("{} beat {} so point for me.".format(computer_choice,player_choice))
    
    
    if player_choice == computer_choice:
        print("Hey {}, you've red my mind I choose {} to.".format(player_name,computer_choice))
        pass

    print("Player points: {} ".format(player_point_RPS))
    print("Computer point: {}".format(computer_points_RSP))
    print()

    if player_point_RPS == maxpoints_rsp:
        print("GRHHHH How it’s possible that you beat me?!")
        break
    if computer_points_RSP == maxpoints_rsp:
        print(game_over)
        
        exit()

# ///Card game///
# header
print("""
.------..------..------..------..------..------..------..------.
|C.--. ||A.--. ||R.--. ||D.--. ||W.--. ||A.--. ||R.--. ||S.--. |
| :/\: || (\/) || :(): || :/\: || :/\: || (\/) || :(): || :/\: |
| :\/: || :\/: || ()() || (__) || :\/: || :\/: || ()() || :\/: |
| '--'C|| '--'A|| '--'R|| '--'D|| '--'W|| '--'A|| '--'R|| '--'S|
`------'`------'`------'`------'`------'`------'`------'`------'
""")

win_points = 3 # Setting points to win
print("Okay beginner's luck. {} let’s play another game called CARD WARS.\n"
"The rules are easy- who have higher card get a point. The one who get the first {} points is winner. Of course, it will be me.".format(player_name,win_points))

# Game mechanics

cards = ["6","7","8","9","10","J","Q","K","A"] # Wee can change type of cards

def flip_coin(): # In case of equal points

    player_coin = input("It's a draw, let's flip a coin. What's your choice tail or head: ").lower()
    coin = "tail","head"
    coin_side = random.choice(coin)
    if player_coin not in coin:
        player_coin= input("please choose betwen tail or head: ").lower()

    if player_coin  in coin:
        if player_coin==coin_side:
            print("Yeah good guees It's {}, player wins.".format(coin_side))
        

    else:
        print("It's {}, I'm a winner.".format(coin_side))
        print(game_over)
        
        exit()

def shuffling_cards(r):
    hand= []
    for i in range(r):
        random_cards = [str(random.choice(cards))]
        hand = hand+random_cards
    return hand
    
#game body
player_point_CRD = 0
computer_points_CRD = 0

players_cards= shuffling_cards(5)
computer_cards= shuffling_cards(5)

while computer_points_CRD or player_point_CRD != win_points:
    
    computer_choice_CRD = str(random.choice(computer_cards))

    player_choice=input("Please choose one card from your hand {}:".format(players_cards)).upper()
   
    if player_choice not in players_cards:
        player_choice=input("Again check your card and choose one {}:".format(players_cards)).upper()
      
    if cards.index(computer_choice_CRD) > cards.index(player_choice):
        print("{} is higher than {} that means point for me".format(computer_choice_CRD,player_choice))
        computer_points_CRD+=1
    if cards.index(computer_choice_CRD) < cards.index(player_choice):
        print("Okay I have {}, point for you".format(computer_choice_CRD))
        player_point_CRD+=1
    if cards.index(computer_choice_CRD) == cards.index(player_choice):
        print("My is also {}, boring no one get a point".format(computer_choice_CRD))
    
    players_cards.remove(player_choice)
    computer_cards.remove(computer_choice_CRD)
    print("{}'s points:{} and computer:{}".format(player_name,player_point_CRD,computer_points_CRD))
    print()

    if not players_cards:
        if player_point_CRD > computer_points_CRD:
            print("Hmm you won another game. Maybe I have to take it seriously")
            break
        if computer_points_CRD > player_point_CRD:
            print(game_over)
        
            exit()
        if computer_points_CRD == player_point_CRD:
            flip_coin()
            break

    if player_point_CRD == win_points:
        print("Hmm you won another game. Maybe I have to take it seriously")
        break
    
    if computer_points_CRD == win_points:
            print(game_over)
        
            exit()

# ///Guess the number///
# header
print("""  
  _   _ _    _ __  __ ____  ______ _____   ____   _____ 
 | \ | | |  | |  \/  |  _ \|  ____|  __ \ / __ \ / ____|
 |  \| | |  | | \  / | |_) | |__  | |__) | |  | | (___  
 | . ` | |  | | |\/| |  _ <|  __| |  _  /| |  | |\___ \ 
 | |\  | |__| | |  | | |_) | |____| | \ \| |__| |____) |
 |_| \_|\____/|_|  |_|____/|______|_|  \_\\____/|_____/ 
                                                        
 """)
print()
print ( "My systems do not report any armageddon, What a pitty. But it's time to change that" 
        "Guess the number I am thinking of betwen 1 and 20. But be careful {} you only have 4 attempts". format(player_name))
print()
# Game mechanics
guesses = 3
number = random.randrange(1,20)
player_guess= int(input("Guess the number I am thinking of: "))

#game body
if player_guess == number:
       print("You are a wizard {}, you guess it for the first time. ".format(player_name))

while player_guess != number:
   
       if player_guess < number:  
              player_guess= int(input("Don't be humble it's higher. C'mon guess again: "))
              guesses -= 1
       if player_guess > number:  
              player_guess= int(input("No no no, go lower. C'mon guess again: "))
              guesses -= 1
       
       if guesses == 0 and player_guess != number:
              print("My number was {}".format(number))
              print(game_over)
              quit()
              
       if player_guess == number and guesses<=1:
              print("IT was closed but you save the world for now {}.".format(player_name))
              break

       if player_guess == number and guesses>1:
              print("That is correct. I think I chose very easy game for you.".format(guesses))
              break

# ///Player can decides if he can end the game or continue///
print("Okay that wasn't bad. Look I have a little proposition for you before our last game. You can quit now and I will not destroy the world (maybe)\n"
       "On the other hand you can take a risk and earn unknow reaward")
print()
player_choose = input("So what's you choice? Would you like to continue? Choose yes or no : ").lower()

if player_choose == "no":
    consequences = good,game_over
    computer_chose = random.choice(consequences)
    print(computer_chose)
    quit()

choice= "yes","no"

if player_choose  not in choice:
    player_choose = input("I know that it can be hard for you bud just write me yes or no: ")

else :
    pass

# ///Player decided to continue///

# ///Dices///
# header
print("""
 ▄████████    ▄████████    ▄████████  ▄███████▄  ▄██   ▄        ████████▄   ▄█   ▄████████    ▄████████    ▄████████ 
███    ███   ███    ███   ███    ███ ██▀     ▄██ ███   ██▄      ███   ▀███ ███  ███    ███   ███    ███   ███    ███ 
███    █▀    ███    ███   ███    ███       ▄███▀ ███▄▄▄███      ███    ███ ███▌ ███    █▀    ███    █▀    ███    █▀  
███         ▄███▄▄▄▄██▀   ███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███      ███    ███ ███▌ ███         ▄███▄▄▄       ███        
███        ▀▀███▀▀▀▀▀   ▀███████████   ▄███▀   ▀ ▄██   ███      ███    ███ ███▌ ███        ▀▀███▀▀▀     ▀███████████ 
███    █▄  ▀███████████   ███    ███ ▄███▀       ███   ███      ███    ███ ███  ███    █▄    ███    █▄           ███ 
███    ███   ███    ███   ███    ███ ███▄     ▄█ ███   ███      ███   ▄███ ███  ███    ███   ███    ███    ▄█    ███ 
████████▀    ███    ███   ███    █▀   ▀████████▀  ▀█████▀       ████████▀  █▀   ████████▀    ██████████  ▄████████▀  
             ███    ███                                                                                              

""")

max_score = 5 # Score to winn the game
print("I have to admit you are brave. The last {} points wil decides the fate of humanity\n Let's get this over.".format(max_score))

# Game mechanics
rolling_dice = random.randint(1,6)

players_point = 0
cumpoters_point = 0
player_total= random.randint(1,6)
computer_total= random.randint(1,6)

#game body
while players_point or cumpoters_point!=max_score:
    print()
    input("press enter to roll the dice")
    player_roll1 = random.randint(1,6)
    player_roll2 = random.randint(1,6)
    player_roll3 = random.randint(1,6)
    player_total = player_roll1+player_roll2+player_roll3

    computer_roll1 = random.randint(1,6)
    computer_roll2 = random.randint(1,6)
    computer_roll3 = random.randint(1,6)
    computer_total = computer_roll1+computer_roll2+computer_roll3
    print()

    print("{0} you roll({1}, {2} and {3} = {7} total ) and computer has ({4}, {5} and {6} = {8} total )".format(player_name,player_roll1,player_roll2, player_roll3, computer_roll1, computer_roll2,computer_roll3,player_total,computer_total))
    
    if player_total > computer_total:
        players_point += 1

    elif player_total == computer_total:
        players_point+0

    else:
        cumpoters_point+=1


    print("{}'s points: {}  and computer: {}".format(player_name,players_point,cumpoters_point))

    if players_point == max_score:
        print(good)
        print("Not becouse you won. I'm just not in the mood to destry the world. however promis is promis here is your reward:")
        currency = "€","£","৳","ƒ","₹","₡","Kč","₣","₪","¥",".ރ","₮","₲","₽","฿","Ft"
        print("{0},{1}{2}{3},{4}{5}{6} {7}".format(random.randint(1,5),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
        random.randint(0,9),random.randint(0,9),random.choice(currency)))
        quit()

    if cumpoters_point == max_score:
        print(game_over)
        quit()








