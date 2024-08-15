first = 10 # הגדרת מדרגות מס
second = 14
third = 21
fourth = 31

def calc_tax (salary): # פונקציה שמחשבת מס על משכורת
    if salary <= 5220:
        newSalary = salary*(100-first)/100 # חישוב משכורת חדשה עם מס 1
    elif salary <= 8920:
        newSalary = (5220*(100-first)/100) + (salary-5220)*(100-second)/100 # חישוב משכורת חדשה עם שתי מדרגות מס
    elif salary <= 13860:
        newSalary = (5220 * (100 - first) / 100) + 3700 * (100 - second) / 100 + (salary - 8920) * (100 - third) / 100 # חישוב משכורת חדשה עם שלוש מדרגות מס
    else:
        newSalary = (5220 * (100 - first) / 100) + 3700 * (100 - second) / 100 + 4940*(100-third)/100 + (salary-13860)*(100-fourth)/100 # חישוב משכורת חדשה עם ארבע מדרגות מס

    return salary - newSalary # מחזירים את המס שמשלמים סה"כ

salary = int(input("please enter your salary\n")) # מבקשים מהמשתמש שיזין משכורת
print("you are going to pay-", calc_tax(salary)," tax!" )
