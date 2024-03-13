from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

import PySide6QtAds as QtAds
from PySide6QtAds import CDockManager, CDockWidget

from Managers.SDRManager import SDRManager
from Widgets.ConfigurationWidget import Configuration
from Widgets.FFTPlotWidget import FFTPlot
from Widgets.IQPlotWidget import IQPlot
from Widgets.SDRSettingsWidget import SDRSettings


class MainWindow(QMainWindow):
    __version__ = "24.3.9"

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f'RTLFFT v{self.__version__}')

        # Get managers
        self.sdr_manager = SDRManager()

        # Create Dock Widgets
        self.dock_manager = CDockManager(self)

        self.fft_plot_dock_widget = CDockWidget("FFT Plot")
        self.fft_plot = FFTPlot()
        self.fft_plot_dock_widget.setWidget(self.fft_plot)
        self.fft_plot_dock_widget.setIcon(QPixmap("../Images/chart.png"))

        self.menuBar().addAction(self.fft_plot_dock_widget.toggleViewAction())

        self.dock_manager.addDockWidget(QtAds.DockWidgetArea.TopDockWidgetArea, self.fft_plot_dock_widget)

        self.iq_plot_dock_widget = CDockWidget("IQ Plot")
        self.iq_plot = IQPlot()
        self.iq_plot_dock_widget.setWidget(self.iq_plot)
        self.iq_plot_dock_widget.setIcon(QPixmap("../Images/chart.png"))

        self.menuBar().addAction(self.iq_plot_dock_widget.toggleViewAction())

        self.dock_manager.addDockWidget(QtAds.DockWidgetArea.BottomDockWidgetArea, self.iq_plot_dock_widget)

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
        self.sdr_manager.new_fft_data.connect(self.fft_plot.plot)
        self.sdr_manager.new_iq_data.connect(self.iq_plot.plot)

        # SDR Settings
        self.sdr_settings.freq_changed.connect(self.sdr_manager.sdr.set_center_freq)
        self.sdr_settings.ss_start.connect(self.sdr_manager.start_gather_data)
        self.sdr_settings.ss_stop.connect(self.sdr_manager.stop_gather_data)
        self.sdr_settings.gain_changed.connect(self.sdr_manager.sdr.set_gain)
        self.sdr_settings.iir_alpha_changed.connect(self.sdr_manager.set_iir_alpha)
        self.sdr_settings.sr_changed.connect(self.sdr_manager.sdr.set_sample_rate)
