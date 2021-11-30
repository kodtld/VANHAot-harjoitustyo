#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-

import tkinter as tk
import csv
import os

dirname = os.path.dirname(__file__)
userdata_file_path = os.path.join(dirname, 'User_Data.csv')
coursedata_file_path = os.path.join(dirname, 'Course_Data.csv')

class MainScreen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("950x750")
        self.title("Opintojen seuranta")
        self._frame = None
        self.switch_frame(LoginScreen)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class LoginScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.User_name = tk.Entry(self, width="75")
        self.User_name.pack()
        self.User_name.insert(0,"Username")

        self.User_password = tk.Entry(self,width="75")
        self.User_password.pack()
        self.User_password.insert(0,"Password")
        
        def Login():
            usna = self.User_name.get()
            uspa = self.User_password.get()

            def Fail():
                self.viesti = tk.Label(self,text="Wrong username or password").pack()
            
            with open(userdata_file_path,"r") as ud:
                reader = csv.reader(ud, delimiter=",")    
                if [usna,uspa] in reader:
                    
                   lam = lambda : master.switch_frame(CourseScreen)
                   lam()
                else:
                    Fail()
            ud.close()

        def Register():
            usna = self.User_name.get()
            uspa = self.User_password.get()

            Used_names=[]
            with open(userdata_file_path,"r") as ud:
                reader = csv.reader(ud, delimiter=",")
                for row in reader:
                    Used_names.append(row[0])
            ud.close()

            # Inner functions
            def Succes():
                self.viesti = tk.Label(self,text="Succes! You can now login with your credentials").pack()

            def Fail():
                self.viesti = tk.Label(self,text="That username is already taken").pack()

            def Character_check():
                self.viesti = tk.Label(self,text="Username can't contain spaces, or the following characters: ä, å, ö").pack()

            def Correct_Lenght():
                self.viesti = tk.Label(self,text="Username must be 4-15 characters long").pack()

            if len(usna) < 4 or len(usna) > 15:
                Correct_Lenght()

            elif usna not in Used_names:
                if " " in usna or "ä" in usna or "å" in usna or "ö" in usna:
                    Character_check()
                else:    
                    with open(userdata_file_path,"a") as ud:
                        writer = csv.writer(ud,lineterminator='\n')
                        writer.writerow([usna,uspa])
                        ud.close()
                        Succes()
            
            else:
                Fail()
        
        
        tk.Button(self,text="Login",height="3",width="30",command=Login).pack()

        tk.Label(self,text="").pack()

        tk.Button(self,text="Register",height="3",width="30",command=Register).pack()

class CourseScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Kurssi").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Add courses",
                  command=lambda: master.switch_frame(Add_CourseScreen)).pack()
        tk.Button(self, text="My courses",
                  command=lambda: master.switch_frame(AddGradeScreen)).pack()

        tk.Button(self, text="Logout",
                  command=lambda: master.switch_frame(LoginScreen)).pack()

class Add_CourseScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Home",
                  command=lambda: master.switch_frame(CourseScreen)).pack()

        self.Course_name = tk.Entry(self, width="75")
        self.Course_name.pack()
        self.Course_name.insert(0,"Course name")
        
        self.Scope = tk.Entry(self, width="75")
        self.Scope.pack()
        self.Scope.insert(0,"Scope in study points, enter integer")
        
        self.Return = tk.Entry(self, width="75")
        self.Return.pack()
        self.Return.insert(0,"Return day Mon/Tue/Wed/Thu/Fri")

        self.Peer = tk.Entry(self, width="75")
        self.Peer.pack()
        self.Peer.insert(0,"Peer review day Mon/Tue/Wed/Thu/Fri")

        self.End_Date = tk.Entry(self, width="75")
        self.End_Date.pack()
        self.End_Date.insert(0,"End date in YYYY/MM/DD")


        def Add_Course():
            rl = []
            rl.append(self.Course_name.get())
            rl.append(self.Scope.get())
            rl.append(self.Return.get())
            rl.append(self.Peer.get())
            rl.append(self.End_Date.get())
            rl.append("e")
            print(rl)

        tk.Button(self,text="Add course",height="3",width="30",command=Add_Course).pack()

class AddGradeScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Button(self, text="Home",
                  command=lambda: master.switch_frame(CourseScreen)).pack()

if __name__ == "__main__":
    root = MainScreen()
    root.mainloop()