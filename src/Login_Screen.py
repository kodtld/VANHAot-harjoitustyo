#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-

import tkinter as tk
import csv
import os

dirname = os.path.dirname(__file__)
data_file_path = os.path.join(dirname, 'User_Data.csv')

root = tk.Tk()
root.geometry("950x750")
root.title("Opintojen seuranta")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)

def frm1to2():
    frame1.pack_forget()
    frame2.pack()

def frm2to1():
    frame2.pack_forget()
    frame1.pack()

def frm2to3():
    frame2.pack_forget()
    frame3.pack()

def frm2to4():
    frame2.pack_forget()
    frame4.pack()

def frm3to2():
    frame3.pack_forget()
    frame2.pack()

def frm4to2():
    frame4.pack_forget()
    frame2.pack()

# FRAME 1

User_name = tk.Entry(frame1, width="75")
User_name.pack()
User_name.insert(0,"Username")

User_password = tk.Entry(frame1,width="75")
User_password.pack()
User_password.insert(0,"Password")

def Login():
    usna = User_name.get()
    uspa = User_password.get()

    def Fail():
        viesti = tk.Label(frame1,text="Wrong username or password").pack()
    
    with open(data_file_path,"r") as ud:
        reader = csv.reader(ud, delimiter=",")    
        if [usna,uspa] in reader:

            # Tarkoituksena on tulevaisuudessa kutsua funktiota joka avaa sovelluksen, Succes on valiaikainen tayte
            frm1to2()
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
        viesti = tk.Label(frame1,text="Succes! You can now login with your credentials").pack()

    def Fail():
        viesti = tk.Label(frame1,text="That username is already taken").pack()

    def Character_check():
        viesti = tk.Label(frame1,text="Username can't contain spaces, or the following characters: ä, å, ö").pack()

    def Correct_Lenght():
        viesti = tk.Label(frame1,text="Username must be 4-15 characters long").pack()

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

tk.Button(frame1,text="Login",height="3",width="30",command=Login).pack()

tk.Label(frame1,text="").pack()

tk.Button(frame1,text="Register",height="3",width="30",command=Register).pack()

frame1.pack()
root.mainloop()
    
