import tkinter
from tkinter import *
from tkinter import messagebox
from array import *
from Myframe import Myframe


class Mymenu:

    buttons=[]

    def playGame(self, mainFrame, gameFrame):
        gameFrame.tkraise()

    def getInstructions(self, mainFrame, instructFrame):
        instructFrame.tkraise()

    def setSettings(self, mainFrame, settingsFrame):
        settingsFrame.tkraise()


    def display(self, raiseFrame, lowerFrame):
        lowerFrame.destroy()
        raiseFrame.place(anchor=NW)
        raiseFrame.tkraise()

    def __init__(self, mainFrame, gameFrame, instructFrame, settingsFrame):
        self.theFrame=mainFrame

        self.buttons.append(Button(mainFrame.get(),text="Play Game",command=lambda:self.playGame(mainFrame.get(), gameFrame.get())))
        self.buttons.append(Button(mainFrame.get(),text="Instructions",command=lambda:self.getInstructions(mainFrame.get(), instructFrame.get())))
        self.buttons.append(Button(mainFrame.get(),text="Settings",command=lambda:self.setSettings(mainFrame.get(), settingsFrame.get())))


    def placeButtons(self):
        for n in range(3):
            self.buttons[n].pack()
        return self.theFrame