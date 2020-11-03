import matplotlib.backends.backend_tkagg as plttk
import matplotlib.pyplot as plt
import tkinter as tk
from app_frame import AppFrame
from matplotlib import style

exchange = False
data = None
metadata = None

style.use("classic")

f, ax = plt.subplots(nrows=1, ncols=1)


def changeExchange(toWhat, pn):
    global exchange
    print(toWhat)
    exchange = toWhat


def changeExchangeData(dataToWhat, metadataTowhat):
    global data
    global metadata
    data = dataToWhat
    metadata = metadataTowhat


class TidalGraph(AppFrame):
    def __init__(self, parent, controller):
        AppFrame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.setup()

    def action(self):
        pass

    def setup(self):
        self.canvas = plttk.FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(
            side=tk.BOTTOM,
            fill=tk.BOTH,
            expand=tk.TRUE
        )

        self.toolbar = plttk.NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=tk.TRUE)

    def estilo(self, toWhat):
        plt.style.use(toWhat)
        print(toWhat)


def animate(i):
    x_ = []
    y_ = []
    if exchange == "mare":
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=6, colspan=6)
        for line in data.items():
            x, y = line
            x_.append(x)
            y_.append(y)
        a.plot(x_, y_)

    elif exchange == 'estatistica':
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=6, colspan=6)
        x = [1]
        y = [10]
        a.plot(x, y)
