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
plugin = None


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


class PythonMareApplication(tk.Frame):
    def __init__(self, parent=None, data=None):
        self.parent = parent
        if not self.parent:
            tk.Frame.__init__(self)
            self.main = self.master
        else:
            self.main = tk.Toplevel()
            self.master = self.main
        self.frames = {}
        self.main.title('Mare - visualizador de dados')
        self.setup_menu()
        self.setup_gui()
        self.setup_frames(self.nb, [TreeViewer, TidalGraph])

    def setup_gui(self):
        self.m = tk.PanedWindow(self.main, orient=tk.VERTICAL)
        self.m.pack(fill=tk.BOTH, expand=1)
        self.nb = ttk.Notebook(self.main)
        self.m.add(self.nb)
        self.set_geometry()
        return

    def get_best_geometry(self):
        ws = self.main.winfo_screenwidth()
        hs = self.main.winfo_screenheight()
        self.w = w = ws/1.4
        h = hs*0.7
        x = (ws/2)-(w/2)
        y = (hs/2)-(h/2)
        g = '%dx%d+%d+%d' % (w, h+10, x, y)
        return g

    def set_geometry(self):
        self.winsize = self.get_best_geometry()
        self.main.geometry(self.winsize)
        return

    def setup_frames(self, parent, frame_list):
        main = tk.PanedWindow(orient=tk.HORIZONTAL)
        self.nb.add(main, text='ExploreMare')

        for F in frame_list:
            f1 = tk.Frame(main)
            frame = F(f1, self)
            self.frames[F] = frame
            frame.pack(side=tk.LEFT, fill=tk.Y, expand=tk.TRUE, padx=0, pady=0)
            f1.pack(side=tk.LEFT, fill=tk.Y, expand=tk.TRUE, padx=0, pady=0)

    def setup_menu(self):
        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(
            label="Open",
            command=lambda: self.open_data(self.frames[TreeViewer].action)
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
        self.main.config(menu=menubar)

    def open_data(self, event):
        filename = filedialog.askopenfilename()
        event(filename.split('/')[-1])
        self.configure_app_data(filename)

    def configure_app_data(self, filename):
        td = TidalData(filename)
        data = td.data2dict()
        metadata = td.get_metadata()
        changeExchangeData(data, metadata)

    def make_notebook(self, parent):
        dict_notebook = {}
        for item in items_notebook:
            dict_notebook[item] = tk.Frame(self.nb)
            self.nb.add(dict_notebook[item], text=item)
        return dict_notebook

    def show_frame(self, conteudo):
        frame = self.frames[conteudo]
        frame.tkraise()
