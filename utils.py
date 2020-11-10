# -*- coding: utf-8 -*-
import os

this_path = os.path.realpath('__file__')
this_dir = os.path.dirname(this_path)

menu_dict = {}

items_notebook = ["Pythonmare"]


list_style = ["classic", "ggplot", "bmh", "dark_background", "fivethirtyeight"]
list_file = ['Open', 'Exit']

menu_dict["File"] = list_file
menu_dict["Estilo"] = list_style
