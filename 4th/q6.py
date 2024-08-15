#q6.1:
file = open("alufa.txt", 'r') #open file to read

win = {} #creat dic
for line in file: #loop
    if line not in win: #line not yet in dic
        if line != 'no game\n': #if line =! no game
            win[line] = 1 #key=line, val=1
    else: #line allready in dic
        win[line]+=1 #val of key(=line) ++
print(win) #print

file.close()

#q6.2:
file = open ('alufa.txt', 'r') #open file to read

dic = {} #creat dic
years = 1953 #start year

for line in file: #loop
    dic[years] = line #key=year, val= line (group who won)
    years+=1 #next year
print(dic)

file.close()

#q6.3
year = int(input("please choose year")) #ask from user choose year
if year == 1955: #if year 1955 - there was no game
    print("no game in this year") #no game
else:
    print("in this year the winner was " + dic[year]) #print the val from dic = group name
    print("she won in total " + str(win[dic[year]]) + " times") #print the val from win = num of wins
