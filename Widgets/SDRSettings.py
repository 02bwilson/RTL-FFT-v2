from PySide6.QtGui import QDoubleValidator

from Widgets.AbstractWidget import AbstractWidget

from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Signal as QSignal


class SDRSettings(AbstractWidget):

    ss_start = QSignal()
    ss_stop = QSignal()
    gain_changed = QSignal(float)
    def __init__(self):
        AbstractWidget.__init__(self, layout=QFormLayout)

        # Start Button
        self.ss_state = False
        self.ss_button = QPushButton("Start")
        self.ss_button.pressed.connect(self.handle_ss_pressed)


        # Labels
        self.gain_label = QLabel("Gain [dB]")
        self.sr_label = QLabel("Sample Rate [MSPS]")
        self.plot_rr_label = QLabel("Plot Refresh Rate [MS/S]")

        # Line Edits
        self.gain_line_edit = QLineEdit()
        self.gain_line_edit.setValidator(QDoubleValidator())
        self.gain_line_edit.returnPressed.connect(lambda: self.gain_changed.emit(float(self.gain_line_edit.text())))

        self.sr_line_edit = QLineEdit()

        self.plot_rr_line_edit = QLineEdit()
        self.plot_rr_line_edit.setPlaceholderText("1")


        # Setup Layout
        self.layout.addRow(self.ss_button)
        self.layout.addRow(self.gain_label, self.gain_line_edit)
        self.layout.addRow(self.sr_label, self.sr_line_edit)
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