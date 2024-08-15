import math

text_file = open("Shapes.txt", "r") # לאפשר לקרוא את הקובץ
lines = text_file.readlines() # להפוך את הקובץ למערך
lines.append('end') # לשים בתא האחרון במערך מילת סיום
lines[len(lines)-2] = lines[len(lines)-2] + '\n' # להוסיף לערך בתא האחרון ירידת שורה

def isCircle(lines, x): #פונקצית מעגל
    try: # בדיקה
        temp1 = float(lines[x + 1]) ** 2 * 3.14  # שטח
        temp2 = 2 * float(lines[x + 1]) * 3.14  # היקף

        if float(lines[x + 1]) > 0: # אם הרדיוס חיובי
            x = x + 2
            lines.insert(x, str(temp1)+'\n') # נוסיף לתא במערך את השטח
            x = x + 1
            lines.insert(x, str(temp2)+'\n') # נוסיף לתא במערך את ההיקף
        else:
            x = x + 2
            raise ValueError("radios must to be bigger than 0 !"+'\n') # נשלח חריגה

    except ValueError as ve:
        print(ve)
        lines.insert(x, (ve)) # נדפיס את החריגה

    return lines, x + 1 # הפונקציה מחזירה את המערך ואת הX הנוכחי

def isTriangle(lines, x):  #פונקצית משולש
    try: # בדיקה
        zela = math.sqrt(float(lines[x + 1]) * 0.5 ** 2 + float(lines[x + 2]) ** 2)  # חישוב צלע
        temp1 = float(lines[x + 1]) * float(lines[x + 2]) / 2  # חישוב שטח
        temp2 = zela * 2 + float(lines[x + 1])  # חישוב היקף

        if float(lines[x + 1]) > 0: # אם בסיס חיוב
            if float(lines[x + 1]) % 1 == 0: # אם בסיס שלם
                if float(lines[x + 2]) > 0: # אם גובה חיובי
                    x = x + 3
                    lines.insert(x, str(temp1)+'\n') # נוסיף לתא במערך את השטח
                    x = x + 1
                    lines.insert(x, str(temp2)+'\n') # נוסיף לתא במערך את ההיקף
                else:
                    x = x + 3
                    raise ValueError("high must to be bigger than 0 !"+'\n') # חריגה
            else:
                x = x + 3
                raise ValueError("basis must to be an integer !"+'\n') # חריגה
        else:
            x = x + 3
            raise ValueError("basis must to be bigger than 0 !"+'\n') # חריגה

    except ValueError as ve:
        print(ve)
        lines.insert(x, (ve)) # נדפיס את החריגה

    return lines, x + 1 # הפונקציה מחזירה


def isRectangle(lines, x): # פונקצית מלבן
    try:
        temp1 = float(lines[x + 1]) * float(lines[x + 2]) #שטח
        temp2 = 2 * float(lines[x + 1]) + 2 * float(lines[x + 2]) # היקף

        if float(lines[x + 1]) > 0: # אם צלע 1 חיובי
            if float(lines[x + 1]) % 1 == 0: # אם הצלע 1 מס שלם
                if float(lines[x + 2]) > 0: # אם צלע 2 חיובית
                    if float(lines[x + 2]) % 1 == 0: # אם צלע 2 מס שלם
                        x = x + 3
                        lines.insert(x, str(temp1)+'\n') # נוסיף לתא במערך את השטח
                        x = x + 1
                        lines.insert(x, str(temp2)+'\n') # נוסיף לתא במערך את ההיקף
                    else:
                        x = x + 3
                        raise ValueError("zela must to be an integer !"+'\n') # חריגה
                else:
                    x = x + 3
                    raise ValueError("zela must to be be bigger than 0 !"+'\n') # חריגה
            else:
                x = x + 3
                raise ValueError("zela must to be be an integer !"+'\n') #חריגה
        else:
            x = x + 3
            raise ValueError("zela must to be be bigger than 0 !"+'\n') # חריגה

    except ValueError as ve:
        print(ve)
        lines.insert(x, (ve)) # נדפיס את החריגה

    return lines, x + 1 # הפונקציה מחזירה

x = 0
while 'end' != lines[x]: # לולאה שעוברת על המערך עד שמגיעים לתא שמכיל מילת סיום
    if isinstance(lines[x], str): # כל עוד יש בתא סטרינג
        if 'CIRCLE' in lines[x].upper():  # אם זה מעגל
            lines, x = isCircle(lines, x)

        if 'TRIANGLE' in lines[x].upper():  # אם זה משולש
            lines, x = isTriangle(lines, x)

        if 'RECTANGLE' in lines[x].upper(): # אם זה מלבן
            lines, x = isRectangle(lines, x)

lines.remove('end') # נמחק את התא האחרון עם מילת הסיום

question = input("do you want to add a shape? (yes/no)\n") # נשאל את המשתמש אם הוא רוצה להזין צורות
while question.upper() == 'YES': #אם כתב שכן
    try:
        shape = input("please choose shape:\n")
        if (shape.upper() != 'CIRCLE' and shape.upper() != 'TRIANGLE' and shape.upper() != 'RECTANGLE'):
            raise ValueError("shape must to be circle or triangle or rectangle")  # # אם הוזן צורה שונה מהשלוש
    except ValueError as err:
        print(err)
    else:
        if (shape.upper() == 'CIRCLE'): # אם מעגל
            lines.append('CIRCLE \n')
            try:
                radios = float(input("please choose radios:\n")) # נקלוט רדיוס
                lines.append(str(radios)+'\n')
                lines, x = isCircle(lines, x)
            except ValueError: # אם הוזן ערך שאינו מספר
                print("you can only enter a number")
        if (shape.upper() == 'TRIANGLE'): # אם משולש
            lines.append('TRIANGLE \n')
            try:
                high = float(input("please choose high:\n")) # נקלוט גובה
                lines.append(str(high)+'\n')
                basis = float(input("please choose basis:\n")) # נקלוט בסיס
                lines.append(str(basis)+'\n')
                lines, x = isTriangle(lines, x)
            except ValueError as ve: # אם הוזן ערך שאינו מספר
                print("yoy can only enter a number")
        if (shape.upper() == 'RECTANGLE'): # אם מלבן
            lines.append('RECTANGLE \n')
            try:
                zela1 = float(input("please choose first zela:\n")) # נקלוט צלע 1
                lines.append(str(zela1)+'\n')
                zela2 = float(input("please choose second zela:\n")) # נקלוט צלע 2
                lines.append(str(zela2)+'\n')
                lines, x = isRectangle(lines, x)
            except ValueError as ve: # אם הוזן ערך שאינו מספר
                print("yoy can only enter a number")

        question = input("do you want to add more shape? (yes/no)\n")

text_file = open("Shapes.txt", "w") # נאפשר כתיבה לקובץ

for x in lines: # לולאה שמעתיקה את המערך לקובץ
    text_file.write(str(x))

print(lines)