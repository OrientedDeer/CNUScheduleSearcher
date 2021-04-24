import csv
from tkinter import *

teachers = {}
classes = {}

def dictAdd(key, item, dictionary):
    if(key == "Staff, CNU" or item == "Staff, CNU"):
        return
    if(key in dictionary.keys()):
        if(item not in dictionary.get(key)):
            dictionary.get(key).append(item)
        else:
            return
    else:
        dictionary.update({key: [item]})

def readFile(fileName):
    with open(fileName) as file:
        lines = csv.reader(file,delimiter=",")
        for line in lines:
            if(";" in line[10]):
                instructors = line[10].split(";")
                for instructor in instructors:
                    dictAdd(instructor.strip(), line[1], teachers)
                continue
            dictAdd(line[10], line[1], teachers)

    with open(fileName) as file:
        lines = csv.reader(file,delimiter=",")
        for line in lines:
            if(";" in line[10]):
                instructors = line[10].split(";")
                for instructor in instructors:
                    dictAdd(line[1], instructor.strip(), classes)
                continue
            dictAdd(line[1], line[10], classes)

readFile("Fall2021.csv")
readFile("Fall2020.csv")
readFile("Fall2019.csv")
readFile("Spring2020.csv")
readFile("Spring2021.csv")
readFile("Spring2019.csv")

def searchFor(isClass, key):
    if(isClass == 2 and classes.get(key) != None):
        return classes.get(key)
    elif(isClass == 1 and teachers.get(key) != None):
        return teachers.get(key)
    else:
        return "Not a teacher/class."

root = Tk()
label = Label(root)

def methodReply():
    label.config(text =searchFor(var.get(),userText.get()))

var = IntVar()
R1 = Radiobutton(root, text="Professors", variable=var, value=1)
R1.pack( anchor = CENTER )
R2 = Radiobutton(root, text="Classes", variable=var, value=2)
R2.pack( anchor = CENTER )
userText = Entry(root)
userText.pack( anchor = CENTER )
search = Button(root, text="search", command=methodReply)
search.pack()
label.pack(anchor = CENTER)
root.mainloop()
