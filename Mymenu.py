import tkinter
from tkinter import *
from tkinter import messagebox
from array import *
import math


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

        gridFrame=Frame(window,width=screenWidth/4, height=screenHeight/2)
        rowNumber=5
        colNumber=5
        colorfield=[[""]*colNumber]*rowNumber

        for x in range(rowNumber):
            for y in range(colNumber):
                colorfield[x][y]="gray"

        colorfield[math.floor(rowNumber/2)][math.floor(colNumber/2)]="red"

        for x in range(rowNumber):
            for y in range(colNumber):
                square=tkinter.Label(gridFrame, text = "    ",bg = colorfield[x][y])
                square.grid(row = x, column = y)
                #square.bind("<Button-1>", on_click)

        gridFrame.pack()
        bottom=Button(gameFrame,text="Main Menu",command=lambda:self.display(window, gameFrame))
        bottom.pack()

    def getInstructions(self, window):
        screenWidth= window.winfo_screenwidth()               
        screenHeight= window.winfo_screenheight()  
        instructFrame=Frame(window,width=screenWidth, height=screenHeight)

        top=Label(instructFrame,text="Get good")
        top.pack()
        instructFrame.pack_propagate(0)
        
        instructFrame.place(anchor=NW)
        instructFrame.tkraise()

        bottom=Button(instructFrame,text="Main Menu",command=lambda:self.display(window, instructFrame))
        bottom.pack()

    def setSettings(self, window):
        screenWidth= window.winfo_screenwidth()               
        screenHeight= window.winfo_screenheight()  
        setFrame=Frame(window,width=screenWidth, height=screenHeight)

        top=Label(setFrame,text="Mode is ?")
        top.pack()
        setFrame.pack_propagate(0)

        setFrame.place(anchor=NW)
        setFrame.tkraise()

        bottom=Button(setFrame,text="Main Menu",command=lambda:self.display(window, setFrame))
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


