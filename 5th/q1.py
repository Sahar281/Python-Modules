class Diet: # class
    def __init__(self): # permanent attribute
        self.calories = 1000 #

    def __int__(self, yearOfBirth, gender):# set attributes
        self.yearOfBirth = yearOfBirth
        self.gender = gender

    def eat_more(self): #func to calculate calories when eat more
        self.calories = self.calories + 100

    def eat_less(self): #func to calculate calories when eat less
        self.calories = self.calories - 100

    def get_calories(self): #func to return calories
        return self.calories


person1 = Diet() # create person from diet type
person1.yearOfBirth = 1996 # val for attribute 1
person1.gender = 'female' # val for attribute 2

person2 = Diet() # create person from diet type
person2.yearOfBirth = 2000 # val for attribute 1
person2.gender = 'men' # val for attribute 2

person1.eat_more() #call func 1
person1.eat_more()
person1.eat_more()
person1.eat_more()
person1.eat_more()
print(person1.get_calories()) #call func 3

person2.eat_less() #call func 2
person2.eat_less()
person2.eat_less()
person2.eat_less()
person2.eat_less()
print(person2.get_calories()) #call func 3