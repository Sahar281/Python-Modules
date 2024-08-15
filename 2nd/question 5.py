#לולאה לקליטת ערכים של 10 סטודנטים
def main():
    for student in range (1,11):
        input("insert name \n")
        get_grade()

#לולאה לבדיקת תקינות הציון
def get_grade():
    while(True):
        try:
            value= float(input("please enter grade \n"))
            if value>100.0 or value<0.0:
                raise ValueError("grade not in a valied range \n please try again")
            if value % 1 != 0:
                raise ValueError("grade is not a whole num \n please try again")
            break
        except ValueError as err:
            print(err)

    return value

#חריגה אם הציון לא בין 0-100
def err():
    value = float(input("please enter grade \n"))


main()