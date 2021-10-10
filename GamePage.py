import tkinter as tk
from math import *
from tkinter import *

class GamePage(tk.Frame):
    
    def __init__(self, parent, controller):

        self.name="GamePage"
        tk.Frame.__init__(self, parent)
        self.controller = controller

        screenWidth= parent.winfo_screenwidth()               
        screenHeight= parent.winfo_screenheight()
        self.configure(width=screenWidth, height=screenHeight) 
        #self.configure(bg='white')

        self.top=tk.Label(self,text="game time start now")
        

        self.gridFrame=Frame(self,width=screenWidth/4, height=screenHeight/2)
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

        #laid out as colorfield[x][y]
        colorfield[0][0]=1
        colorfield[1][4]=1
        colorfield[2][0]=2
        colorfield[1][3]=2
        colorfield[2][1]=3
        colorfield[2][4]=3
        colorfield[4][0]=4
        colorfield[3][3]=4
        colorfield[4][1]=5
        colorfield[3][4]=5


        for x in range(colNumber):
            for y in range(rowNumber):
                if (colorfield[x][y] == 0):
                    square=tk.Label(self.gridFrame, text = "    ",bg = "gray")
                elif(colorfield[x][y]==1):
                    square=tk.Label(self.gridFrame, text = "    ",bg = "red")
                elif(colorfield[x][y]==2):
                    square=tk.Label(self.gridFrame, text = "    ",bg = "green")
                elif(colorfield[x][y]==3):
                    square=tk.Label(self.gridFrame, text = "    ",bg = "blue")
                elif(colorfield[x][y]==4):
                    square=tk.Label(self.gridFrame, text = "    ",bg = "yellow")
                elif(colorfield[x][y]==5):
                    square=tk.Label(self.gridFrame, text = "    ",bg = "orange")
                square.grid(row = y, column = x)
                #square.bind("<Button-1>", on_click)

        

        self.B=tk.Button(self,text="Main Menu",command=lambda:controller.switch_to("Startup"))

        self.pack_all()
        

    def get_name(self):
        return self.name


    def pack_all(self):
        self.top.pack()
        self.gridFrame.pack()
        self.B.pack()

    def unpack_all(self):
        self.gridFrame.pack_forget()
        self.B.pack_forget()
        self.top.pack_forget()