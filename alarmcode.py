from playsound import *
import datetime, time

def get_time():
    '''
    user can set the time for alarm by giving hour and minute input
    '''
    #get the params for hr and min from user and convert to time
    hour = -1
    minute = -1
    while not 0 <= hour <= 23 or not 0 <= minute <= 59: #Make sure you got the correct valid input from user
        try:
            hour = int(input('please enter the hour in which you want the alarm? 0-23?'))
            minute = int(input('please enter the minute in which you want the alarm? 0-59?'))
            iptime = datetime.time(hour,minute)
        except:
            print('oops the time is not valid.. please set a valid time')

    #check if the time is past already and set the variable for controling the loop to check for starting alarm
    if iptime < datetime.datetime.now().time():
        checkforalarm = False
        print('Hey the time is already past the alarm time :(')
    else:
        checkforalarm = True

    #main alarm func
    while checkforalarm:
        if iptime == datetime.datetime.now().time():
            for i in range(10):
                playsound('/Users/arunprakash/Downloads/beep-4.wav')
                time.sleep(0.5)
            checkforalarm = False

get_time()

