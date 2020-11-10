#-*- encoding: utf-8 -*-
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
    df = data.df
    if exchange == 'mare':
        obj.plot_line(df.index, df.data)
    elif exchange == 'normalizado':
        nivel_medio = float(metadata["Nivel medio"][0])
        obj.plot_line(df.index, df.data-nivel_medio)
    elif exchange == 'Max - Min':
        print("Max: {}m\n".format(df.max().data))
        print("Min: {}m\n".format(df.min().data))
        print('Média = {:.2f}m\n'.format(df.mean().data))
        print('Desvio Padrãoo = {:.3f}m\n'.format(df.std().data))
        print('Variancia = {:.3f}m'.format(df.std().data**2))

        fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

        ax1.plot(df.index, df['data'].values)
        ax2.plot(df.index, df['data'].values-df.mean().data)
        ax1.set_title("{} {} {} {}".format(*metadata['Estacao']))
        ax1.set_ylabel("Nível de Maré (m)")
        ax2.set_ylabel("Nível de Maré (m)")
        ax2.set_xlabel("Data/Hora")
        plt.show()


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

    def plot_line(self, x, y):
        self._init_figure()
        self.ax.plot(x, y)
        self.ax.set_title("{} {} {} {}".format(*metadata['Estacao']))
        self.fig.tight_layout()
        self.canvas.draw()

    def estilo(self, toWhat):
        plt.style.use(toWhat)
        self._init_figure()


def add_figure(parent, figure=None, resize_callback=None):
    if not figure:
        figure = Figure(facecolor='white')

    canvas = plttk.FigureCanvasTkAgg(
        figure,
        master=parent,
        resize_callback=resize_callback
        )
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)
    canvas.get_tk_widget().configure(
        highlightcolor='gray75',
        highlightbackground='gray75'
    )
    toolbar = plttk.NavigationToolbar2Tk(canvas, parent)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
    return figure, canvas
