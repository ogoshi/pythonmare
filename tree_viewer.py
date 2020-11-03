# -*- coding: utf-8 -*-
from app_frame import AppFrame
import tkinter as tk
from tkinter import ttk
import os, glob

this_path = os.path.realpath('__file__')
this_dir = os.path.dirname(this_path)

class TreeViewer(AppFrame):
    def __init__(self, parent, controller):
        AppFrame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        vsb = ttk.Scrollbar(orient="vertical")
        hsb = ttk.Scrollbar(orient="horizontal")

        self.tree = ttk.Treeview(
            columns=("fullpath", "type", "size"),
            displaycolumns="size",
            yscrollcommand=lambda f, l: self.autoscroll(vsb, f, l),
            xscrollcommand=lambda f, l: self.autoscroll(hsb, f, l)
        )

        vsb['command'] = self.tree.yview
        hsb['command'] = self.tree.xview

        self.tree.heading("#0", text="Directory Structure", anchor='w')
        self.tree.heading("size", text="File Size", anchor='w')
        self.tree.column("size", stretch=0, width=100)
        self.name = "tree"
        self.tree.pack()

    def setup(self):
        self.add_button(self.tree.get_children(), "Open", self.controller)

    def populate_roots(self, filename):
        node = self.tree.insert('', 'end', text=filename, values=[filename, "text"])
        self.populate_tree(self.tree, node, filename)


    # esta função insere os caminhos do arquivo no widget Treeview
    def populate_tree(self, tree, node, fname):
        if tree.set(node, "type") != 'text':
            return
    
        path = tree.set(node, "fullpath")
        tree.delete(*tree.get_children(node))

        id = tree.insert(node, "end", text='Plot1', values=['plot1', "text"])
        id = tree.insert(node, "end", text='Plot2', values=['plot2', "text"])

    def autoscroll(self, sbar, first, last):
        """Hide and show scrollbar as needed."""
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:
            sbar.grid_remove()
        else:
            sbar.grid()
        sbar.set(first, last)
