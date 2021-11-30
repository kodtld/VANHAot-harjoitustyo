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


class Frame_Changer:
    def __init__(self,master):
        pass

   


class Login_Frame:
    def __init__(self,master):
        loginframe = tk.Frame(master)
        

        self.User_name = tk.Entry(master, width="75")
        self.User_name.pack()
        self.User_name.insert(0,"Username")

        self.User_password = tk.Entry(master,width="75")
        self.User_password.pack()
        self.User_password.insert(0,"Password")

        def Login():
            usna = self.User_name.get()
            uspa = self.User_password.get()

            def Fail():
                self.viesti = tk.Label(master,text="Wrong username or password").pack()
            
            with open(data_file_path,"r") as ud:
                reader = csv.reader(ud, delimiter=",")    
                if [usna,uspa] in reader:

                   pass
                else:
                    Fail()
            ud.close()

        def Register():
            usna = self.User_name.get()
            uspa = self.User_password.get()

            Used_names=[]
            with open(data_file_path,"r") as ud:
                reader = csv.reader(ud, delimiter=",")
                for row in reader:
                    Used_names.append(row[0])
            ud.close()

            # Inner functions
            def Succes():
                self.viesti = tk.Label(master,text="Succes! You can now login with your credentials").pack()

            def Fail():
                self.viesti = tk.Label(master,text="That username is already taken").pack()

            def Character_check():
                self.viesti = tk.Label(master,text="Username can't contain spaces, or the following characters: ä, å, ö").pack()

            def Correct_Lenght():
                self.viesti = tk.Label(master,text="Username must be 4-15 characters long").pack()

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

        self.logbtn = tk.Button(master,text="Login",height="3",width="30",command=Login).pack()

        self.tt = tk.Label(master,text="").pack()

        self.regbtn = tk.Button(master,text="Register",height="3",width="30",command=Register).pack()



class Main_Frame():
    def __init__(self,master):
        mainframe = tk.Frame(master)
        




s = Frame_Changer(root)
root.mainloop()
    
"""         tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(CourseScreen)).pack() """