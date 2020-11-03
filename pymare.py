"""Modulo para processamento dos dados"""
from tidal_data import TidalData
from app import PythonMareApplication
import matplotlib.animation as animation
from app_plot import f, animate


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
    app.eval('tk::PlaceWindow . center')
    ani = animation.FuncAnimation(f, animate, interval=300)
    app.mainloop()
