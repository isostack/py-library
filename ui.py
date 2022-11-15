"""UI classes for library application.
Browse class(window) destroys the main in window(Interface)

"""

from distutils.archive_util import make_archive
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
import webbrowser
from booklist import List

TRANS_BLACK = '#000'
APP_FONT = ('verdana', 10)
BROWSE_FONT = ('verdana', 30 , "bold")

class Browse:
    def __init__(self):
        self.window = Tk()
        self.window.title("Browse Books")
        self.window.geometry("768x790")
        self.window.resizable(True, True)

        banner_img = PhotoImage(file="img/browse.png")
        footer_img = PhotoImage(file="img/landing.png")

        self.app_canvas = Canvas(self.window, width=768, height=508)
        self.app_canvas.create_image(0, 0, image = banner_img, anchor = "nw")
        self.app_canvas.grid(row=0, column=0,columnspan=8)

        self.entry = Entry(width=70)
        self.entry.insert(END, string="")
        self.entry.grid(row=1, column=1 , columnspan=7)

        btn = Button(self.window, text="Quick Search →",fg=TRANS_BLACK, font=APP_FONT, highlightthickness=0,command=self.callback).grid(row=1, column=6)

        self.make_groups(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

        self.window.mainloop()

    def make_groups(self,arg):
        curr_row = 2
        curr_col = 0
        for number in range(len(arg)):
            btn = Button(self.window, text=arg[number],fg=TRANS_BLACK, font=APP_FONT, highlightthickness=0 , pady=10 , padx=10).grid(row=curr_row, column=curr_col)
            curr_col += 1
            if number == 7 or number == 15 or number == 23:
                curr_row += 1
                curr_col = 0

    def callback(self):
        item = self.entry.get().upper()
        listbooks = List(item)
        
class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Meta Library")
        self.root.geometry("1200x750")
        self.root.resizable(False, False)

        banner_img = PhotoImage(file="img/banner.png")
        footer_img = PhotoImage(file="img/landing.png")

        self.app_canvas = Canvas(self.root, width=1200, height=315)
        self.app_canvas.create_image(0, 0, image = banner_img, anchor = "nw")
        self.app_canvas.grid(row=0, column=0,columnspan=2)

        btn_1 = Button(self.root, text="Browse Books",fg=TRANS_BLACK, font=APP_FONT, highlightthickness=0,command=self.browse_books)
        btn_1.grid(row=1, column=0)
        btn_2 = Button(self.root, text="Edit Database",fg=TRANS_BLACK, font=APP_FONT, highlightthickness=0)
        btn_2.grid(row=1, column=1)
        btn_3 = Button(self.root, text="Buy Books",fg=TRANS_BLACK, font=APP_FONT, highlightthickness=0)
        btn_3.grid(row=2, column=0)
        btn_4 = Button(self.root, text="Redeem Book",fg=TRANS_BLACK, font=APP_FONT, highlightthickness=0)
        btn_4.grid(row=2, column=1)
        
        self.footer_canvas = Canvas(self.root , width=1014 , height=400)
        self.footer_canvas.create_image(0, 0, image = footer_img, anchor = "nw")
        self.footer_canvas.grid(row=3, column=0,columnspan=2)
        
        self.root.mainloop()

    def browse_books(self):
        self.root.destroy()
        browser = Browse()
