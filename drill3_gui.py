



from tkinter import *
import tkinter as tk

import drill3
import drill3_func
from tkinter import messagebox
import os
from tkinter import filedialog
import shutil
import sqlite3





def load_gui(self):

    # Text Box
    self.txt_browse1 = tk.Entry(self.master,text='',width=70)
    self.txt_browse1.grid(row=0,column=2,rowspan=1,columnspan=1,padx=(30,40),pady=(40,0),sticky=N+W)
    self.txt_browse2 = tk.Entry(self.master,text='',width=70)
    self.txt_browse2.grid(row=1,column=2,rowspan=1,columnspan=1,padx=(30,40),pady=(0,0),sticky=N+W)


    # Buttons
    self.btn_add = tk.Button(self.master,width=12,height=1,text='Browse..',command=lambda: drill3_func.browser(self))
    self.btn_add.grid(row=0,column=1,padx=(5,0),pady=(40,0),sticky=W)
    self.btn_add = tk.Button(self.master,width=12,height=1,text='Browse..',command=lambda: drill3_func.browser2(self))
    self.btn_add.grid(row=1,column=1,padx=(5,0),pady=(5,0),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Check for files...', command=lambda:drill3_func.checkfile(self))
    self.btn_update.grid(row=2,column=1,padx=(5,0),pady=(5,0),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: drill3_func.ask_quit(self))
    self.btn_update.grid(row=2,column=2,padx=(5,0),pady=(5,0),sticky=E)
    

    







if __name__ == "__main__":
    pass
