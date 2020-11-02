# -*- coding: utf-8 -*-
from app_frame import AppFrame


class TreeViewer(AppFrame):
    def __init__(self, parent, controller):
        AppFrame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

    def setup(self):
        self.add_button(self.parent, "Open", self.controller)
