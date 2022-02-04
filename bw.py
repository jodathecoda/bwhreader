import os
import sys
import re

global cwd
cwd = os.getcwd()

start = "Hand"
flop =  "Flop"
turn =  "Turn"
river = "River"
end =   "Summary"
dealt = "Dealt"
collected = "collected"
seat = "Seat"
balance = "balance"

checks = "checks"
posts =  "posts"
calls =  "calls"
bets =   "bets"
raises = "raises"
folds =  "folds"
small_blind = "small"
big_blind = "big"
table = "Table"

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
actions.append(balance)
actions.append(seat)

flop_table = ""
turn_table = ""
river_table = ""
hand_title = ""
hand_action = ""
hero_button = ""
villain_button = ""
villain_starting_stack = ""
hero_starting_stack = ""

def print_table(hand_title, hand_action):
    if skip_print:
        pass
    clearscreen()
    if incognito:
        print(villain_hand[1:-2] + villain_button + " " + str(vilbet) + " : " + str(herobet)  + " " +hero_button + hero_hand[1:-2])
        print("sum:" + str(pot) + " " +flop_table.rstrip()[1:-1] + turn_table.rstrip()[1:-1] + river_table[1:-2] + " " + hand_title)
    else:
        print(hand_title)
        print("starting stack: " + villain_starting_stack)
        print(villain_nickname + " " + villain_button + " " + villain_hand)
        print("----------------------------------------")
        print("     " + str(vilbet))
        print("")
        print("     " + flop_table.rstrip() + turn_table.rstrip() + river_table)
        print(" pot: " + str(pot))
        print("")
        print("     " + str(herobet))
        print("----------------------------------------")
        print(hero + " " + hero_button + " " + hero_hand)
        print("starting stack: " + hero_starting_stack)
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
    print("1-9")
else:
    print("select hand history file (1-9)")

try:
    pl = int(input("choose number: "))
except:
    print("enter number 1-9")

if pl > 0 and pl < 10:
    pass
else:
    print("error file number")
    sys.exit()
hero = ""
villain = "Villain"
villain_nickname = "Villain"
hero = "Hero"
if pl == 1:
    f = open(cwd + '\\hh\\HH1.txt',"r")
elif pl == 2:
    f = open(cwd + '\\hh\\HH2.txt',"r")
elif pl == 3:
    f = open(cwd + '\\hh\\HH3.txt',"r")
elif pl == 4:
    f = open(cwd + '\\hh\\HH4.txt',"r")
elif pl == 5:
    f = open(cwd + '\\hh\\HH5.txt',"r")
elif pl == 6:
    f = open(cwd + '\\hh\\HH6.txt',"r")
elif pl == 7:
    f = open(cwd + '\\hh\\HH7.txt',"r")
elif pl == 8:
    f = open(cwd + '\\hh\\HH8.txt',"r")
elif pl == 9:
    f = open(cwd + '\\hh\\HH9.txt',"r")
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
        #if act in tokens and seat not in tokens:
        if act in tokens and table not in tokens:
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
villain_starting_stack = ""
hero_starting_stack = ""
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
        hero_starting_stack = ""
        villain_starting_stack = ""
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
            hero_hand = current[-11:]
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
            flop_table = current[-16:]
            if incognito:
                pass
            else:
                flop_table = flop_table.replace("s", suit_spade)
                flop_table = flop_table.replace("h", suit_heart)
                flop_table = flop_table.replace("d", suit_diamond)
                flop_table = flop_table.replace("c", suit_club)
            skip_print = 1
        if turn in current:
            turn_table = current[-8:]
            if incognito:
                pass
            else:
                turn_table = turn_table.replace("s", suit_spade)
                turn_table = turn_table.replace("h", suit_heart)
                turn_table = turn_table.replace("d", suit_diamond)
                turn_table = turn_table.replace("c", suit_club)
            skip_print = 1
        if river in current:
            #print(current)
            #dumb = input("]-------------------------------------------------")
            river_table = current[-8:]
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
                            pot -= float(potential_bet)
                        else:
                            pot += float(potential_bet)
                            if villain in current:
                                vilbet = float(potential_bet)
                            else:
                                herobet = float(potential_bet)
                            pot = pot_offset + herobet + vilbet
                        found_bet = 1
                        if incognito:
                            print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
                        else:
                            print_table("Hand #" + str(current_hand_number), current)
        if seat in current and hero in current:
            tokens = current.split()
            potential_bet = 0
            found_bet = 0
            hero_starting_stack = tokens[-1]
        if seat in current and villain in current:
            tokens = current.split()
            potential_bet = 0
            found_bet = 0
            villain_starting_stack = tokens[-1]

        elif balance in current and villain in current:
            if "[" in current:
                val = current.split('[', 1)[1].split(']')[0]
                villain_hand = "[ " + val + " ]"
                #villain_hand_raw = current[-8:]
                if incognito:
                    pass
                else:
                    villain_hand = villain_hand.replace("s", suit_spade)
                    villain_hand = villain_hand.replace("h", suit_heart)
                    villain_hand = villain_hand.replace("d", suit_diamond)
                    villain_hand = villain_hand.replace("c", suit_club)
                if incognito:
                    print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", " ")
                else:
                    print_table("Hand #" + str(current_hand_number), " ")
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
                            pot -= float(potential_bet)
                        else:
                            pot += float(potential_bet)
                            if villain in current:
                                vilbet += float(potential_bet)
                            else:
                                herobet += float(potential_bet)
                            pot = pot_offset + herobet + vilbet
                        found_bet = 1
                        if incognito:
                            print_table("[" + str(current_hand_number) + "/" + str(counter_hands) + "]", current)
                        else:
                            print_table("Hand #" + str(current_hand_number), current)
        if start in current:
            clear_it = 1


