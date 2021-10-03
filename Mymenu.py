import tkinter
from tkinter import *
from tkinter import messagebox


class Mymenu:

    buttons=[]

    def playGame(self, window):
        screenWidth= window.winfo_screenwidth()               
        screenHeight= window.winfo_screenheight()  
        gameFrame=Frame(window,width=screenWidth, height=screenHeight)

        top=Label(gameFrame,text="Game time")
        top.pack()
        gameFrame.pack_propagate(0)
        
        gameFrame.place(anchor=NW)
        gameFrame.tkraise()

        bottom=Button(gameFrame,text="Main Menu",command=lambda:self.display(window, gameFrame))
        bottom.pack()

    def getInstructions(self, window):
        screenWidth= window.winfo_screenwidth()               
        screenHeight= window.winfo_screenheight()  
        gameFrame=Frame(window,width=screenWidth, height=screenHeight)

        top=Label(gameFrame,text="Get good")
        top.pack()
        gameFrame.pack_propagate(0)
        
        gameFrame.place(anchor=NW)
        gameFrame.tkraise()

        bottom=Button(gameFrame,text="Main Menu",command=lambda:self.display(window, gameFrame))
        bottom.pack()

    def setSettings(self, window):
        screenWidth= window.winfo_screenwidth()               
        screenHeight= window.winfo_screenheight()  
        gameFrame=Frame(window,width=screenWidth, height=screenHeight)

        top=Label(gameFrame,text="Mode is ?")
        top.pack()
        gameFrame.pack_propagate(0)
        
        gameFrame.place(anchor=NW)
        gameFrame.tkraise()

        bottom=Button(gameFrame,text="Main Menu",command=lambda:self.display(window, gameFrame))
        bottom.pack()



    def display(self, raiseFrame, lowerFrame):
        lowerFrame.destroy()
        raiseFrame.place(anchor=NW)
        raiseFrame.tkraise()

    def __init__(self, window):
        self.buttons.append(Button(window,text="Play Game",command=lambda:self.playGame(window)))
        self.buttons.append(Button(window,text="Instructions",command=lambda:self.getInstructions(window)))
        self.buttons.append(Button(window,text="Settings",command=lambda:self.setSettings(window)))

    def getButton(self, n):
        return self.buttons[n] 


