from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

import PySide6QtAds as QtAds
from PySide6QtAds import CDockManager, CDockWidget

from Managers.SDRManager import SDRManager
from Widgets.Configuration import Configuration
from Widgets.PlotWidget import Plot
from Widgets.SDRSettings import SDRSettings


class MainWindow(QMainWindow):
    __version__ = "24.3.9"

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f'RTLFFT v{self.__version__}')

        # Get managers
        self.sdr_manager = SDRManager()

        # Create Dock Widgets
        self.dock_manager = CDockManager(self)

        self.plot_dock_widget = CDockWidget("Plot")
        self.plot = Plot()
        self.plot_dock_widget.setWidget(self.plot)
        self.plot_dock_widget.setIcon(QPixmap("../Images/chart.png"))

        self.menuBar().addAction(self.plot_dock_widget.toggleViewAction())

        self.dock_manager.addDockWidget(QtAds.DockWidgetArea.TopDockWidgetArea, self.plot_dock_widget)

        self.sdr_settings_dock_widget = CDockWidget("SDR Settings")
        self.sdr_settings = SDRSettings()
        self.sdr_settings_dock_widget.setWidget(self.sdr_settings)

        self.menuBar().addAction(self.sdr_settings_dock_widget.toggleViewAction())

        self.dock_manager.addDockWidget(QtAds.DockWidgetArea.RightDockWidgetArea, self.sdr_settings_dock_widget)

        self.configuration_dock_widget = CDockWidget("Configuration")
        self.configuration = Configuration()
        self.configuration_dock_widget.setWidget(self.configuration)

        self.menuBar().addAction(self.configuration_dock_widget.toggleViewAction())


        # self.dock_manager.addDockWidget(QtAds.DockWidgetArea.BottomDockWidgetArea,)
        self.configuration_dock_widget.toggleViewAction()


        self.create_connections()

    def create_connections(self):
        # SDR Data
        self.sdr_manager.new_data.connect(self.plot.plot)

        # SDR Settings
        self.sdr_settings.ss_start.connect(self.sdr_manager.start_gather_data)
        self.sdr_settings.ss_stop.connect(self.sdr_manager.stop_gather_data)
        self.sdr_settings.gain_changed.connect(self.sdr_manager.sdr.set_gain)