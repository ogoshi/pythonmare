# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk


class AppFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.map_frames = {}
        self.tree = None

    def add_button(self, name, controller):
        frame = tk.Frame(self)

        button = ttk.Button(
            frame,
            text=name,
            command=lambda: controller(self.action)
        )
        frame.pack(side=tk.TOP)
        button.pack(side=tk.LEFT)

        self.add_frame2map(name, button)

    def add_label(self, parent, text):
        label = tk.Label(self, text=text)
        label.pack(pady=10, padx=10)

    def add_frame2map(self, k, v):
        self.map_frames[k] = v
