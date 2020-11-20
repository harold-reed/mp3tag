import os, time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from stat import * # ST_SIZE etc 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)
        self.wm_iconbitmap('icon.ico')
 
        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
 
        self.button()
 
 
 
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
 
 
    def fileDialog(self):
 
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetypes =
        (("mp3 files","*.mp3"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
#        self.label.configure(text = self.filename)

        try:
            st = os.stat(self.filename)
        except IOError:
                    print ("failed to get information about", self.filename)
        else:
            print ("file size:", st[ST_SIZE])
            print ("file modified:", time.asctime(time.localtime(st[ST_MTIME]))) 
            self.label.configure(text = (self.filename, st[ST_SIZE]))
 


 
 
root = Root()
root.mainloop()