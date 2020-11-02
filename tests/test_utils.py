# -*- coding: utf-8 -*-
import unittest
import utils

class TestUtils(unittest.TestCase):
  def test_menu_items(self):
      self.assertEqual(
          hasattr(
              utils,
              'menu_items'
          ),
          True,
          "Utils não possui menu items"
      )

  def test_utils_has_this_path(self):
      self.assertEqual(
          hasattr(
              utils,
              'this_path'
          ),
          True,
          "Utils não possui this_path"
      )

  def test_utils_has_this_dir(self):
      self.assertEqual(
          hasattr(
              utils,
              'this_dir'
          ),
          True,
          "Utils não possui this_dir"
      )

  def test_utils_has_items_notebook(self):
      self.assertEqual(
          hasattr(
              utils,
              'items_notebook'
          ),
          True,
          "Utils não possui items_notebook"
      )