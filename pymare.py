"""Modulo para processamento dos dados"""
from tidalData import TidalData
from pprint import pprint


class Main:
    def configure_app_data(self, filename):
        td = TidalData(filename)

        self.data = td.data2dict()
        self.metadata = td.get_metadata()
        pprint(self.data)
        pprint(self.metadata)


main = Main()


if __name__ == "__main__":

    main.configure_app_data("prev_201110.txt")
