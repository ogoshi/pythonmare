"""
Modulo para processar dados de mare

Aluno: Itamar Almeida de Oliveira
Data 01/11/2020
Curso: Oceanografia UERJ
"""
import os
import re
from datetime import datetime, timedelta
import pytz
from core import TableModel
import pandas as pd
thisPath = os.path.realpath('__file__')
thisDir = os.path.dirname(thisPath)


class TidalData(object):
    def __init__(self, filename):
        self.__filename = filename
        self.read_arqv()
        self.values = []

    def read_arqv(self):
        arqv = open(self.__filename)
        self.arqv = arqv.readlines()
        arqv.close()

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
            metadata[k] = v.strip(" ").split()
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

    def data2dict(self):
        dict_temp = {}
        tz = float(self.get_metadata()['Fuso'][0])
        for line in self.get_data_from_file():
            k, v = line
            k = pytz.utc.localize(k)
            dict_temp[k + timedelta(hours=-tz)] = float(v)
        data_d = {
            "time": list(dict_temp.keys()),
            "data": list(dict_temp.values())
        }
        df_data = TableModel(pd.DataFrame.from_dict(data_d))
        df_data.setindex("time")
        df_metadata = {}
        return df_data
