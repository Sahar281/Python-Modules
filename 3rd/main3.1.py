import turtle

table = turtle.Turtle() #creat the game table
table.pencolor('black')

table.penup()
table.goto(0,50) # line
table.pendown()
table.forward(150) # size 150*150

table.penup()
table.goto(0,100) # line
table.pendown()
table.forward(150) # size 150*150

table.penup()
table.goto(50,0) # row
table.left(90)
table.pendown()
table.forward(150) # size 150*150

table.penup()
table.goto(100,0) # row
table.pendown()
table.forward(150) # size 150*150

game = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]] #arr to check the winer

def goToQubeX(): # player X
    print("second player-")
    line = int(input("please choose line")) # get the line
    row = int(input("please choose row")) # get the row
    game[line-1][row-1] = 1 # put in arr check the winer
    
    if line == 1: # go to square
        if row == 1:
            return table.goto(43, 125)
        if row == 2:
            return table.goto(93, 125)
        if row == 3:
            return table.goto(143, 125)
    if line == 2:
        if row == 1:
            return table.goto(43, 75)
        if row == 2:
            return table.goto(93, 75)
        if row == 3:
            return table.goto(143, 75)
    if line == 3:
        if row == 1:
            return table.goto(43, 25)
        if row == 2:
            return table.goto(93, 25)
        if row == 3:
            return table.goto(143, 25)

def goToQubeY(): # player O
    print("first player-")
    line = int(input("please choose line")) # go to line
    row = int(input("please choose row")) # go to row
    game[line-1][row-1] = 2 # put in arr check the winer

    if line == 1:# go to square
        if row == 1:
            return table.goto(0, 105)
        if row == 2:
            return table.goto(52, 105)
        if row == 3:
            return table.goto(102, 105)
    if line == 2:
        if row == 1:
            return table.goto(0, 55)
        if row == 2:
            return table.goto(52, 55)
        if row == 3:
            return table.goto(102, 55)
    if line == 3:
        if row == 1:
            return table.goto(0, 5)
        if row == 2:
            return table.goto(52, 5)
        if row == 3:
            return table.goto(102, 5)

def gameOn():
    x = 0

    while x < 9: # no more than 9 turns
        table.penup()
        goToQubeY() #first player - go to func choose the square
        table.color('blue')
        table.pendown()
        table.right(45) #drow X in the right square
        table.forward(58)
        table.backward(26)
        table.left(90)
        table.forward(26)
        table.backward(58)
        table.penup()
        table.right(45)
        x = x + 1 # count the turn

        #check is there is a winner
        if game[0][0] == game[0][1] == game[0][2] != 0:  # line 1
            table.goto(0, 125)
            table.right(90)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("first player won") # write who won
            return True # if there is winer - finish the game and return true
        if game[1][0] == game[1][1] == game[1][2] != 0:  # line 2
            table.goto(0, 75)
            table.right(90)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("first player won")  # write who won
            return True # if there is winer - finish the game and return true
        if game[2][0] == game[2][1] == game[2][2] != 0:  # line 3
            table.goto(0, 25)
            table.right(90)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("first player won")  # write who won
            return True # if there is winer - finish the game and return true
        if game[0][0] == game[1][0] == game[2][0] != 0:  # row 1
            table.goto(25, 150)
            table.right(180)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("first player won")  # write who won
            return True # if there is winer - finish the game and return true
        if game[0][1] == game[1][1] == game[2][1] != 0:  # row 2
            table.goto(75, 150)
            table.right(180)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("first player won")  # write who won
            return True # if there is winer - finish the game and return true
        if game[0][2] == game[1][2] == game[2][2] != 0:  # row 3
            table.goto(125, 150)
            table.right(180)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("first player won")  # write who won
            return True # if there is winer - finish the game and return true
        if game[0][0] == game[1][1] == game[2][2] != 0:  # slant 1
            table.goto(0, 150)
            table.right(135)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(220) # mark the winning streak
            table.penup()
            print("first player won")  # write who won
            return True # if there is winer - finish the game and return true
        if game[0][2] == game[1][1] == game[2][0] != 0:  # slant 2
            table.goto(150, 150)
            table.left(135)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(220) # mark the winning streak
            table.penup()
            print("first player won")  # write who won
            return True # if there is winer - finish the game and return true
        if x == 9: # if no more turns
            return False # finish the game and return false

        table.penup()
        goToQubeX() # second player - go to func choose the square
        table.color('red')
        table.pendown()
        table.circle(20) # drow circle in the right square
        table.penup()
        x = x+1 # count the turn

        if game[0][0] == game[0][1] == game[0][2] != 0:  # line 1
           table.goto(0, 125)
           table.right(90)
           table.color('black')
           table.width(3)
           table.pendown()
           table.forward(150) # mark the winning streak
           table.penup()
           print("second player won") # write who won
           return True # if there is winer - finish the game and return true
        if game[1][0] == game[1][1] == game[1][2] != 0:  # line 2
            table.goto(0, 75)
            table.right(90)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("second player won") # write who won
            return True # if there is winer - finish the game and return true
        if game[2][0] == game[2][1] == game[2][2] != 0:  # line 3
            table.goto(0, 25)
            table.right(90)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("second player won") # write who won
            return True # if there is winer - finish the game and return true
        if game[0][0] == game[1][0] == game[2][0] != 0:  # row 1
            table.goto(25, 150)
            table.right(180)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("second player won") # write who won
            return True # if there is winer - finish the game and return true
        if game[0][1] == game[1][1] == game[2][1] != 0:  # row 2
            table.goto(75, 150)
            table.right(180)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("second player won") # write who won
            return True # if there is winer - finish the game and return true
        if game[0][2] == game[1][2] == game[2][2] != 0:  # row 3
            table.goto(125, 150)
            table.right(180)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(150) # mark the winning streak
            table.penup()
            print("second player won") # write who won
            return True # if there is winer - finish the game and return true
        if game[0][0] == game[1][1] == game[2][2] != 0:  # slant 1
            table.goto(0, 150)
            table.right(135)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(220) # mark the winning streak
            table.penup()
            print("second player won") # write who won
            return True # if there is winer - finish the game and return true
        if game[0][2] == game[1][1] == game[2][0] != 0:  # slant 2
            table.goto(150, 150)
            table.left(135)
            table.color('black')
            table.width(3)
            table.pendown()
            table.forward(220) # mark the winning streak
            table.penup()
            print("second player won") # write who won
            return True # if there is winer - finish the game and return true


res = gameOn()
if res == False: # if there is no winer
    print("tie!") # its a tie

turtle.done()