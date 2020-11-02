# -*- coding: utf-8 -*-
import unittest
import app_frame
import tkinter as tk

class TestAppFrame(unittest.TestCase):
    """
    docstring: class para testar frames
    """
    def test_app_frame_is_tk_frame(self):
        frame = app_frame.AppFrame(None, None, "")
        self.assertIsInstance(
            frame,
            tk.Frame,
            "Não é um tipo tk.Frame"
        )