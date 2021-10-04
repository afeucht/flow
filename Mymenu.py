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
        #Declaring an empty 1D array.
        a = []
        #Declaring an empty 1D array.
        b = []

        #Initialize the column.
        for j in range(0, colNumber):
            b.append(0)
        #Append the column to each row.
        for i in range(0, rowNumber):
            a.append(b)
        #colorfield=[0*colNumber]*rowNumber

        a = [sublist[:] for sublist in a]
        colorfield=a

        for x in range(rowNumber):
            for y in range(colNumber):
                colorfield[x][y]=0

        #for x in range(rowNumber):
        #    for y in range(colNumber):
        #        print("%i, ", colorfield[x][y], end="")
        #    print("\n")

        #print(colorfield[math.floor(rowNumber/2)][math.floor(colNumber/2)])
        #print("\n")

        colorfield[math.floor(rowNumber/2)][math.floor(colNumber/2)]=1

        #for x in range(rowNumber):
        #    for y in range(colNumber):
        #        print(colorfield[x][y] , ", ", end="")
        #    print("\n")

        for x in range(rowNumber):
            for y in range(colNumber):
                if colorfield[x][y] == 0:
                    square=tkinter.Label(gridFrame, text = "    ",bg = "gray")
                else:
                    square=tkinter.Label(gridFrame, text = "    ",bg = "red")
                #print(colorfield[x][y])
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


