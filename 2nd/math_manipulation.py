import math

def main():
    num1 = int(input("please choose first num\n")) # לקבל מהמשתמש שלושה מסםרים
    num2 = int(input("please choose second num\n"))
    num3 = int(input("please choose third num\n"))
    print(power3Sum(num1, num2, num3)) # הפעלת פונק חזקה

    num4 = int(input("please choose first num\n")) # לקבל מהמשתמש שני מסםרים
    num5 = int(input("please choose second num\n"))
    print(absSqrtAvg(num4, num5)) # הפעלת פונק שורש

#question 3.1
def power3Sum (num1, num2, num3):
    sum = num1**3+num2**3+num3**3 # סכום חזקה שלישית
    return sum

#question 3.2
def absSqrtAvg (num4, num5):
    if num4 < 0: # אם אחד המספרים שלילי = יהפוך לאפס
        num4 = 0
    if num5 < 0:
        num5 = 0
    return (math.sqrt(num4)+math.sqrt(num5))/2 # חישוב שורש באמצעות מחלקת math + חילוק ב2 של הסכום


if __name__ == "__main__": # בדיקה האם קוראים מהמיין או ממחלקה אחרת
    main()

