# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from utils import (
    items_notebook
)

from tree_viewer import TreeViewer
from app_plot import TidalGraph, changeExchangeData
from tidal_data import TidalData

from tkinter import filedialog


LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


class PythonMareApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Python Mare DataViewer')
        self.frames = {}
        self.new_data = {}
        self.notebooks = self.make_notebook(self)
        self.menubar = tk.Menu(self)
        self.container = tk.Frame(self.notebooks['Pythonmare'])
        self.container.pack(side="right", fill="x", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.setup_frames(self.container)

        self.setup_menu()

    def setup_frames(self, parent):
        cont = 0

        for F in (TreeViewer, TidalGraph):
            frame = F(parent, self)
            self.frames[F] = frame
            frame.pack(side=tk.LEFT, fill=tk.Y, expand=tk.TRUE, padx=3, pady=2)
            cont += 1

    def setup_menu(self):
        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(
            label="Save settings",
            command=lambda: popupmsg("Not supported just yet!")
        )
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)

        menubar.add_cascade(label="File", menu=filemenu)

        style = tk.Menu(menubar, tearoff=1)
        style.add_command(
            label="classic",
            command=lambda: self.frames[TidalGraph].estilo("classic")
        )
        style.add_command(
            label="ggplot",
            command=lambda: self.frames[TidalGraph].estilo("ggplot")
        )
        style.add_command(
            label="bmh",
            command=lambda: self.frames[TidalGraph].estilo("bmh")
        )
        style.add_command(
            label="dark_background",
            command=lambda: self.frames[TidalGraph].estilo("dark_background")
        )
        style.add_command(
            label="fivethirtyeight",
            command=lambda: self.frames[TidalGraph].estilo("fivethirtyeight")
        )

        menubar.add_cascade(label="Definir Estilo", menu=style)

        tk.Tk.config(self, menu=menubar)

    def open_data(self, event):
        filename = filedialog.askopenfilename()
        event(filename.split('/')[-1])
        self.configure_app_data(filename)

    def configure_app_data(self, filename):
        td = TidalData(filename)
        data = td.data2dict()
        print(data.items())
        metadata = td.get_metadata()
        changeExchangeData(data, metadata)

    def make_notebook(self, parent):
        abas = ttk.Notebook(parent)
        dict_notebook = {}
        for item in items_notebook:
            dict_notebook[item] = tk.Frame(abas)
            abas.add(dict_notebook[item], text=item)

        abas.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=tk.TRUE
        )
        return dict_notebook

    def show_frame(self, conteudo):
        frame = self.frames[conteudo]
        frame.tkraise()
