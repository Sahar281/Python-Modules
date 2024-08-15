file1 = input("please choose first file") #ask from user choose first file
file2 = input("please choose second file") #ask from user choose second file

firstFile = open(file1+'.txt', "r") #open file to read
secondFile = open(file2+'.txt', "r") #open file to read

#q5.1:
data1 = firstFile.read()
words1 = data1.split() #first file is list of words
set1 = set(words1) #make list as set - remove duplicate
print(set1) #print

data2 = secondFile.read()
words2 = data2.split() #second file is list of words
set2 = set(words2) #make list as set - remove duplicate
print(set2) #print

#q5.2:
final_list = list(set(set1) | set(set2)) # combination of 2 sets - words in 2 files - no duplicate
print(final_list)

#q5.3:
onlyFirst = list(set(set1) - set(set2)) # combination of 2 sets - words in first file and not in second file
print(onlyFirst)

#q5.4:
onlySecond = list(set(set2) - set(set1)) # combination of 2 sets - words in second file and not in first file
print(onlySecond)

#q5.5:
final_list1 = list(set(set1) - set(set2) | set(set2) - set(set1)) # combination of 2 sets - words in first file and not in second + words in second file and not in first file
print(final_list1)

firstFile.close()
secondFile.close()