import pyqtgraph as pg
pg.setConfigOptions(antialias=True)
from Widgets.AbstractWidget import AbstractWidget


class PW(pg.PlotItem):

    def __init__(self):
        pg.PlotItem.__init__(self)

    def setAxisItems(self, axisItems):
        pg.PlotItem.setAxisItems(self, axisItems)
class FFTPlot(AbstractWidget):

    def __init__(self):
        AbstractWidget.__init__(self)

        self.graph_widget = pg.PlotWidget(plotItem=PW())
        self.graph_widget.setMouseEnabled(x=False, y=False)
        self.plotLine = self.graph_widget.plot()

        self.layout.addWidget(self.graph_widget, 0, 0)

        self.graph_widget.setYRange(-55, 30)
    def plot(self, xdata, ydata):
        self.plotLine.setData(xdata , ydata)