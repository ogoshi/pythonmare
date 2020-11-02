"""
Modulo para processar dados de marÃ©

Aluno: Itamar Almeida de Oliveira
Data 01/11/2020
Curso: Oceanografia UERJ
"""
import os
import re
from datetime import datetime

thisPath = os.path.realpath('__file__')
thisDir = os.path.dirname(thisPath)


class TidalData(object):
    def __init__(self, filename):
        self.__filename = filename
        self.read_arqv()
        self.values = []

    def read_arqv(self):
        self.arqv = open(self.__filename).readlines()

    def process_line(self, values):
        return [item.split() for item in values]

    def search_line(self, result, expre):
        self.read_arqv()
        r = re.compile(expre)
        return [line for line in self.arqv if r.match(line) is not result]

    def get_data_from_file(self):
        data = self.format_date(
            self.process_line(
                self.remove_broken_line(
                    self.search_line(
                        None,
                        '.*/.*/.*.*:.*.*'
                    )
                )
            )
        )
        return data

    def get_metadata(self):
        md = self.remove_broken_line(self.search_line(None, '.* .*: .* .*'))
        metadata = {}
        for m in md:
            k, v = m.split(':')
            metadata[k] = v
        return metadata

    def remove_broken_line(self, values):
        return [item.strip(' ').strip('\n') for item in values]

    def format_date(self, data):
        date_temp = []
        for line in data:
            date_temp.append(
                [
                    datetime.strptime(
                        "{} {}".format(
                            line[0],
                            line[1]
                        ),
                        r'%d/%m/%Y %H:%M'
                    ),
                    line[2]
                ]
            )
        return date_temp