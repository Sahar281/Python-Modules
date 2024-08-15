#1
wholeNum= int(input ("please enter num \n "))
#recive a 3 digits num from user
print (int(wholeNum/100),(int (wholeNum/10%10)),(int(wholeNum%10)),sep="@",end="! \n \n ")
print ("bye")
#print third digits one by one with '@' as seperation ending with '!' going down two lines then printing bye

#2
numOfWoman= int(input("plese enter num of wonan in the class: \n"))
#recive num of women in class frome user
numOfMen= int(input("please enter num of man in the class: \n"))
#recive num of man in class from user
totalClass= int(numOfWoman+numOfMen)
#sum man & women to whole class
print (numOfWoman/totalClass*100, "% woman frome class")
#print calculatation of the percentage of woman from class
print(numOfMen/totalClass*100,"% men from class")
#print calculatation of the percentage of man from class

#3
firstNum=int(input("please enter first num: \n"))
secondNum=int(input("please enter second num: \n"))
#recive 2 nums frome user
if (firstNum%secondNum==0):
    print("first div in second")
else:
    print("first dosent div in second")

if(secondNum%firstNum==0):
    print("second div in first")
else:
    print("second dosent div in first")

#4
grade= float(input("pleasse enter grade: \n"))
#asking for grade frome user
if grade>100 or grade<0:
    print("invalide grade ")
#if grade is between 90 and 100 A
elif grade<=100 and grade>=90:
    grade="A"
#if grade is between 80 and 90 p[rint gtade B
elif grade<90 and grade>=80:
    grade="B"
#if grade is not between 70 and 80 print grade C
elif grade<80 and grade>=70:
    grade="C";
else: grade="D"
#if grade is between 0 and 70 print grade D

#5
carSpeed=float(input("please insert car speed: \n"))
#user insert car velocity
numOfHoures=int(input("please insert deiving time in houres"))
#user insert houres of driving
i=0
# index
while i<=numOfHoures:
#while loop as long as the index smaller then numOfHourse
    print (i,"houres ",i*carSpeed,"km\p")
#printing the specific houre and the path the car coverd
    i+=1
#index adding one

#6
num=int(input("please insert num between 1 and 100 \n"))
#user insert num between 1 and 100
for x in range(0,101,num):
#for loop
    print(x)

#7
number=input("please insert number: \n")
#user insert num as String
d=input("plese entre num between 0-9 called d \n")
#user insert ndigit as String
for x in number:
#for loop goes on every digit in number and prints digit when equals to digit d
    if x==d:
        print(d)
print("end")

#8
rowsColls=int(input("please enter size"))
#user enter size of triangle
for r in range(1,rowsColls+1):
#for loop between 1 and rowsColls full size
    for c in range(r):
#for loop between 0 and size of r
          print("*", end="")
#prints "*" and changing the end from default to nothing
    print()