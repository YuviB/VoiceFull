#import libraries
import time
import tkinter
from tkinter import *
from tkinter import messagebox

# creating Tk window
root = Tk()

# set geometry of tk window
root.geometry("300x250")

#Title of window
root.title("Atlas Timer System")

# creating and assigning variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# set default timer to 00
hour.set("00")
minute.set("00")
second.set("00")

# using Entry to act as input and create for hours entry

Headline = Text(root, font=("Arial", 18, ""))
Headline.place(x=100)


hour_entry = Entry(root, width=3, font=("Arial", 18, ""),
                  textvariable=hour)
#Place Entry box in Awndow
hour_entry.place(x=80, y=50)

minute_entry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minute_entry.place(x=130, y=50)

second_entry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second)
second_entry.place(x=180, y=50)


def submit():
    try:
        # the input provided by the user is
        # temporrary storage in temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        #if user does not eneter number will display error and ask user to input a number
        print("Please input a number only")
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,

        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format to store the current value and keep it to two deciaml places

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # refresh the current time on the window
        # decrease the time value and wait one second every decrease
        root.update()
        time.sleep(1)

        #when time is == 0 then open a spereate box and alert user
        if (temp == 0):
            messagebox.showinfo("Your Timer has Fisnihed")

        # after every one second the value of temp (the stored amount in the counter will be decreased by one
        #this should happen after the one second delay under root.update

        temp -= 1


# button widget
button = Button(root, text='Start Timer', bd='5',
             command=submit)
button.place(x=110, y=120)

#Headline Text
Headline.pack()
Headline.insert(tkinter.END, "The Atlas Timer System\n")
# run tkinter program and loop screen

root.mainloop()
