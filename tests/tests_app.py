# -*- coding: utf-8 -*-
import unittest
from app import PythonMareApplication
import tkinter as tk


class TestCaseApp(unittest.TestCase):
    def test_app_is_tk_app(self):
        self.assertIsInstance(
            PythonMareApplication(),
            tk.Tk,
            "N�o � uma instancia de TK!!"
        )

    def test_app_has_frames(self):
        self.assertEqual(
            hasattr(
                PythonMareApplication(),
                "frames"
            ),
            True,
            "Aplicativo n�o possui atributo frames!"
        )

    def test_app_has_any_frames(self):
        self.assertEqual(
            len(PythonMareApplication().frames.values()) > 0,
            True,
            "Aplicativo n�o possui nenhum frames!"
        )

    def test_app_has_setup_menu(self):
        self.assertEqual(
            hasattr(
                PythonMareApplication(),
                "setup_menu"
            ),
            True,
            "Aplicativo n�o possui method de criar menus!"
        )

    def test_app_has_make_notebook(self):
        self.assertEqual(
            hasattr(
                PythonMareApplication(),
                "make_notebook"
            ),
            True,
            "Aplicativo n�o cria notebook!"
        )

    def test_app_has_setup_frames(self):
        self.assertEqual(
            hasattr(
                PythonMareApplication(),
                "setup_frames"
            ),
            True,
            "Aplicativo n�o cria instala os frames!"
        )
