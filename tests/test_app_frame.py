# -*- coding: utf-8 -*-
import unittest
import app_frame
import tkinter as tk


class TestAppFrame(unittest.TestCase):
    """
    docstring: class para testar frames
    """
    frame = app_frame.AppFrame(None)

    def test_app_frame_is_tk_frame(self):
        self.assertIsInstance(
            self.frame,
            tk.Frame,
            "Não é um tipo tk.Frame"
        )

    def test_app_frame_hasattr(self):
        l1 = [
            'create_top_level_item',
            'add_button'
        ]

        s = "Não possui o seguinte atributo: {}"

        for attr in l1:
            self.assertEqual(
                hasattr(self.frame, attr),
                True,
                s.format(attr)
            )
