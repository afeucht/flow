#from Myframe import Myframe
#from Mymenu import Mymenu
import tkinter
from math import floor
from tkinter import *
from Startup import Startup
from GamePage import GamePage
from InstructPage import InstructPage
from SetPage import SetPage

class Game:
    buttons=[]
    frames={}

    def __init__(self):
        #make the first window, which will make the menu, which owns all other windows
        self.mainWindow=tkinter.Tk()
        #creates main window, sets size, titles
        self.mainWindow.title('Rush')
        self.screenWidth= self.mainWindow.winfo_screenwidth()               
        self.screenHeight= self.mainWindow.winfo_screenheight()               
        self.mainWindow.geometry("%dx%d" % (self.screenWidth, self.screenHeight))

        self.frames["Startup"] = Startup(parent=self.mainWindow, controller=self)
        self.frames["GamePage"] = GamePage(parent=self.mainWindow, controller=self)
        self.frames["InstructPage"] = InstructPage(parent=self.mainWindow, controller=self)
        self.frames["SetPage"] = SetPage(parent=self.mainWindow, controller=self)

        #self.frames["Startup"].place(x=floor(self.screenWidth/2), y=0)
        #self.frames["GamePage"].place(x=floor(screenWidth/2), y=0)
        #self.frames["InstructPage"].place(x=floor(screenWidth/2), y=0)
        #self.frames["SetPage"].place(x=floor(screenWidth/2), y=0)

        self.switch_to("Startup")

        #make frames to go in main window
        #self.mainFrame=Myframe("main", self.mainWindow)
        #self.gameFrame=Myframe("game", self.mainWindow)
        #self.instructFrame=Myframe("instructions", self.mainWindow)
        #self.settingsFrame=Myframe("settings", self.mainWindow)

        #self.mainMenu=Mymenu(self.mainFrame, self.gameFrame, self.instructFrame, self.settingsFrame)
        #self.mainFrame=self.mainMenu.placeButtons()

        

        #for n in range(3):
        #    self.buttons[n].pack()

        #self.mainFrame.get().pack(padx=floor(screenWidth/2), pady=0)
        #self.gameFrame.get().pack(padx=floor(screenWidth/2), pady=0)
        #self.instructFrame.get().pack(padx=floor(screenWidth/2), pady=0)
        #self.settingsFrame.get().pack(padx=floor(screenWidth/2), pady=0)

        #self.mainFrame.get().tkraise()
        #self.gameFrame.get().lower()
        #self.instructFrame.get().lower()
        #self.settingsFrame.get().lower()

    def run(self):
        #run the main window
        self.mainWindow.mainloop()

    def switch_to(self, page):
        for f in self.frames:
            if (f == page):
                self.frames[f].place(x=floor(self.screenWidth/2), y=0)
                #self.frames[f].pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
                self.frames[f].pack_all()
                self.frames[f].tkraise()
            else:
                self.frames[f].unpack_all()

    
