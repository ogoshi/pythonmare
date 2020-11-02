"""Modulo para processamento dos dados"""
from tidal_data import TidalData
from app import PythonMareApplication


class Main:
    def configure_app_data(self, filename):
        td = TidalData(filename)

        self.data = td.data2dict()
        self.metadata = td.get_metadata()

    def configure_app(self):
        app = PythonMareApplication()
        return app


main = Main()


if __name__ == "__main__":

    app = main.configure_app()
    app.mainloop()
