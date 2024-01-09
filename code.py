import tkinter
from tkinter import *

app=Tk()
app.title("To-Do List App")
app.geometry("400x650+400+100")
app_tasks=[]

Image_icon=PhotoImage(file="app icon.png")
app.iconphoto(False,Image_icon)

def openTaskFile():
    try:
        global app_tasks
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task !="\n":
                app_tasks.append(task)
                listbox.insert(END,task)
    except:
        file=open("tasklist.txt","w")
        file.close()

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        app_tasks.append(task)
        listbox.insert(END,task)
def delTask():
    global app_tasks
    task=str(listbox.get(ANCHOR))
    if task in app_tasks:
        app_tasks.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in app_tasks:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

heading=Label(app,text="TASK MANAGER",font="arial 20 bold",fg="silver",bg="yellow")
heading.place(x=80,y=20)


frame=Frame(app,width=400,height=50,bg="white")
frame.place(x=0,y=180)


task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",width=4,bg="green yellow",fg="Silver",bd=0,command=addTask)
button.place(x=300,y=0)
button=Button(text="DEL",font="arial 20 bold",width=4,bg="green yellow",fg="Silver",bd=0,command=delTask)
button.place(x=300,y=100)


frame1=Frame(app,bd=3,width=700,height=200,bg="Silver")
frame1.pack(pady=(160,0))
frame1.place(x=0,y=240)

listbox=Listbox(frame1,font=('arial bold',12,),width=40,height=16,bg="lawn green")
listbox.pack(side=LEFT , fill=BOTH ,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT , fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()



app.mainloop()


