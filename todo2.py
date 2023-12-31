import tkinter
from tkinter import *
import tkinter.messagebox
import pickle
root=tkinter.Tk()
root.title("TO DO LIST")

def add_task():
    task = entry_task.get()
    if task!= "":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning!",message="You must enter a task.")
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning!",message="You must Select a task.")
def load_tasks():
    tasks = pickle.load(open("tasks.dat","rb"))
    listbox_tasks.delete(0,tkinter.END)
    for task in tasks:
        listbox_tasks.insert(tkinter.END,task)
def save_tasks():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat","wb"))

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
listbox_tasks = tkinter.Listbox(root,height=10,width=50)
listbox_tasks.pack(side=tkinter.LEFT)

Scrollbar_tasks = tkinter.Scrollbar(root)
Scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_tasks.config(yscrollcommand= Scrollbar_tasks.set)
Scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root,width=50)
entry_task.pack()

button_add_task = tkinter.Button(root,text="Add Text",command=add_task,width=45)
button_add_task.pack()

button_delete_task = tkinter.Button(root,text="Delete Text",command=delete_task,width=45)
button_delete_task.pack()

button_load_task = tkinter.Button(root,text="Load Text",command=load_tasks,width=45)
button_load_task.pack()

button_save_task = tkinter.Button(root,text="Save Text",command=save_tasks,width=45)
button_save_task.pack()


root.mainloop()
