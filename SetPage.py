import tkinter as tk
from math import floor

class SetPage(tk.Frame):
    
    def __init__(self, parent, controller):

        self.name="SetPage"
        tk.Frame.__init__(self, parent)
        self.controller = controller

        screenWidth= parent.winfo_screenwidth()               
        screenHeight= parent.winfo_screenheight()
        self.configure(width=screenWidth, height=screenHeight) 
        #self.configure(bg='white')

        self.top=tk.Label(self,text="it is how it is")
        self.B=tk.Button(self,text="Main Menu",command=lambda:self.controller.switch_to("Startup"))
        self.pack_all()

    def get_name(self):
        return self.name

    def pack_all(self):
        self.top.pack()
        self.B.pack()

    def unpack_all(self):
        self.top.pack_forget()
        self.B.pack_forget()