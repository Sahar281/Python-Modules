class nba: # class
    def __init__(self, name, nickName, team, position): # set attributes
        self.name = name
        self.nickName = nickName
        self.team = team
        self.position = position


player1 = nba('Julius Erving','Dr. J', 'Brooklyn Nets', 'Small forward') # create player 1 from nba type
player2 = nba('Kobe Bryant', 'Black Mamba', 'Los Angeles Lakers', 'Shooting guard') # create player 2 from nba type
player3 = nba('Michael Jordan', 'His Airness', 'Chicago Bulls', 'Shooting guard' ) # create player 3 from nba type

print(vars(player1)) #print
print(vars(player2))
print(vars(player3))