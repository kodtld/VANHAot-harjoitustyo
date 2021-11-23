#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-


from tkinter import * 
import csv
import os

dirname = os.path.dirname(__file__)
data_file_path = os.path.join(dirname, 'User_Data.csv')

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
        viesti = Label(screen,text="Onnittelut tama toimii").pack()

    def Fail():
        viesti = Label(screen,text="Wrong username or password").pack()
    
    with open(data_file_path,"r") as ud:
        reader = csv.reader(ud, delimiter=",")    
        if [usna,uspa] in reader:

            # Tarkoituksena on tulevaisuudessa kutsua funktiota joka avaa sovelluksen, Succes on valiaikainen tayte
            Succes()
        else:
            Fail()
    ud.close()

def Register():
    usna = User_name.get()
    uspa = User_password.get()

    Used_names=[]
    with open(data_file_path,"r") as ud:
        reader = csv.reader(ud, delimiter=",")
        for row in reader:
            Used_names.append(row[0])
    ud.close()

    # Inner functions
    def Succes():
        viesti = Label(screen,text="Succes! You can now login with your credentials").pack()

    def Fail():
        viesti = Label(screen,text="That username is already taken").pack()

    def Character_check():
        viesti = Label(screen,text="Username can't contain spaces, or the following characters: ä, å, ö").pack()

    def Correct_Lenght():
        viesti = Label(screen,text="Username must be 4-15 characters long").pack()

    if len(usna) < 4 or len(usna) > 15:
        Correct_Lenght()

    elif usna not in Used_names:
        if " " in usna or "ä" in usna or "å" in usna or "ö" in usna:
            Character_check()
        else:    
            with open(data_file_path,"a") as ud:
                writer = csv.writer(ud,lineterminator='\n')
                writer.writerow([usna,uspa])
                ud.close()
                Succes()
    
    else:
        Fail()

Button(text="Login",height="3",width="30",command=Login).pack()

Label(text="").pack()

Button(text="Register",height="3",width="30",command=Register).pack()

screen.mainloop()
    
