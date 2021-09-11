# Pomodoro Timer
# Python 3.9.5 on Mac

import time
import tkinter
from tkinter import *
from tkinter import messagebox
import os

f = ('Courier', 24)

# Create window size, orientation on screen, and background color
ws = Tk()
ws.geometry('300x250+0+700')
ws.title('Pomodoro Timer')
ws.config(bg='#300')

minute = StringVar()
second = StringVar()

minute.set("00")
second.set("00")

mins_tf = Entry(
    ws,
    width = 3,
    font = f,
    textvariable = minute)

mins_tf.place(x = 98, y = 30)

sec_tf = Entry(
    ws,
    width = 3,
    font = f,
    textvariable = second)

sec_tf.place(x = 150, y = 30)

# Create a ticking state that would continue
tick = True

# Create functions for application
# Create ticking function
def ticking():
    total_seconds = int(minute.get()) * 60 + int(second.get())
    while total_seconds > -1 and tick == True:
        mins, secs = divmod(total_seconds,60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        ws.update()
        time.sleep(1)
        if (total_seconds == 0):
            play_sound("notification_sound.mp3")
            messagebox.showinfo("", "Time's Up.")
        total_seconds -= 1

# Create Pomodoro button function
def pomodoroCountdown():
    global tick
    tick = True
    minute.set("25")
    second.set("00")
    ticking()

# Create break button function
def breakCountdown():
    minute.set("05")
    second.set("00")
    global tick
    tick = True
    ticking()

# Create start button function
def startCountdown():
    global tick
    tick = True
    ticking()

# Create stop button function
def stopCountdown():
    global tick 
    tick = False

# Create soundfile function
def play_sound(sound_file, time = 0): # Time is in sec, how many seconds before time file repeats?, if no time, it doesn't repeat
    os.system("afplay {}&".format(sound_file))
    
# Creating the Button GUI
# Create POMODORO button that begins countdown for 25 mins
pomodoro_btn = Button(
    ws,
    text='POMODORO',
    bd='0',
    command = pomodoroCountdown
    )

pomodoro_btn.place(x = 102, y = 120)

# Create BREAK button that begins countdown for 5 mins
break_btn = Button(
    ws,
    text='BREAK',
    bd='0',
    command = breakCountdown
    )

break_btn.place(x = 120, y = 145)

# Create START button that resumes countdown if countdown is stopped by STOP button
start_btn = Button(
    ws,
    text='START',
    bd='0',
    command = startCountdown
    )

start_btn.place(x = 120, y = 170)

#Create STOP button that stops countdown
stop_btn = Button(
    ws,
    text="STOP",
    bd='0',
    command = stopCountdown)

stop_btn.place(x = 123, y = 195)


ws.mainloop()
        
