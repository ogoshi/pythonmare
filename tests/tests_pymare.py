# -*- coding: utf-8 -*-
import os
from io import TextIOWrapper
import unittest
from pymare import main
import tkinter as tk

class TestMain(unittest.TestCase):
    def test_configure_app_data(self):
        self.assertEqual(
            hasattr(
                main,
                'configure_app_data'
            ),
            True,
            "Não possui config data app"
        )

    def test_configure_app(self):
        self.assertEqual(
            hasattr(
                main,
                'configure_app'
            ),
            True,
            "Não possui configure app"
        )

    def test_configure_app_return_root(self):
        self.assertIsInstance(
            main.configure_app(),
            tk.Tk,
            "Não retorna um Tk Root!"
        )