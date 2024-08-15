import random

num = input("please enter a num-") #לבחור מספר
file_object = open('numbers.text','w') # לאפשר לכתוב בתוך הקובץ

while int(num) > 0: # לולאה לכתיבת מספרים בקובץ
    file_object.write(str(random.randint(1,500))+"\n") #נגריל מספר רנדומלי בין 1-500 ונכתוב בקובץ
    num = int(num) - 1

file_object.close()