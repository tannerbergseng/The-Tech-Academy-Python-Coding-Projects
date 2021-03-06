


from tkinter import *
import tkinter as tk

import drill3
import drill3_gui
from tkinter import messagebox
import os
from tkinter import filedialog
import shutil
import sqlite3




def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo




# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def browser(self):
    """Browse file directory."""
    path = filedialog.askdirectory()
    print (self.txt_browse1.insert(INSERT,path))


def browser2(self):
    """Browse file directory."""
    path = filedialog.askdirectory()
    print (self.txt_browse2.insert(INSERT,path))


def checkfile(self):
    sourceDir = self.txt_browse1.get()
    source = os.listdir(sourceDir)
    destination = self.txt_browse2.get()
    for files in source:
        if files.endswith(".txt"):
            absPath = os.path.join(sourceDir, files)
            time = os.path.getmtime(absPath)
            print(files, time)
            shutil.move(absPath, destination)
            print(destination)

            
            """ checks to add to database"""

            conn = sqlite3.connect('drill3Final.1.db')
            with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                    ID INTEGER PRIMARY KEY, \
                    col_fileName TEXT,\
                    col_date TEXT\
                    )")
                conn.commit()
            conn.close()


            conn = sqlite3.connect('drill3Final.1.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_fileName,col_date) VALUES (?,?)", \
                [files,time])
                
            conn.close()



            
            
           
          





   
 


if __name__ == "__main__":
    pass
