import time

t = time.localtime()
current_time = time.strftime("%H", t)
current_time = int(current_time)

def getTime():

    if current_time < 12:
        time = "Good Morning"
    elif current_time < 17:
        time = "Good Afternoon"
    else:
        time = "Good Evening"

    return time
