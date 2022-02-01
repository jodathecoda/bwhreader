import os
import sys
import re

global cwd
cwd = os.getcwd()

start = "Hand"
flop =  "FLOP"
turn =  "TURN"
river = "RIVER"
end =   "SUMMARY"
dealt = "Dealt"
collected = "collected"
seat = "Seat"

checks = "checks"
posts =  "posts"
calls =  "calls"
bets =   "bets"
raises = "raises"
folds =  "folds"
small_blind = "small"
big_blind = "big"

RED   = '\033[1;31m'
BLUE  = '\033[1;34m'
CYAN  = '\033[1;36m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD    = '\033[;1m'
REVERSE = '\033[;7m'
GREY = '\033[1;30m'
YELLOW='\033[0;33m'
RESET= '\033[0m'

suit_club = '\u2663'
suit_diamond = '\u2666'
suit_heart = '\u2665'
suit_spade = '\u2660'

colors_on = 1
if colors_on:
    suit_club = GREEN + '\u2663' + RESET
    suit_diamond = BLUE + '\u2666' + RESET
    suit_heart = RED + '\u2665' + RESET
    suit_spade = GREY + '\u2660' + RESET

actions = []
actions.append(start)
actions.append(flop)
actions.append(turn)
actions.append(river)
actions.append(posts)
actions.append(calls)
actions.append(bets)
actions.append(raises)
actions.append(folds)
actions.append(checks)
actions.append(dealt)
actions.append(collected)

flop_table = ""
turn_table = ""
river_table = ""
hand_title = ""
hand_action = ""
hero_button = ""
villain_button = ""

def print_table(hand_title, hand_action):
    if skip_print:
        pass
    clearscreen()
    if incognito:
        print(villain_hand[1:-2] + villain_button + " " + str(vilbet) + " : " + str(herobet)  + " " +hero_button + hero_hand[1:-2])
        print("sum:" + str(pot) + " " +flop_table.rstrip()[1:-1] + turn_table.rstrip()[1:-1] + river_table[1:-2] + " " + hand_title)
    else:
        print(hand_title)
        print(villain_nickname + " "+ villain_button + " " + villain_hand)
        print("-----------------------------")
        print("     " + str(vilbet))
        print("")
        print("     " + flop_table.rstrip() + turn_table.rstrip() + river_table)
        print(" pot: " + str(pot))
        print("")
        print("     " + str(herobet))
        print("-----------------------------")
        print(hero + " " + hero_button + " " + hero_hand)
        print("")
        print(hand_action)
    dumb = input("]")

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

if os.name == 'posix':
    pass

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

pl = 0
history = []
index = 0

incognito = 0
if len(sys.argv) > 1:
    if sys.argv[1] == 'i':
        #incognito mode
        incognito = 1

#incognito = 1

if incognito:
    print("1-34")
else:
    print("1 bachmann.juergen vs deepstack.ai")
    print("2 bos.alexander vs deepstack.ai")
    print("3 dmit.pol vs deepstack.ai")
    print("4 eshkar.eyal vs deepstack.ai")
    print("5 freire.gaia vs deepstack.ai")
    print("6 gavin.fintan vs deepstack.ai")
    print("7 indenok.sergey vs deepstack.ai")
    print("8 islam.jefri vs deepstack.ai")
    print("9 laak.phil vs deepstack.ai")
    print("10 lesnoy.dmitry vs deepstack.ai")
    print("11 moschitta.luca vs deepstack.ai")
    print("12 naumenko.igor vs deepstack.ai")
    print("13 okearney.dara vs deepstack.ai")
    print("14 parlavecchio.antonio vs deepstack.ai")
    print("15 pastor.juan_manuel vs deepstack.ai")
    print("16 phan.mike vs deepstack.ai")
    print("17 pizzarello.silvio vs deepstack.ai")
    print("18 qin.youwei vs deepstack.ai")
    print("19 santos.victor vs deepstack.ai")
    print("20 schaumann.lucas vs deepstack.ai")
    print("21 schwab.sebastian vs deepstack.ai")
    print("22 sethi.muskan vs deepstack.ai")
    print("23 shabalin.ivan vs deepstack.ai")
    print("24 shaposhnikov.roman vs deepstack.ai")
    print("25 shrimankar.prakshat vs deepstack.ai")
    print("26 sturc.martin vs deepstack.ai")
    print("27 sun.fan vs deepstack.ai")
    print("28 sun.kaishi vs deepstack.ai")
    print("29 takeda.tsuneaki vs deepstack.ai")
    print("30 talacka.giedrius vs deepstack.ai")
    print("31 tishekvich.stas vs deepstack.ai")
    print("32 voloshin.stanislav vs deepstack.ai")
    print("33 zurr.shai vs deepstack.ai")
    print("34 fedor.holz vs wiktor.malinowski")
try:
    pl = int(input("choose number: "))
except:
    print("enter number 1-34")

if pl > 0 and pl < 35:
    pass
else:
    print("error file number")
    sys.exit()
hero = ""
villain = "DeepStack"
villain_nickname = "deep.stack"
if pl == 1:
    hero = "bachmann.juergen"
    f = open(cwd + '\\full_info\\all_hands.bachmann.juergen.log',"r")
elif pl == 2:
    hero = "bos.alexander"
    f = open(cwd + '\\full_info\\all_hands.bos.alexander.log',"r")
elif pl == 3:
    hero = "dmit.pol" 
    f = open(cwd + '\\full_info\\all_hands.dmit.pol.log',"r")
elif pl == 4:
    hero = "eshkar.eyal"
    f = open(cwd + '\\full_info\\all_hands.eshkar.eyal.log',"r")
elif pl == 5:
    hero = "freire.gaia" 
    f = open(cwd + '\\full_info\\all_hands.freire.gaia.log',"r")
elif pl == 6:
    hero = "gavin.fintan" 
    f = open(cwd + '\\full_info\\all_hands.gavin.fintan.log',"r")
elif pl == 7:
    hero = "indenok.sergey"
    f = open(cwd + '\\full_info\\all_hands.indenok.sergey.log',"r")
elif pl == 8:
    hero = "islam.jefri"
    f = open(cwd + '\\full_info\\all_hands.islam.jefri.log',"r")
elif pl == 9:
    hero = "laak.phil"
    f = open(cwd + '\\full_info\\all_hands.laak.phil.log',"r")
elif pl == 10:
    hero = "lesnoy.dmitry"
    f = open(cwd + '\\full_info\\all_hands.lesnoy.dmitry.log',"r")
elif pl == 11:
    hero = "moschitta.luca"
    f = open(cwd + '\\full_info\\all_hands.moschitta.luca.log',"r")
elif pl == 12:
    hero = "naumenko.igor"
    f = open(cwd + '\\full_info\\all_hands.naumenko.igor.log',"r")
elif pl == 13:
    hero = "okearney.dara"
    f = open(cwd + '\\full_info\\all_hands.okearney.dara.log',"r")
elif pl == 14:
    hero = "parlavecchio.antonio"
    f = open(cwd + '\\full_info\\all_hands.parlavecchio.antonio.log',"r")
elif pl == 15:
    hero = "pastor.juan_manuel"
    f = open(cwd + '\\full_info\\all_hands.pastor.juan_manuel.log',"r")
elif pl == 16:
    hero = "phan.mike"
    f = open(cwd + '\\full_info\\all_hands.phan.mike.log',"r")
elif pl == 17:
    hero = "pizzarello.silvio"
    f = open(cwd + '\\full_info\\all_hands.pizzarello.silvio.log',"r")
elif pl == 18:
    hero = "qin.youwei"
    f = open(cwd + '\\full_info\\all_hands.qin.youwei.log',"r")
elif pl == 19:
    hero = "santos.victor"
    f = open(cwd + '\\full_info\\all_hands.santos.victor.log',"r")
elif pl == 20:
    hero = "schaumann.lucas"
    f = open(cwd + '\\full_info\\all_hands.schaumann.lucas.log',"r")
elif pl == 21:
    hero = "schwab.sebastian"
    f = open(cwd + '\\full_info\\all_hands.schwab.sebastian.log',"r")
elif pl == 22:
    hero = "sethi.muskan"
    f = open(cwd + '\\full_info\\all_hands.sethi.muskan.log',"r")
elif pl == 23:
    hero = "shabalin.ivan"
    f = open(cwd + '\\full_info\\all_hands.shabalin.ivan.log',"r")
elif pl == 24:
    hero = "shaposhnikov.roman"
    f = open(cwd + '\\full_info\\all_hands.shaposhnikov.roman.log',"r")
elif pl == 25:
    hero = "shrimankar.prakshat"
    f = open(cwd + '\\full_info\\all_hands.shrimankar.prakshat.log',"r")
elif pl == 26:
    hero = "sturc.martin"
    f = open(cwd + '\\full_info\\all_hands.sturc.martin.log',"r")
elif pl == 27:
    hero = "sun.fan"
    f = open(cwd + '\\full_info\\all_hands.sun.fan.log',"r")
elif pl == 28:
    hero = "sun.kaishi"
    f = open(cwd + '\\full_info\\all_hands.sun.kaishi.log',"r")
elif pl == 29:
    hero = "takeda.tsuneaki"
    f = open(cwd + '\\full_info\\all_hands.takeda.tsuneaki.log',"r")
elif pl == 30:
    hero = "talacka.giedrius"
    f = open(cwd + '\\full_info\\all_hands.talacka.giedrius.log',"r")
elif pl == 31:
    hero = "tishekvich.stas"
    f = open(cwd + '\\full_info\\all_hands.tishekvich.stas.log',"r")
elif pl == 32:
    hero = "voloshin.stanislav"
    f = open(cwd + '\\full_info\\all_hands.voloshin.stanislav.log',"r")
elif pl == 33:
    hero = "zurr.shai"
    f = open(cwd + '\\full_info\\all_hands.zurr.shai.log',"r")
elif pl == 34:
    hero = "fedor.holz"
    f = open(cwd + '\\full_info\\all_hands.fedor.holz.log',"r")
    villain = "wiktor.malinowski"
    villain_nickname = "wiktor.malinowski"
else:
    pass

hand_lines = []
counter_lines = 0   
for line in f:
    history.append(line)
f.close()

line_counter = 0
counter_hands = 0
action_points = []
for current_line in history:
    if start in current_line:
        counter_hands += 1
    tokens = current_line.split()
    for act in actions:
        if act in tokens and seat not in tokens:
            action_points.append(current_line)
    line_counter += 1

start_hand = 0
if incognito:
    pass 
else:          
    print("number of hands: " + str(counter_hands - 1))
    #dumb = input("]")
    
starting_hand_number = input("which hand do you want to start from?")
if starting_hand_number.isdigit():
    start_hand = int(starting_hand_number)
marker = 0
current = action_points[marker]
clear_it = 0
pot = 0
back = 0
herobet = 0
vilbet = 0
pot_offset = 0
hero_hand = ""
villain_hand = ""
flop_table = ""
turn_table = ""
river_table = ""
hand_title = ""
hand_action = ""
hero_button = ""
villain_button = ""
if incognito:
    hero_button = "(?)"
    villain_button = "(?)"
skip_print = 0
current_hand_number = 0

while(True):
    but_press = "z"
    if clear_it:
        clear_it = 0
        pot = 0
        herobet = 0
        vilbet = 0
        pot_offset = 0
        hero_hand = ""
        villain_hand = ""
        hand_title = ""
        hand_action = ""
        flop_table = ""
        turn_table = ""
        river_table = ""
        hero_button = ""
        villain_button = ""
        if incognito:
            hero_button = "(?)"
            villain_button = "(?)"
        skip_print = 0
        clearscreen()
    else:
        pass
    if but_press == "b" and marker > 0:
        marker -= 1
        back = 1
        current = action_points[marker]
    elif marker <= len(action_points):
        marker += 1
        back = 0
        current = action_points[marker]
    else:
        pass

    if start in current:
        current_hand_number += 1

    if current_hand_number >= start_hand:
        if posts in current and villain in current and small_blind in current:
            villain_button = "D"
            if incognito:
                villain_button = "(!)"
        if posts in current and hero in current and small_blind in current:
            hero_button = "D"
            if incognito:
                hero_button = "(!)"
        if flop in current or turn in current or river in current:
            pot_offset = pot
            herobet = 0
            vilbet = 0
            skip_print = 1
        if "Dealt" in current and hero in current:
            hero_hand = current[-8:]
            if incognito:
                pass
            else:
                hero_hand = hero_hand.replace("s", suit_spade)
                hero_hand = hero_hand.replace("h", suit_heart)
                hero_hand = hero_hand.replace("d", suit_diamond)
                hero_hand = hero_hand.replace("c", suit_club)
            skip_print = 1
        if "Dealt" in current and villain in current:
            villain_hand = current[-8:]
            villain_hand_raw = current[-8:]
            if incognito:
                pass
            else:
                villain_hand = villain_hand.replace("s", suit_spade)
                villain_hand = villain_hand.replace("h", suit_heart)
                villain_hand = villain_hand.replace("d", suit_diamond)
                villain_hand = villain_hand.replace("c", suit_club)
            skip_print = 1
        if flop in current:
            flop_table = current[-11:]
            if incognito:
                pass
            else:
                flop_table = flop_table.replace("s", suit_spade)
                flop_table = flop_table.replace("h", suit_heart)
                flop_table = flop_table.replace("d", suit_diamond)
                flop_table = flop_table.replace("c", suit_club)
            skip_print = 1
        if turn in current:
            turn_table = current[-5:]
            if incognito:
                pass
            else:
                turn_table = turn_table.replace("s", suit_spade)
                turn_table = turn_table.replace("h", suit_heart)
                turn_table = turn_table.replace("d", suit_diamond)
                turn_table = turn_table.replace("c", suit_club)
            skip_print = 1
        if river in current:
            river_table = current[-5:]
            if incognito:
                pass
            else:
                river_table = river_table.replace("s", suit_spade)
                river_table = river_table.replace("h", suit_heart)
                river_table = river_table.replace("d", suit_diamond)
                river_table = river_table.replace("c", suit_club)
        if checks in current and villain in current:
            vilbet = 0
            if incognito:
                print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
            else:
                print_table("Hand #" + str(current_hand_number), current)
        if checks in current and hero in current:
            herobet = 0
            if incognito:
                print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
            else:
                print_table("Hand #" + str(current_hand_number), current)
        if folds in current and villain in current:
            vilbet = 0
            clear_it = 1
            if incognito:
                print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
            else:
                print_table("Hand #" + str(current_hand_number), current)
        if folds in current and hero in current:
            herobet = 0
            clear_it = 1
            if incognito:
                print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
            else:
                print_table("Hand #" + str(current_hand_number), current)

        if  raises in current or bets in current:
            tokens = current.split()
            potential_bet = 0
            found_bet = 0

            for t in tokens[::-1]:
                if found_bet:
                    break
                isthis_bet = re.findall('\d+', t)
                for potential_bet in isthis_bet:
                    if potential_bet.isdigit():
                        if back:
                            pot -= int(potential_bet)
                        else:
                            pot += int(potential_bet)
                            if villain in current:
                                vilbet = int(potential_bet)
                            else:
                                herobet = int(potential_bet)
                            pot = pot_offset + herobet + vilbet
                        found_bet = 1
                        if incognito:
                            print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
                        else:
                            print_table("Hand #" + str(current_hand_number), current)
        elif  posts in current or calls in current:
            tokens = current.split()
            potential_bet = 0
            found_bet = 0
            for t in tokens[::-1]:
                if found_bet:
                    break
                isthis_bet = re.findall('\d+', t)
                for potential_bet in isthis_bet:
                    if potential_bet.isdigit():
                        if back:
                            pot -= int(potential_bet)
                        else:
                            pot += int(potential_bet)
                            if villain in current:
                                vilbet += int(potential_bet)
                            else:
                                herobet += int(potential_bet)
                            pot = pot_offset + herobet + vilbet
                        found_bet = 1
                        if incognito:
                            print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
                        else:
                            print_table("Hand #" + str(current_hand_number), current)
        if start in current:
            clear_it = 1


