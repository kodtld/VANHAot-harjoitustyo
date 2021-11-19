from tkinter import *
import csv


screen = Tk()
screen.geometry("950x750")
screen.title("Opintojen seuranta")

User_name = Entry(screen, width="75")
User_name.pack()
User_name.insert(0,"Username")

User_password = Entry(screen,width="75")
User_password.pack()
User_password.insert(0,"Password")


def Login():
    usna = User_name.get()
    uspa = User_password.get()
    
    def Succes():
        viesti = Label(screen,text="Onnittelut tämä toimii").pack()

    def Fail():
        viesti = Label(screen,text="Wrong username or password").pack()

    with open("User_Data.csv","r") as ud:
        reader = csv.reader(ud, delimiter=",")
        
        if [usna,uspa] in reader:
            Succes()
        else:
            Fail()


def Register():
    usna = User_name.get()
    uspa = User_password.get()
    Used_names=[]

    with open("User_Data.csv","r") as ud:
        reader = csv.reader(ud, delimiter=",")
        for row in reader:
            Used_names.append(row[0])

    # Inner functions
    def Succes():
        viesti = Label(screen,text="Onnittelut tämä toimii").pack()

    def Fail():
        viesti = Label(screen,text="Wrong username or password").pack()

    # Check for duplicates
    if usna in Used_names:
        Fail()
    
    else:
        Succes()




Button(text="Login",height="3",width="30",command=Login).pack()

Label(text="").pack()

Button(text="Register",height="3",width="30",command=Register).pack()
    
    


screen.mainloop()
    
