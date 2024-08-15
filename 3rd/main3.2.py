# question 1

list = [] # creat list
for x in range(10): # loop to add inputs to the list
    num = input("please choose number-") # get the input from user
    list.append(num) #add to list

size = len(list) # list size, print all questions:
print(list[0:3])
print(list[size - 3:size])
print(list[1:size])
print(list[0:-1])
list.reverse()
print(list)
list.reverse() #return to original list

# question 2.1
numbers = [] # create list
for x in range(10): # loop to add inputs to the list
    number = int(input("please choose number-")) # get the input from user
    numbers.append(number) #add to list

even = odd = 0 # counter

for x in numbers:
    if x % 2 == 0: #check if even
        even = even + 1 #countr ++
    else: #its odd
        odd = odd + 1 #other countr ++

if odd > even: # check which counter is higer
    print("Odd")
elif even > odd:
    print("Even")
else:
    print("Same")

# question 2.2
numbers.sort() # use sort func
print(numbers)
numbers.sort(reverse=True) # reverse list + use sort func
print(numbers)


# question 3.1
def list_to_3(oLists): # func get list
    size1 = len(oLists) # check the zise of original list

    if size1 % 3 != 0: # if size not divide by 3
        if size1 % 3 == 1: # if one left over
            oLists.append(0) # add 2 places with 0 to original list
            oLists.append(0)
        if size1 % 3 == 2: # if 2 left over
            oLists.append(0) #add 1 place with 0 to original list

    oLists.append("end") # add the word in the end of the original list
    nSize = len(oLists) # the current size of the original lise
    nNsize = (nSize - 1) / 3 # calculate the size of the *new* list
    list = [None] * int(nNsize) # creat new list with the new size

    n = 0
    i = 0

    while 'end' not in str(oLists[n]): #while original list didnt finish
        list[i] = oLists[n:n + 3] #first place in *new* list <- 3 places in *original* list
        if n != nSize: # if original list didnt finish
            n = n + 3 # jump in 3 index
        if i < nNsize: # if new list didnt finish
            i = i + 1 # jump to next index

    return list # return *new* list


def main():
    list1 = [] # create list

    num = 1
    while num != 0: # get numbers from user until 0
        num = float(input("please add number to the list-"))
        if num != 0:
            list1.append(num)

    print(list_to_3(list1)) # use func to creat new list


if __name__ == "__main__": # main
    main()
