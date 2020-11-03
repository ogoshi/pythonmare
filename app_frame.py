# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk


class AppFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.map_frames = {}
        self.tree = None
        
    def add_button(self, parent, name, controller):
        button = ttk.Button(
            parent,
            text=name,
            command=lambda: controller.open_data(self.populate_roots)
        )
        button.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.NO)
        self.add_frame2map(name, button)

    def populate_roots(self, filename):
        name = [
            name for name in filename.split('/') if name.find('.txt') != -1
        ]

        node = self.tree.insert(
                    '',
                    'end',
                    text=name[0],
                    values=[filename, "directory"]
        )
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.add_frame2map(filename, node)

    def add_frame2map(self, k, v):
        self.map_frames[k] = v
