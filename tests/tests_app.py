# -*- coding: utf-8 -*-
import os
from io import TextIOWrapper
import unittest
from app import PythonMareApplication
import tkinter as tk


class TestCaseApp(unittest.TestCase):
    def test_app_is_tk_app(self):
        self.assertIsInstance(
            PythonMareApplication(),
            tk.Tk,
            "Não é uma instancia de TK!!"
        )

    def test_app_has_frames(self):
        self.assertEqual(
            hasattr(
                PythonMareApplication(),
                "frames"
            ),
            True,
            "Aplicativo não possui atributo frames!" 
        )

    def test_app_has_any_frames(self):
        self.assertEqual(
            len(PythonMareApplication().frames.values())>0,
            True,
            "Aplicativo não possui nenhum frames!" 
        )

    def test_app_has_setup_menu(self):
        self.assertEqual(
            hasattr(
                PythonMareApplication(),
                "setup_menu"
            ),
            True,
            "Aplicativo não possui method de criar menus!" 
        )


    def test_app_has_make_notebook(self):
        self.assertEqual(
            hasattr(
                PythonMareApplication(),
                "make_notebook"
            ),
            True,
            "Aplicativo não cria notebook!" 
        )