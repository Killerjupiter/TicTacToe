#By Bealex my discord is bealex if you need me

#imported module for random number generation
from random import randint, choice

#fuction controls row size, thinking of expanding upon functionality for other stuff
def yxrow(a,): 
    b = "|"
    return [a, " ", b, " ", b, " "]

#Win condition variables
win = False
ewin = 0
pwin = 0
tie = 0

#Game Board could of probably been a dictionary
Num_row = ("   1   2   3")
border_a = (" -----------")
row_a = yxrow("A")
row_b = yxrow("B")
row_c = yxrow("C")

#Valid Inputs
InputsL = ("A", "B", "C")
InputsN = ("1", "2","3")
InputsLN = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")

#invalid Inputs
taken_areas = []

#defines board placement maybe
y = None
x = None
#input splitter values
xy1 = [None, None]
y1 = None
x1 = None
#Below handles player Input 
player_1L = None
player_1N = None
#Enemy variables
O = None
#invalid Inputs
taken_areas = []

def clear_game():
    global y, x, xy1, y1, x1, player_1L, player_1N, O, taken_areas
    #defines board placement maybe
    y = None
    x = None
    #input splitter values
    xy1 = None
    y1 = None
    x1 = None
    #Below handles player Input 
    player_1L = None
    player_1N = None
    #Enemy variables
    O = None
    #invalid Inputs
    taken_areas = []

#random numbers we have none
rnumber_used = []

#functions that are defined here 
def yx_move(inputy, row): #Converts input into cordinates to put into the board using the x and y values
    if y == inputy:
        x_move(1, 1, row)
        x_move(2, 3, row)
        x_move(3, 5, row)

def x_move(inputx, convert_position, row): #takes x and given y cordinates and places the X on the board in that positon
        if x == (str(inputx)):
            row[convert_position] = "x" 

def winrow(a, b):#Ussed inside of next defined function winner()
    a[1] = b
    a[3] = b
    a[5] = b

def winner(a):
    if a == "x":
        winrow(row_a, "W")
        winrow(row_b, "W")
        winrow(row_c, "W")
    if a == "o":
        winrow(row_a, "L")
        winrow(row_b, "L")
        winrow(row_c, "L")
    if a == " ": #board clear
        winrow(row_a, " ")
        winrow(row_b, " ")
        winrow(row_c, " ")

def check_winner(a, z, c, d, e, f, g,):
    global win, pwin, ewin
    global exit
    b = ("x", "o")
    if a[d] == b[g]:
        if z[e] == b[g]:
            if c[f] == b[g]:
                if b[g] == "x":
                    winner("x")
                    printboard()
                    clear_game()
                    pwin += 1
                    win = True
                    print("YOU WIN!!! Do you want to play again?")
                    print("Y to play again or N to quit: ")
                    if input().capitalize() == "Y":
                        winner(" ")
                        win = False
                        printboard()
                    elif input().capitalize() == "N":
                        print("Thanks for playing!")
                        exit()
                elif b[g] == "o":
                    winner("o")
                    printboard()
                    clear_game()
                    ewin += 1
                    win = True
                    print("YOU LOSE!!! Do you want to play again?")
                    print("Y to play again or N to quit: ")
                    if input().capitalize() == "Y":
                        winner(" ")
                        win = False
                        printboard()
                    elif input().capitalize() == "N":
                        print("Thanks for playing!")
                        exit()

def check_winner1():
    check_winner(row_a, row_b, row_c, 1, 3, 5, 0) #Checks for win conditions that are diagonal
    check_winner(row_a, row_b, row_c, 1, 3, 5, 1) 
    check_winner(row_a, row_b, row_c, 5, 3, 1, 0)
    check_winner(row_a, row_b, row_c, 5, 3, 1, 1)
    check_winner(row_a, row_a, row_a, 1, 3, 5, 0) #Checks for win conditions that are rows
    check_winner(row_a, row_a, row_a, 1, 3, 5, 1)
    check_winner(row_b, row_b, row_b, 1, 3, 5, 0)
    check_winner(row_b, row_b, row_b, 1, 3, 5, 1)
    check_winner(row_c, row_c, row_c, 1, 3, 5, 0)
    check_winner(row_c, row_c, row_c, 1, 3, 5, 1)
    check_winner(row_a, row_b, row_c, 1, 1, 1, 0)#checks columns
    check_winner(row_a, row_b, row_c, 1, 1, 1, 1)
    check_winner(row_a, row_b, row_c, 3, 3, 3, 0)
    check_winner(row_a, row_b, row_c, 3, 3, 3, 1)
    check_winner(row_a, row_b, row_c, 5, 5, 5, 0)
    check_winner(row_a, row_b, row_c, 5, 5, 5, 1)
    
def printboard():
    if pwin > 0 or ewin > 0 or tie > 0:
        print()
        print("Players Win:", pwin, "Enemies Win:", ewin, "Ties:", tie)
    print(Num_row)
    print(" ".join(row_a))
    print(border_a)
    print(" ".join(row_b))
    print(border_a)
    print(" ".join(row_c))
    print("  ")
    
#function to handle enemy placement
def ochoice(a, b, c): #Just allows me to put in the row
        global O
        if b == 1:
            taken_areas.append(c)
            a[b] = "o"
            O = True
        if b == 2:
            b = 3
            taken_areas.append(c)
            a[b] = "o"
            O = True
        if b == 3:
            b = 5
            taken_areas.append(c)
            a[b] = "o"
            O = True

#first print of board at clean slate
print("This is TicTacToe, to play type row A, B, or C " 
    "and than select the number on that row 1, 2, or 3")
print("Example: A1, B2, or even C3")
#prints clean board
printboard() 

#Game loop
while win == False:

    check_winner1() #checks if o won

    #Decides position
    while player_1L not in InputsL or player_1N not in InputsN or player_1L + player_1N in taken_areas:
        O = None
        player_1LL = input("Input Letter and Number:").capitalize()
        xy1 = list(player_1LL)
        try:
            player_1L = xy1[0]
            player_1N = xy1[1]
        except IndexError:
            player_1L = "A"
            player_1N = "0"
        if player_1L + player_1N in taken_areas:
            print("That area is already taken")
        elif player_1L + player_1N not in taken_areas:
            if player_1L in InputsL:
                y = player_1L
            if player_1N in InputsN:
                x = player_1N
            if player_1L not in InputsL:
                print("Not a valid option")
            elif player_1N not in InputsN:
                print("Not a valid option")
            #adds the area to the taken areas list
    taken_areas.append(player_1L + player_1N)        

    #handles palyer board placement uses def yx_move and def x_move at the top of the project
    yx_move("A", row_a)
    yx_move("B", row_b)
    yx_move("C", row_c)
    
    #prints board after players move
    printboard()
    print()

    check_winner1() #calls the function to check for win conditions

    #Hopefully O's algorithm
    while O == None:
        player_1L = None
        player_1N = None

        def winning_move(a, b, c, d, e, f, g, h,): #will work on later and rename variables to replace likes 245-280 I want to say
            z = ("x", "o")
            if a[d] == z[g]:
                if z[e] == z[g]:
                    if c[f] == z[g]:
                        if b[g] == "x":
                            pass

        if "A2" not in taken_areas and row_a[1] == "o" and row_a[5] == "o":
                ochoice(row_a, 2, "A2")
        elif "C2" not in taken_areas and row_c[1] == "o" and row_c[5] == "o":
            ochoice(row_c, 2, "C2")
        elif "B1" not in taken_areas and row_a[1] == "o" and row_c[1] == "o":
            ochoice(row_b, 1, "B1")
        elif "B3" not in taken_areas and row_a[5] == "o" and row_c[5] == "o":
            ochoice(row_b, 3, "B3")
        elif "A1" not in taken_areas and row_b[1] == "o" and row_c[1] == "o":
            ochoice(row_a, 1, "A1")
        elif "A2" not in taken_areas and row_b[3] == "o" and row_c[3] == "o":
            ochoice(row_a, 2, "A2")
        elif "A3" not in taken_areas and row_b[5] == "o" and row_c[5] == "o":
            ochoice(row_a, 3, "A3")
        elif "C1" not in taken_areas and row_a[1] == "o" and row_b[1] == "o":
            ochoice(row_c, 1, "C1")
        elif "C2" not in taken_areas and row_a[3] == "o" and row_b[3] == "o":
            ochoice(row_c, 2, "C2")
        elif "C3" not in taken_areas and row_a[5] == "o" and row_b[5] == "o":
            ochoice(row_c, 3, "C3")
        elif "B2" not in taken_areas and row_a[3] == "o" and row_c[3] == "o":   
            ochoice(row_b, 2, "B2")
        elif "B2" not in taken_areas and row_b[1] == "o" and row_b[5] == "o":
            ochoice(row_b, 2, "B2")
        elif "B2" not in taken_areas and row_a[1] == "o" and row_c[5] == "o":
            ochoice(row_b, 2, "B2")
        elif "B2" not in taken_areas and row_a[5] == "o" and row_c[1] == "o":
            ochoice(row_b, 2, "B2")
        elif "A1" not in taken_areas and row_b[3] == "o" and row_c[5] == "o":
            ochoice(row_a, 1, "A1")
        elif "A3" not in taken_areas and row_b[3] == "o" and row_c[1] == "o":
            ochoice(row_a, 3, "A3")
        elif "C1" not in taken_areas and row_b[3] == "o" and row_a[5] == "o":
            ochoice(row_c, 1, "C1")
        elif "C3" not in taken_areas and row_b[3] == "o" and row_a[1] == "o":
            ochoice(row_c, 3, "C3")
        elif "B2" in taken_areas:
            rnumbners = 0
            if all(x not in taken_areas for x in ["A1", "A3", "C1", "C3"]):
                    rnumbners = randint(1, 4)
                    if rnumbners == 1:
                        ochoice(row_a, 1, "A1")
                    elif rnumbners == 2:
                        ochoice(row_a, 3, "A3")
                    elif rnumbners == 3:
                        ochoice(row_c, 1, "C1")
                    elif rnumbners == 4:
                        ochoice(row_c, 3, "C3")
            elif "A1" not in taken_areas and "C3" not in taken_areas:
                ochoice(row_a, 1, "A1")
            elif all(x not in taken_areas for x in ["C1", "A1"]):
                ochoice(row_c, 1, "C1")
            elif "C3" not in taken_areas:
                ochoice(row_c, 3, "C3")
            elif "A3" not in taken_areas:
                ochoice(row_a, 3, "A3")
            elif "A1" not in taken_areas:
                ochoice(row_a, 1, "A1")
            elif "C1" not in taken_areas:
                ochoice(row_c, 1, "C1")
            elif all(x in taken_areas for x in ["A1", "A3", "C1", "C3"]):
                loop_breaker = 0
                T = None
                while T == None and loop_breaker < 20:
                    rnumbners = randint(1, 4)
                    if rnumbners == 1 and "A2" not in taken_areas:
                        ochoice(row_a, 2, "A2")
                        T = True
                    if rnumbners == 2 and "B1" not in taken_areas:
                        ochoice(row_b, 1, "B1")
                        T = True
                    if rnumbners == 3 and "B3" not in taken_areas:
                        ochoice(row_b, 3, "B3")
                        T = True
                    if rnumbners == 4 and "C2" not in taken_areas:
                        ochoice(row_c, 2, "C2")
                        T = True
                    loop_breaker += 1
                if loop_breaker >= 20:
                    print("No valid moves left, skipping turn")
                    clear_game()
                    tie += 1
                    win = True
                    print("YOU Tied!!! Do you want to play again?")
                    print("Y to play again or N to quit: ")
                    if input().capitalize() == "Y":
                        winner(" ")
                        win = False
                        printboard()
                    elif input().capitalize() == "N":
                        print("Thanks for playing!")
                        exit()
                    O = True

        elif "B2" not in taken_areas:
            rnumbners = randint(1, 8)
            loop_breaker = 0
            if all(x not in taken_areas for x in ["A1", "A3", "C1", "C3"]) and rnumbners <= 4 and loop_breaker < 10:
                if rnumbners == 1 and "A1" not in taken_areas:
                    ochoice(row_a, 1, "A1")
                elif rnumbners == 2 and "A3" not in taken_areas:
                    ochoice(row_a, 3, "A3")
                elif rnumbners == 3 and "C1" not in taken_areas:
                    ochoice(row_c, 1, "C1")
                elif rnumbners == 4 and "C3" not in taken_areas:
                    ochoice(row_c, 3, "C3")
                loop_breaker += 1
            elif rnumbners > 5 and "B2" not in taken_areas:
                row_b[3] = "o"
                taken_areas.append("B2")
                O = True

    #prints board after enemies move
    printboard()
    print()
