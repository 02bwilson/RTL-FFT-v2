from PySide6.QtGui import QDoubleValidator

from Widgets.AbstractWidget import AbstractWidget

from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Signal as QSignal


class SDRSettings(AbstractWidget):
    ss_start = QSignal()
    ss_stop = QSignal()
    gain_changed = QSignal(float)
    freq_changed = QSignal(float)
    sr_changed = QSignal(float)
    iir_alpha_changed = QSignal(float)

    def __init__(self):
        AbstractWidget.__init__(self, layout=QFormLayout)

        # Start Button
        self.ss_state = False
        self.ss_button = QPushButton("Start")
        self.ss_button.pressed.connect(self.handle_ss_pressed)

        # Labels
        self.freq_label = QLabel("Center Frequency [MHz]")
        self.gain_label = QLabel("Gain [dB]")
        self.sr_label = QLabel("Sample Rate [MSPS]")
        self.iir_alpha_label = QLabel("IIR Alpha")
        self.plot_rr_label = QLabel("Plot Refresh Rate [MS]")

        # Line Edits
        self.freq_line_edit = QLineEdit("103.1")
        self.freq_line_edit.setValidator(QDoubleValidator())
        self.freq_line_edit.returnPressed.connect(
            lambda: self.freq_changed.emit(float(self.freq_line_edit.text()) * 1e6))

        self.gain_line_edit = QLineEdit("0")
        self.gain_line_edit.setValidator(QDoubleValidator())
        self.gain_line_edit.returnPressed.connect(lambda: self.gain_changed.emit(float(self.gain_line_edit.text())))

        self.sr_line_edit = QLineEdit("1.024")
        self.sr_line_edit.setValidator(QDoubleValidator())
        self.sr_line_edit.returnPressed.connect(lambda: self.sr_changed.emit(float(self.sr_line_edit.text()) * 1e6))

        self.iir_alpha_line_edit = QLineEdit(".99")
        self.iir_alpha_line_edit.setValidator(QDoubleValidator())
        self.iir_alpha_line_edit.returnPressed.connect(
            lambda: self.iir_alpha_changed.emit(float(self.iir_alpha_line_edit.text())))

        self.plot_rr_line_edit = QLineEdit()
        self.plot_rr_line_edit.setPlaceholderText("1")

        # Setup Layout
        self.layout.addRow(self.ss_button)
        self.layout.addRow(self.freq_label, self.freq_line_edit)
        self.layout.addRow(self.gain_label, self.gain_line_edit)
        self.layout.addRow(self.sr_label, self.sr_line_edit)
        self.layout.addRow(self.iir_alpha_label, self.iir_alpha_line_edit)
        self.layout.addRow(self.plot_rr_label, self.plot_rr_line_edit)

    def handle_ss_pressed(self):
        if not self.ss_state:
            self.ss_start.emit()
            self.ss_button.setText("Stop")
            self.ss_state = not self.ss_state
        else:
            self.ss_stop.emit()
            self.ss_button.setText("Start")
            self.ss_state = not self.ss_state
