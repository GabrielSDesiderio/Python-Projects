days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',4: 'Friday', 5: 'Saturday', 6: 'Sunday'}



def add_time(init,interval,weekday1 = None):
    import datetime
    time_init = datetime.datetime.strptime(init, "%I:%M %p")
    if weekday1 != None:
        weekday1 = weekday1.title()
        while days[time_init.weekday()] != weekday1:
            time_init += datetime.timedelta(days=1)
    
    tm1 = interval.split(':')
    tm1 = list(map(int, tm1)) 
    tm2 = datetime.timedelta(hours=tm1[0], minutes=tm1[1])
    tm3 = time_init + tm2
    time_final = tm3.strftime("%I:%M %p")
    
    if (time_final[0] == "0"):
        time_final = time_final[1:]

    next_day=''
    if (tm3.day-time_init.day == 1):
        next_day = ' (next day)'
    elif (tm3.day-time_init.day > 1):
        next_day = ' (' + str(tm3.day-time_init.day) + ' days later)'

    finalday = ''
    if weekday1 != None:
        finalday = ', ' + tm3.strftime('%A')

    new_time = time_final + finalday + next_day
    return new_time;