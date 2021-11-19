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


def Succes():
    viesti = Label(screen,text="Onnittelut tämä toimii").pack()
    

def Fail():
    viesti = Label(screen,text="Ei natsaa").pack()
    

def Login():
    usna = User_name.get()
    uspa = User_password.get()
    
    with open("User_Data.csv","r") as ud:
        reader = csv.reader(ud, delimiter=",")
        
        if [usna,uspa] in reader:
            Succes()
        else:
            Fail()

Button(text="Login",height="3",width="30",command=Login).pack()

Label(text="").pack()

Button(text="Register",height="3",width="30").pack()
    
    






screen.mainloop()
    


