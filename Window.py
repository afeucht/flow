from Menu import Menu
import tkinter

class Window:

    def layout_window(self, window):
        mainMenu=Menu(window)
        B=mainMenu.button()
        B.pack()

    def __init__(self):
        self.mainWindow=tkinter.Tk()
        self.layout_window(self.mainWindow)
        self.mainWindow.geometry("500x200")
        self.mainWindow.mainloop()
