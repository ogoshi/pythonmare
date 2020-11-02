# -*- coding: utf-8 -*-

import os
from tree_viewer import TreeViewer

this_path = os.path.realpath('__file__')
this_dir = os.path.dirname(this_path)

menu_items = ["File", "Estilo"]

items_notebook = ["Pythonmare", "Resultados"]

frames_list = [TreeViewer]
