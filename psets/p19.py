import calendar

def sundays():
    # sundays = 0
    calendar.setfirstweekday(6) #sets first day to sunday 
    s = 0 
    for y in range(1901, 2001):
        for m in range (1, 13):
            year_month = calendar.monthcalendar(y,m)
            if year_month[0][0]:
                s += 1
    print (s)


if __name__ == "__main__":
    sundays()

