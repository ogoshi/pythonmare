# -*- coding: utf-8 -*-
import tkinter as tk


class AppFrame(tk.Frame):
    def __init__(self, parent, controller, text):
        tk.Frame.__init__(self, parent)

    def create_top_level_item(self, vf, id):
        pass