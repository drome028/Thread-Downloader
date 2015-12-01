import tkinter as tk
import StartPage as start
__author__ = 'David'


class ThreadDownloaderUtilities(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="left", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = start.StartPage(container, self)

        self.frames[start.StartPage] = frame

        frame.grid(row=0, column=0, stick="nsew")

        self.show_frame(start.StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
