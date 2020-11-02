# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from utils import menu_items, items_notebook, frames_list
from tkinter import filedialog


class PythonMareApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.title('Python Maré DataViewer')
        self.frames = {}

        self.setup_menu()
        notebooks = self.make_notebook(self)
        button = ttk.Button(
            notebooks["Pythonmare"],
            text="Open",
            command=lambda: self.open_data()
        )
        button.pack()

    def setup_frames(self):
        for F in frames_list:

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

    def setup_menu(self):
        for item in menu_items:
            self.menubar.add_cascade(
                label=item,
                menu=None
            )

    def open_data(self, event=None):
        filename = filedialog.askopenfilename()
        print('Selected:', filename)

    def make_notebook(self, parent):
        abas = ttk.Notebook(parent)
        dict_notebook = {}
        for item in items_notebook:
            dict_notebook[item] = tk.Frame(abas)
            abas.add(dict_notebook[item], text=item)

        abas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=tk.YES
        )
        return dict_notebook
