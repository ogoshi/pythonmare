import os
from io import TextIOWrapper
import unittest
from tidalData import TidalData
from datetime import datetime


thisPath = os.path.realpath('__file__')
thisDir = os.path.dirname(thisPath)


class TestDataTital(unittest.TestCase):
    filename = r"prev_201110.txt"
    tidal = TidalData(filename)

    def test_input(self):
        self.assertNotIsInstance(
            type(self.tidal.arqv),
            TextIOWrapper,
            "Nao eh um tipo valido de entrada de texto!")

    def test_read_data(self):
        self.tidal.get_data_from_file()

    def test_values(self):
        self.assertIsInstance(
            self.tidal.get_data_from_file(),
            list,
            "nao eh uma lista!"
        )

    def test_exist_metadata(self):
        self.assertEqual(
            hasattr(self.tidal, 'get_metadata'),
            True,
            "Nao existe atributo metadata!")

    def test_metadata_has_lines(self):
        self.assertEqual(
            len(self.tidal.get_metadata()) > 0,
            True,
            "Nao existe linhas"
        )

    def test_remove_broken_line_exist(self):
        self.assertEqual(
            hasattr(self.tidal, "remove_broken_line"),
            True,
            "Nao existe dados possuem quebra de linha!"
        )

    def test_remove_broken_line_is_list(self):
        self.assertIsInstance(
            self.tidal.get_data_from_file(),
            list,
            str(self.tidal.get_data_from_file())
        )

    def test_process_line_exist(self):
        self.assertEqual(
            hasattr(self.tidal, "process_line"),
            True,
            "Nao existe Process Line!"
        )

    def test_format_date(self):
        self.assertEqual(hasattr(self.tidal, 'format_date'), True, "nao possui format date")
        for line in self.tidal.get_data_from_file():
            self.assertIsInstance(line[0], datetime, line[0])

    def test_char_in_line(self):
        for line in self.tidal.get_data_from_file():
            self.assertEqual(
                "\n" in line,
                False,
                "linha sem tratamento"
        )

        for line in self.tidal.get_metadata():
            self.assertEqual(
                "\n" in line,
                False,
                "linha sem tratamento"
        )

    def test_metadata_is_dict(self):
        self.assertIsInstance(
            self.tidal.get_metadata(),
            dict,
            "nao eh uma collection"
        )

    def test_dict_metadata_has_attrbs(self):
        self.assertEqual(
            len(self.tidal.get_metadata().keys()),
            10,
            str(self.tidal.get_metadata().keys())
        )

    def test_get_station_name(self):
        pass