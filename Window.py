from Mymenu import Mymenu
import tkinter
from tkinter import *

class Window:

    def layout_window(self, window):
        #creates main window, sets size, titles
        self.mainWindow.title('Rush')
        screenWidth= self.mainWindow.winfo_screenwidth()               
        screenHeight= self.mainWindow.winfo_screenheight()               
        self.mainWindow.geometry("%dx%d" % (screenWidth, screenHeight))

        #creates frame to hold menu components
        menuFrame=Frame(window, width=screenWidth, height=screenHeight)
        menuFrame.place(anchor=NW)
        menuFrame.pack_propagate(0)
        #menuFrame.tkraise()

        #creates label and packs into menu frame
        top=Label(menuFrame,text="Welcome to Rush")
        top.pack()

        #gets button and packs into menu frame
        self.mainMenu=Mymenu(menuFrame)
        for n in range(3):
            B=self.mainMenu.getButton(n)
            B.pack()

    def __init__(self):
        self.mainWindow=tkinter.Tk()
        self.layout_window(self.mainWindow)
        
        
    def run(self):
        self.mainWindow.mainloop()
