#Imports
from tkinter import *


from tkinter import messagebox

#Creating a global varibale for tasks
tasks_list = []

# variable for counter of tasks posted
counter = 1


#Error system if entry fields are empty
def input_error():

    if enter_taskbox.get() == "":

        messagebox.showerror("Input Error")

        return 0

    return 1


#Clearing given task number from task list box
def clear_task_numbox():

    task_num.delete(0.0, END)


def clear_taskField():
    # clear the content of task field entry box
    enter_taskbox.delete(0, END)


#insert new task to list
def insert_task():
    global counter

    # check value (whats in entry box) to ensure that input is valid
    value = input_error()

    #value check fallback if 0
    if value == 0:
        return

    #Task info concat with a new line to ensure next task is pushed below and not inline
    content = enter_taskbox.get() + "\n"

    #publish task (content) to the list
    tasks_list.append(content)

    # insert content of task entry field to the text area
    text_area.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    # increase current number task by one
    counter += 1

    #clear  entry field
    clear_taskField()


#Use to delete the specified task
def delete():
    global counter

    # If there are no tasks to delete (Length of the task lenght is less than or equal to 0 then show error)
    if len(tasks_list) <= 0:
        #Put message in title of window
        # Work to make text field instead

        messagebox.showerror("No task")
        #finsih
        return

    # store current task number enetred by user to delete
    number = task_num.get(1.0, END)

    #input error if number of task is not on line
    if number == "\n":
        messagebox.showerror("input error")
        return

    else:
        task_no = int(number)

    #Call to delete  content in task number field
    clear_task_numbox()

    # deleted enetred task number from  list
    tasks_list.pop(task_no - 1)

    # decrease the current task counter by subtracitung one
    counter -= 1

    #delete from big text vox
    text_area.delete(1.0, END)

    # Change task number once a task is delted, do this by taking the assigned number and the string
    #and moving given nymber on task list up by one.

    for i in range(len(tasks_list)):
        text_area.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])


# Main Code for UI
if __name__ == "__main__":
    # create a new window
    gui = Tk()



    # set the title of GUI window
    gui.title("Atlas To Do ")

    #Set BackGround
    gui.configure(background="light blue")


    # set the size of window
    gui.geometry("350x400")

    # create a label (servrs as builder for entry field)
    enter_task = Label(gui, text="Enter Task Name", bg="light blue")

    # create a new text entry field

    enter_taskbox = Entry(gui)

    #Submit Button places it into message box of all tasks
    Submit = Button(gui, text="Submit", fg="Black", bg="Green", command=insert_task)



    # This text area is for listing the jobs to do
    text_area = Text(gui, height=15, width=25, font="Arial 13", borderwidth=2, relief="raised" )

    # create a new label to delete task from list by enetring number
    enter_tasknumber = Label(gui, text="Delete Task Number", )
    #Number of Task, Details
    task_num = Text(gui, height=1, width=2, font="Arial 13")

    # create a Delete Button and
    #Make Button Red!!! (Stakeholder Request)
    delete = Button(gui, text="Delete", fg="Black", bg="Red", command=delete)

    # create a Exit Button to quit
    #For relevant implicaitons & usability hueristscs
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

   #Using grid & x & y positioning to align buttons & componsents
    #Title
    enter_task.grid(row=0, column=2)

    #Enter new task text field
    enter_taskbox.grid(row=1, column=2, ipadx=50)
    #Submit Button
    Submit.grid(row=1, column=3)

    #Intrustiocn Box
    #enter_tasknumber.grid(row=2, column=3, pady=50)
    enter_tasknumber.place(x=230, y=50)

    #ENTER TASK TO DELETE INPUT

    task_num.place(x=230, y=75)

    #Big Box of Tasks
    text_area.grid(row=2, column=2,  sticky=W)

    delete.place(x=230, y=103)

    Exit.place(x=10, y=340)

    # loops window over and over agians to keep it updated
    gui.mainloop()
