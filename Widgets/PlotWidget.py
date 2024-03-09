import pyqtgraph as pg

from Widgets.AbstractWidget import AbstractWidget


class Plot(AbstractWidget):

    def __init__(self):
        AbstractWidget.__init__(self)

        self.graph_widget = pg.PlotWidget()
        self.graph_widget.setMouseEnabled(x=False, y=False)
        self.plotLine = self.graph_widget.plot([0])

        self.layout.addWidget(self.graph_widget, 0, 0)

    def plot(self, xdata, ydata):
        self.plotLine.setData(ydata, xdata)