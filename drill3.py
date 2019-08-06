



from tkinter import *
import tkinter as tk

import drill3_gui
import drill3_func
from tkinter import messagebox
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(600,150) #(Height, Width)
        self.master.maxsize(600,150)
        # This CenterWindow method will center our app on the user's screen
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill3_func.ask_quit(self))
        arg = self.master



        drill3_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


