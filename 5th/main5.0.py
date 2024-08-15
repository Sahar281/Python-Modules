#q4:
months = {} #creat dic of month and days
months[1] = 31
months[2] = 28
months[3] = 31
months[4] = 30
months[5] = 31
months[6] = 30
months[7] = 31
months[8] = 31
months[9] = 30
months[10] = 31
months[11] = 30
months[12] = 31


def daysInMonth(n):
    if months[n] == 1: # stop term
        print(months[n])
        return

    print(months[n]) #print days in month
    months[n] = months[n] - 1 #print days in month-1
    daysInMonth(n) #call again the func

daysInMonth(2) # call the func

#q5:
sickPeople = (100, 200, 50, 400, 330, 120, 1700, 800, 130, 900, 660, 240) #tuple of sick people

def lowerMonth(tuple):
    if len(tuple) == 2: # stop term when only 2 values in tuple
        if tuple[0] < tuple[1]: # return the lowest
            return tuple[0]
        else:
            return tuple[1]

    else:
        x = lowerMonth(tuple[1:]) #call the func again with tuple from second val
        if tuple[0] < x: #if first val < tuple from second val
            return tuple[0] # return the lowest
        else:
            return x # return the lowest

print(lowerMonth(sickPeople)) # call the func

#q6:
def lighTheCandle(n):
    if n == 0: # stop term when no candles
        return 0
    return n+lighTheCandle(n-1)+1 #call the func again with lower amount+ count amount of candles + shamash candle

print(lighTheCandle(8)) # call the func
