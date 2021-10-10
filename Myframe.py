import tkinter
from tkinter import *
import math

class Myframe:
    def makeMainFrame(self, inputFrame):
        #creates label and packs into menu frame
        top=Label(inputFrame,text="Welcome to Rush")
        top.pack()
        

    def makeGameFrame(self, inputFrame, inputWindow):
        screenWidth= inputWindow.winfo_screenwidth()               
        screenHeight= inputWindow.winfo_screenheight()  
        
        top=Label(inputFrame,text="Game time")
        top.pack()

        gridFrame=Frame(inputFrame,width=screenWidth/4, height=screenHeight/2)
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

        a = [sublist[:] for sublist in a]
        colorfield=a

        for x in range(rowNumber):
            for y in range(colNumber):
                colorfield[x][y]=0

        colorfield[math.floor(rowNumber/2)][math.floor(colNumber/2)]=1

        for x in range(rowNumber):
            for y in range(colNumber):
                if colorfield[x][y] == 0:
                    square=tkinter.Label(gridFrame, text = "    ",bg = "gray")
                else:
                    square=tkinter.Label(gridFrame, text = "    ",bg = "red")
                square.grid(row = x, column = y)
                #square.bind("<Button-1>", on_click)

        gridFrame.pack()
        bottom=Button(inputWindow,text="Main Menu",command=lambda:inputFrame.lower())
        bottom.pack()
    
    def makeInstructFrame(self, inputFrame):
        top=Label(inputFrame,text="Get good")
        top.pack()

        bottom=Button(inputFrame,text="Main Menu",command=lambda:inputFrame.lower())
        bottom.pack()

    def makeSettingsFrame(self, inputFrame):
        top=Label(inputFrame,text="Mode is ?")
        top.pack()

        bottom=Button(inputFrame,text="Main Menu",command=lambda:inputFrame.lower())
        bottom.pack()


    def __init__(self, type, inputWindow):
        screenWidth= inputWindow.winfo_screenwidth()               
        screenHeight= inputWindow.winfo_screenheight()  
        self.theFrame=Frame(inputWindow,width=screenWidth, height=screenHeight)

        if(type == "main"):
            self.makeMainFrame(self.theFrame)
        elif(type == "game"):
            self.makeGameFrame(self.theFrame, inputWindow)
        elif(type == "instructions"):
            self.makeInstructFrame(self.theFrame)
        elif(type == "settings"):
            self.makeSettingsFrame(self.theFrame)
        #else:
            #invalid input        
        
    def get(self):
        return self.theFrame