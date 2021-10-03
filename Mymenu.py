import tkinter
from tkinter import *
from tkinter import messagebox


class Mymenu:

    buttons=[]

    def playGame(self, window):
        screenWidth= window.winfo_screenwidth()               
        screenHeight= window.winfo_screenheight()  
        gameFrame=Frame(window, bg='grey',width=screenWidth, height=screenHeight)

        top=Label(gameFrame,text="Game time")
        top.pack()
        gameFrame.pack_propagate(0)

        #gameFrame.pack()
        gameFrame.place(anchor=NW)
        gameFrame.tkraise()

    def __init__(self, window):
        self.buttons.append(Button(window,text="Play Game",command=lambda:self.playGame(window)))

    def getButton(self):
        return self.buttons[0] 


