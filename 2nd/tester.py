#question 3.3
import math_manipulation

def main():
    num1 = int(input("please choose first num\n"))  # לקבל מהמשתמש שלושה מסםרים
    num2 = int(input("please choose second num\n"))
    num3 = int(input("please choose third num\n"))
    print(math_manipulation.power3Sum(num1, num2, num3))  # קריאה לפונק ממחלקת math_manipulation

    num4 = int(input("please choose first num\n"))   # לקבל מהמשתמש שני מסםרים
    num5 = int(input("please choose second num\n"))
    print(math_manipulation.absSqrtAvg(num4, num5)) # קריאה לפונק ממחלקת math_manipulation

main()
