import tkinter as tk
from tkinter import *
from math import floor


class Startup(tk.Frame):

    buttons=[]
    frames={}
    
    def __init__(self, parent, controller):

        self.name="Startup"
        tk.Frame.__init__(self, parent)
        self.controller = controller

        screenWidth= parent.winfo_screenwidth()               
        screenHeight= parent.winfo_screenheight()
        self.configure(width=screenWidth, height=screenHeight)
        #self.configure(bg='white')

        self.top=tk.Label(self,text="Welcome to Rush")
        self.buttons.append(tk.Button(self,text="Play Game",command=lambda:controller.switch_to("GamePage")))
        self.buttons.append(tk.Button(self,text="Instructions",command=lambda:controller.switch_to("InstructPage")))
        self.buttons.append(tk.Button(self,text="Settings",command=lambda:controller.switch_to("SetPage")))
        self.pack_all()
        

    def get_name(self):
        return self.name

    def pack_all(self):
        self.top.pack()

        for n in range(3):
            self.buttons[n].pack()

    def unpack_all(self):
        for n in range(3):
            self.buttons[n].pack_forget()
        self.top.pack_forget()

