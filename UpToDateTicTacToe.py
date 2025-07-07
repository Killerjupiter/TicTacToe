#By Bealex my discord is bealex if you need me


def yxrow(a,): 
    b = "|"
    return [a, " ", b, " ", b, " "]


#Game Board could of probably been a dictionary
Num_row = ("   1   2   3")
row_a = yxrow("A")
border_a = ("   ----------")
row_b = yxrow("B")
border_b = ("   ----------")
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
rnumbers = []
rnumber_used = []


#first print of board at clean slate
print("This is TicTacToe, to play type row A, B, or C " 
    "and than select the number on that row 1, 2, or 3")

def printboard():
    print(Num_row)
    print(" ".join(row_a))
    print(border_a)
    print(" ".join(row_b))
    print(border_b)
    print(" ".join(row_c))
    print("  ")
    print("  ")
    print("  ")

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
            
            


    #handles palyer board placement
    taken_areas.append(player_1L + player_1N)
    def yx_move(inputy, row): #Converts input into cordinates to put into the board using the x and y values
        if y == inputy:
            x_move(1, 1, row)
            x_move(2, 3, row)
            x_move(3, 5, row)
    def x_move(inputx, convert_position, row): #takes x and given y cordinates and places the X on the board in that positon
            if x == (str(inputx)):
                row[convert_position] = "x" 
    
    yx_move("A", row_a)
    yx_move("B", row_b)
    yx_move("C", row_c)
    

    #test print
    printboard()


    print(taken_areas) #Make sure to delete when done
    

    #Probably win conditions
    if row_a[1] == "x":
        if row_a[3] == "x":
            if row_a[5] == "x":
                print("YOU WIN!!! Do you want to play again?")
                row_a[1] = "W"
                row_a[3] = "W"
                row_a[5] = "W"
                pwin = True
                restart = input("Y for YES and N for NO:  ").capitalize()
                if restart == "Y":
                    taken_areas = []
                    pwin = False


    #Hopefully O's algorithm

    while O == None:
        player_1L = None
        player_1N = None
        if "B2" not in taken_areas:
            row_b[3] = "o"
            taken_areas.append("B2")
            O = True
        elif "B2" in taken_areas:
            if "A2" not in taken_areas:
                row_a[3] = "o"
                taken_areas.append("A2")
                O = True
            elif "C1" not in taken_areas:
                row_c[3] = "o"
                taken_areas.append("C2")
                O = True
        
        elif "B2" in taken_areas:
            if "B3" not in taken_areas:
                row_b[5] = "o"
                taken_areas.append("B3")
                O = True

    #test print
    printboard()
