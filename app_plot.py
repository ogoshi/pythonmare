import matplotlib.backends.backend_tkagg as plttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import tkinter as tk
from app_frame import AppFrame
from matplotlib import style
import matplotlib.dates as mdates
from collections import OrderedDict


exchange = False
data = None
metadata = None

style.use("classic")

LARGE_FONT = ("Verdana", 12)
width, height = plt.figaspect(1)


def changeExchange(toWhat, pn, obj):
    global exchange
    exchange = toWhat
    print(exchange)
    if exchange == 'mare':
        obj.plot_mare()
    elif exchange == 'normalizado':
        obj.plot_normalize()
    elif exchange == 'estatistica':
        obj.plot_statistic()


def changeExchangeData(dataToWhat, metadataTowhat):
    global data
    global metadata
    data = dataToWhat
    metadata = metadataTowhat


class TidalGraph(AppFrame):
    def __init__(self, parent, controller):
        self.parent = parent
        if self.parent:
            tk.Frame.__init__(self, parent)
            self.main = self.master

        self.globalopts = OrderedDict(
            {
                'dpi': 80,
                'grid layout': False,
                '3D plot': False
            }
        )

        pframe = tk.Frame(self.main)

        self.m = tk.PanedWindow(pframe, orient='vertical')
        self.m.pack(fill=tk.BOTH, expand=1)
        self.plotfr = tk.Frame(self.m)
        self.fig, self.canvas = add_figure(self.plotfr)
        self.ax = self.fig.add_subplot(111)
        self.canvas.draw()
        self.setup_gui()
        self._init_figure()

    def action(self):
        pass

    def update_style(self, toWhat):
        plt.style.use(toWhat)
        print(toWhat)

    def setup_gui(self):
        """Add GUI elements"""

        self.m = tk.PanedWindow(self, orient='vertical')
        self.m.pack(fill=tk.BOTH, expand=1)

        self.plotfr = tk.Frame(self.m)

        self.fig, self.canvas = add_figure(self.plotfr)
        self.ax = self.fig.add_subplot(111)

        self.m.add(self.plotfr)

        self.ctrlfr = tk.Frame(self.main)
        self.m.add(self.ctrlfr)
        self.m.pack(side=tk.LEFT,  expand=True)

    def _init_figure(self):
        self.fig.clear()
        self.gridaxes = {}
        self.ax = self.fig.add_subplot(111)
        self.ax.xaxis_date()
        locator = mdates.AutoDateLocator(minticks=5, maxticks=12)
        formatter = mdates.ConciseDateFormatter(locator)
        self.ax.xaxis.set_major_locator(locator)
        self.ax.xaxis.set_major_formatter(formatter)
        return

    def plot_mare(self):
        self._init_figure()
        self.ax.plot(data.df.index, data.df['data'])
        self.ax.set_title("{} {} {} {}".format(*metadata['Estacao']))
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_normalize(self):
        y_ = []
        self._init_figure()
        nivel_medio = float(metadata["Nivel medio"][0])
        for y in data.df['data']:
            y_.append(y-nivel_medio)
        self.ax.plot(data.df.index, y_)
        self.ax.set_title("{} {} {} {}".format(*metadata['Estacao']))
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_statistic(self):
        self._init_figure()
        df = data.df
        df_max = df.loc[df['data'] == df.max().data]
        df_min = df.loc[df['data'] == df.min().data]
        self.ax.plot(df.index.values, df.data.values, '-k')
        self.ax.plot(df_max.index.values, df_max.data.values, 'or')
        self.ax.plot(df_min.index.values, df_min.data.values, 'ob')
        self.canvas.draw()


def add_figure(parent, figure=None, resize_callback=None):
    if not figure:
        figure = Figure(facecolor='white')

    canvas = plttk.FigureCanvasTkAgg(
        figure,
        master=parent,
        resize_callback=resize_callback
        )
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=0)
    canvas.get_tk_widget().configure(
        highlightcolor='gray75',
        highlightbackground='gray75'
    )
    toolbar = plttk.NavigationToolbar2Tk(canvas, parent)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=0)
    return figure, canvas
