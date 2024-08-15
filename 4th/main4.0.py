#q1.1
file = open("imagine.txt", "r") #open file to read
lines = file.readlines() #arr of lines

file = open("imagine.txt", "r") #open file to read
imagine = file.read() #
words = imagine.split() #split to arr of words

print("the average number of words per lines is:" + str(len(words)/len(lines))) #lenth : lent = ave

file.close()

#q1.2
file = open("imagine.txt", "r") #open file to read

x = 0
for line in file: #loop on the files lines
    newLine = line.split() #split the line to words
    print(newLine[len(newLine)-1]) #print the last word
file.close()

#q2
name = input("please write the file name") #ask from user to choose file
file = open(name+'.txt', "r") #open file to read
file1 = file.read()

countD = 0 #counter
for char in file1: #loop
    if char.isdigit(): # if char is digit
        countD = countD + 1 #counter++
print(countD) #print counter - num of digits in file

countLow = 0 #counter
for char in file1: #loop
    if char.islower(): # if char is low leter
        countLow = countLow + 1 #counter++
print(countLow) #print counter - num of low leters in file

countUp = 0 #counter
for char in file1:  #loop
    if char.isupper(): # if char is big leter
        countUp = countUp + 1 #counter++
print(countUp) #print counter - num of big leters in file

countS = 0 #counter
for char in file1: #loop
    if char.isspace(): # if char is space
        countS = countS + 1 #counter++
print(countS) #print counter - num of spaces in file

file.close()

#q3
string = input("please write a string-") #ask from user to write a string
Common = max(set(string), key=string.count) #set on string , count how many time each char apper, show tha max

print(Common)#print most common

