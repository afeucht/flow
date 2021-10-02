import tkinter
from tkinter import *
from tkinter import messagebox


class Menu:

    buttons=[]

    def helloCallBack(self):
       messagebox.showinfo( "Hello Python", "Hello World")

    def __init__(self, window):
        self.buttons.append(Button(window,text="test",command=self.helloCallBack))

    def button(self):
       return self.buttons[0]

