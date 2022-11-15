from tkinter import *
from tkinter import ttk
import webbrowser
import json

APP_FONT = ('verdana', 30, "bold")

class List:
    def __init__(self , call):
        self.window = Tk()
        self.window.title(f"{call} Section")
        # width=400, height=400
        self.window.geometry("400x400")
        
        # create a Main Frame
        main_frame = Frame(self.window)
        main_frame.pack(fill=BOTH, expand=1)
        
        # Create A Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        
        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(
        main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        
        # Configure Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind("<Configure>", lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))
        
        # Create Another Frame INSIDE The Canvas
        second_frame = Frame(my_canvas)
        
        # Add That New frame To a Window In Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        
        # Now put you widgets in second_frame
        with open("books.json", "r") as file:
            data = json.load(file)
            curr_data = data[call]

            for _ in range(len(curr_data)):
                link = Label(second_frame, text=curr_data[_], font=('Helveticabold', 12), fg="#09181d", cursor="hand2", anchor="e")
                link.bind("<Button-1>", lambda e:self.callback())
                link.grid(row=_, column=0, pady=5, padx=150)

            
        self.window.mainloop()
    
    def callback(self):
        webbrowser.open_new(r"http://www.tutorialspoint.com")
