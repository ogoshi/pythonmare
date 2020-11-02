# -*- coding: utf-8 -*-
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
            "Não é um tipo válido de entrada de texto!")

    def test_read_data(self):
        self.tidal.get_data_from_file()

    def test_values(self):
        self.assertIsInstance(
            self.tidal.get_data_from_file(),
            list,
            "não é uma lista!"
        )

    def test_exist_metadata(self):
        self.assertEqual(
            hasattr(self.tidal, 'get_metadata'),
            True,
            "Não existe atributo metadata!")

    def test_metadata_has_lines(self):
        self.assertEqual(
            len(self.tidal.get_metadata()) > 0,
            True,
            "Não existe linhas!"
        )

    def test_remove_broken_line_exist(self):
        self.assertEqual(
            hasattr(self.tidal, "remove_broken_line"),
            True,
            "Dados possuem quebra de linha!"
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
            "Não existe func process_line!"
        )

    def test_format_date(self):
        self.assertEqual(
            hasattr(
                self.tidal,
                'format_date'
            ),
            True,
            "não possui format date"
        )
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

    def test_data_from_file_is_dict(self):
        self.assertEqual(
            type(self.tidal.data2dict()),
            dict,
            "não é um dicionario!"
        )

    def test_data2dict(self):
        self.assertEqual(
            hasattr(
                self.tidal,
                'data2dict'
            ),
            True,
            "Não existe data2dict!!"
        )

    def test_water_level_is_float(self):
        for k, v in self.tidal.data2dict().items():
            self.assertIsInstance(v, float, "data type has must be a float!")

    def test_water_level_is_digit(self):
        for line in self.tidal.get_data_from_file():
            self.assertEqual(
                line[1].isdigit(),
                False,
                "date dont is digit!"
            )

    def test_tzinfo_from_date(self):
        for k, v in self.tidal.data2dict().items():
            self.assertEqual(k.tzinfo != None, True, 'Time zona não definido!!')

    def test_metadata_value_is_list(self):
        for k, v in self.tidal.get_metadata().items():
            self.assertIsInstance(v, list, "valores do metadata nao eh uma lista")