"""
IQPlotWidget.py

Bryce W, 2024
"""
import pyqtgraph as pg
pg.setConfigOptions(antialias=True)
from Widgets.AbstractWidget import AbstractWidget


class PW(pg.PlotItem):

    def __init__(self):
        pg.PlotItem.__init__(self)

    def setAxisItems(self, axisItems):
        pg.PlotItem.setAxisItems(self, axisItems)
class IQPlot(AbstractWidget):

    def __init__(self):
        AbstractWidget.__init__(self)

        self.graph_widget = pg.PlotWidget(plotItem=PW())
        self.graph_widget.setMouseEnabled(x=False, y=False)

        self.plotLine = pg.ScatterPlotItem()
        self.graph_widget.addItem(self.plotLine)

        self.layout.addWidget(self.graph_widget, 0, 0)

        self.graph_widget.setXRange(.05, -.05)
        self.graph_widget.setYRange(.05, -.05)


    def plot(self, data):
        i = [s.real for s in data]
        q = [s.imag for s in data]
        self.plotLine.setData(x=i, y=q)
