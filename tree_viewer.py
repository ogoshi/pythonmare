# -*- coding: utf-8 -*-
from app_frame import AppFrame
import tkinter as tk
from tkinter import ttk
import os
from app_plot import changeExchange
from app_plot import TidalGraph

this_path = os.path.realpath('__file__')
this_dir = os.path.dirname(this_path)


class TreeViewer(AppFrame):
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.map_frames = {}
        tk.Frame.__init__(self, parent)
        self.main = self.master

        vsb = ttk.Scrollbar(orient="vertical")
        hsb = ttk.Scrollbar(orient="horizontal")

        tframe = tk.Frame(self.main)
        self.tree = ttk.Treeview(
            tframe,
            columns=("fullpath", "type", "size"),
            displaycolumns="size",
            yscrollcommand=lambda f, l: self.autoscroll(vsb, f, l),
            xscrollcommand=lambda f, l: self.autoscroll(hsb, f, l)
        )

        vsb['command'] = self.tree.yview
        hsb['command'] = self.tree.xview
        self.main.pack(side=tk.LEFT, fill=tk.Y, expand=tk.TRUE, padx=3, pady=2)
        self.tree.heading("#0", text="Nome do Arquivo", anchor='w')
        self.tree.heading("size", text="Tamanho", anchor='w')
        self.tree.column("size", stretch=0, width=100)
        self.name = "tree"
        self.tree.bind("<Double-1>", self.on_double_click)
        tframe.pack(side=tk.LEFT, fill=tk.Y, expand=1)
        self.tree.pack(side=tk.LEFT, fill=tk.Y, expand=1)
        self.add_button("Open", self.controller.open_data)

    def on_double_click(self, event):
        item = self.tree.selection()[0]
        plot = self.tree.item(item, "text")
        changeExchange(
            plot,
            plot,
            self.controller.frames[TidalGraph]
        )

    def action(self, filename):
        node = self.tree.insert(
            '',
            'end',
            text=filename,
            values=[filename, "text"]
        )
        size = os.stat(os.path.join(this_dir, filename)).st_size
        self.tree.set(node, "size", "%d bytes" % size)
        self.populate_tree(filename, node)

    def populate_tree(self, fname, node=None):
        if self.tree.set(node, "type") != 'text':
            return

        self.tree.insert(
            node,
            "end",
            text='mare',
            values=['mare', "text"]
        )

        self.tree.insert(
            node,
            "end",
            text='normalizado',
            values=['normalizado', "text"]
        )

        self.tree.insert(
            node,
            "end",
            text='estatistica',
            values=['estatistica', "text"]
        )

    def autoscroll(self, sbar, first, last):
        """Hide and show scrollbar as needed."""
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:
            sbar.grid_remove()
        else:
            sbar.grid()
        sbar.set(first, last)
