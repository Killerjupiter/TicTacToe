#By Bealex my discord is bealex if you need me

#imported module for random number generation
from random import randint, choice

#fuction controls row size, thinking of expanding upon functionality for other stuff
def yxrow(a,): 
    b = "|"
    return [a, " ", b, " ", b, " "]


#Game Board could of probably been a dictionary
Num_row = ("   1   2   3")
row_a = yxrow("A")
border_a = (" -----------")
row_b = yxrow("B")
border_b = (" -----------")
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
xy1 = None
y1 = None
x1 = None

#Below handles player Input
player_1L = None
player_1N = None
pwin = False

#Enemy variables
O = None
ewin = False

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

def winrow(a):
    a[1] = "W"
    a[3] = "W"
    a[5] = "W"

def winner():
    winrow(row_a)
    winrow(row_b)
    winrow(row_c)

def printboard():
    print(Num_row)
    print(" ".join(row_a))
    print(border_a)
    print(" ".join(row_b))
    print(border_b)
    print(" ".join(row_c))
    print("  ")
    print("  ")
    

#first print of board at clean slate
print("This is TicTacToe, to play type row A, B, or C " 
    "and than select the number on that row 1, 2, or 3")

#prints clean board
printboard() 

#Game loop
while pwin == False:

    #Decides position
    while player_1L not in InputsL or player_1N not in InputsN or player_1L + player_1N in taken_areas:
        O = None
        player_1LL = input("Input Letter and Number:").capitalize()
        xy1 = list(player_1LL)
        player_1L = xy1[0]
        player_1N = xy1[1]
        if player_1L + player_1N in taken_areas:
            print("That area is already taken")
        if player_1L + player_1N not in taken_areas:
            if player_1L in InputsL:
                y = player_1L
            if player_1L not in InputsL:
                print("Not a valid option")
            if player_1N in InputsN:
                x = player_1N
            if player_1N not in InputsN:
                print("Not a valid option")
            
            


    #handles palyer board placement uses def yx_move and def x_move at the top of the project
    taken_areas.append(player_1L + player_1N)
    yx_move("A", row_a)
    yx_move("B", row_b)
    yx_move("C", row_c)
    
    #prints board after players move
    printboard()

    #Probably win conditions
    if row_a[1] == "x":
        if row_a[3] == "x":
            if row_a[5] == "x":
                print("YOU WIN!!! Do you want to play again?")
                winner()
                pwin = True
                restart = input("Y for YES and N for NO:  ").capitalize()
                if restart == "Y":
                    taken_areas = []
                    pwin = False

    #Hopefully O's algorithm

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


    #Enemy algorithm honestly don't know if it fully works
    while O == None:
        player_1L = None
        player_1N = None
        rnumbners = randint(1, 3)
        if "B2" not in taken_areas:
            if rnumbners != 1:
                 if "A1" and "A3" and"C1" and "C3" not in taken_areas:
                    rnumbners = randint(1, 4)
                    if rnumbners == 1 and "A1" not in taken_areas:
                        ochoice(row_a, 1, "A1")

                    if rnumbners == 2 and "A3" not in taken_areas:
                        ochoice(row_a, 3, "A3")

                    if rnumbners == 3 and "C1" not in taken_areas:
                        ochoice(row_c, 1, "C1")

                    if rnumbners == 4 and "C3" not in taken_areas:
                        ochoice(row_c, 3, "C3")

                    elif "A1" not in taken_areas and "C3" not in taken_areas:
                        ochoice(row_a, 1, "A1")

                    elif "C1" not in taken_areas and "A1" not in taken_areas:
                        ochoice(row_c, 1, "C1")

                    elif "C3" not in taken_areas:
                        ochoice(row_c, 3, "C3")
                     
                    elif "A3" not in taken_areas:
                        ochoice(row_a, 3, "A3")  
            else:
                row_b[3] = "o"
                taken_areas.append("B2")
                O = True
        elif "B2" in taken_areas:
            if row_a[3] not in taken_areas and row_a[1] == "o" and row_a[5] == "o":
                ochoice(row_a, 2, "A2")
            elif row_c[3] not in taken_areas and row_c[1] == "o" and row_c[5] == "o":
                ochoice(row_c, 2, "C2")
            elif row_b[1] not in taken_areas and row_a[1] == "o" and row_c[1] == "o":
                ochoice(row_b, 1, "B1")
            elif row_b[5] not in taken_areas and row_a[5] == "o" and row_c[5] == "o":
                ochoice(row_b, 3, "B3")
            elif all(x not in taken_areas for x in ["A1", "A3", "C1", "C3"]):
                rnumbners = randint(1, 4)
                if rnumbners == 1:
                    ochoice(row_a, 1, "A1")
                if rnumbners == 2:
                    ochoice(row_a, 3, "A3")
                if rnumbners == 3:
                    ochoice(row_c, 1, "C1")
                if rnumbners == 4:
                    ochoice(row_c, 3, "C3")
            elif "A1" not in taken_areas and "C3" not in taken_areas:
                ochoice(row_a, 1, "A1")
            elif all(x not in taken_areas for x in ["C1", "A1"]):
                ochoice(row_c, 1, "C1")
            elif "C3" not in taken_areas:
                ochoice(row_c, 3, "C3")
            elif "A3" not in taken_areas:
                ochoice(row_a, 3, "A3")
        elif all(x in taken_areas for x in ["A1", "A3", "C1", "C3"]):
            loop_breaker = 0
            while O is None and loop_breaker < 10:
                rnumbners = randint(1, 4)
                if rnumbners == 1 and "A2" not in taken_areas:
                    ochoice(row_a, 2, "A2")
                elif rnumbners == 2 and "B1" not in taken_areas:
                    ochoice(row_b, 1, "B1")
                elif rnumbners == 3 and "B3" not in taken_areas:
                    ochoice(row_b, 3, "B3")
                elif rnumbners == 4 and "C2" not in taken_areas:
                    ochoice(row_c, 2, "C2")
                loop_breaker += 1
            if loop_breaker >= 10:
                print("Tie, no more moves available")
    #prints board after enemies move
    printboard()
