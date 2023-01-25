def add_time(start, duration, day = None):

    # reference list for days of the week
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    # split the time into time and AM or PM
    start = start.split(" ")

    # split start time into hours and minutes
    start_split = start[0].split(":")

    # set variables for hours, minutes, AM/PM string
    start_hour = int(start_split[0])
    start_min = int(start_split[1])
    start_period = start[1]
    new_day = ""

    # set period change to false at start
    change_period = False

    # similarly split the timer duration into min and hours
    duration_split = duration.split(":")

    duration_hour = int(duration_split[0])
    duration_min = int(duration_split[1])

    # add duration to start time
    new_min = start_min + duration_min
    new_hour = start_hour + duration_hour

    # if the hour mark is breached, add another hour to the final time
    # and reduce minutes by 60 to account

    # print(new_min)
    if new_min >= 60:
        new_hour += 1
        # check if AM/PM was changed thru this process
        if new_hour >= 12 and start_hour < 12:
            change_period = True
        new_min -= 60
    else:
        # if added minutes didn't change AM/PM check for changes due to hour
        if (new_hour % 24) >= 12 and start_hour < 12:
            change_period = True

    # print(change_period)

    # add a zero to minutes if less than 10
    if new_min < 10:
        new_min = "0" + str(new_min)

    # change AM/PM if boolean is true
    if change_period is True:
            if start_period == "PM":
                new_period = "AM"
            elif start_period == "AM":
                new_period = "PM"
    else: # if change period is false,keep original period
        new_period = start_period

    periods_past = int(new_hour/12)
    # print(periods_past)

    days_past = periods_past/2
    # print(days_past)

    # reduce high hours to 12 or less
    if periods_past >= 1:
        new_hour -= periods_past * 12

    # don't print midnight as 0:00, instead as 12:00
    if new_hour == 0:
        new_hour = 12

    day_indic = ""
    day_change = False

    # print(change_period)
    if change_period is True:
        if start_period == "PM" and (periods_past % 2) != 0:
            day_indic += " (next day)"
            day_change = True
        elif start_period == "AM" and (periods_past % 2) == 0:
            day_indic += " (next day)"
            day_change = True


    if day is not None:
        for i in range(len(weekdays)):
            if day.lower() == weekdays[i].lower():
                index = i
                # print(index)
                # print(day_change)
                if day_change is True:
                    index += 1
        new_day = ", " + weekdays[(index + int(days_past)) % 7]

    if days_past > 1:
        for i in range(int(days_past)+1):
            day_indic = " (" + str(i+1) + " days later)"

    if days_past == 1:
        day_indic = " (next day)"

    # create output string
    new_time = str(new_hour) + ':' + str(new_min) + " " + new_period + new_day + day_indic

    # print(days_past)

    # print(index+days_past.__ceil__())

    return new_time

# print(add_time("2:59 AM", "24:00", "saturDay"))

'''
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
'''