def convert_km_to_miles(kilometers=1):  # פונק קולטת מס ק"מ - אם לא מקבלת קלט 1 ברירת מחדל
    miles = kilometers * 0.6214  # ממירה למייל

    return miles

numKm = int(input("please write km num\n"))
if numKm >= 0:  # אם חיובי
    print(convert_km_to_miles(numKm))  # מחשבת ומדפיסה מייל
else:  # אם שלילי
    print(convert_km_to_miles())  # מחשבת ומדפיסה מייל ללא ערך (1 ברירת מחדל)
