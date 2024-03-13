"""
SDRSettingsWidget.py

Bryce W, 2024
"""

from PySide6.QtGui import QDoubleValidator, QIntValidator

from Widgets.AbstractWidget import AbstractWidget

from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PySide6.QtCore import Signal as QSignal


class SDRSettings(AbstractWidget):
    ss_start = QSignal()
    ss_stop = QSignal()

    freq_changed = QSignal(float)
    freq_correction_changed = QSignal(float)
    sr_changed = QSignal(float)
    bw_changed = QSignal(float)
    gain_changed = QSignal(float)
    agc_changed = QSignal(bool)
    bias_tee_changed = QSignal(bool)
    direct_sampling_changed = QSignal(bool)

    rr_changed = QSignal(int)
    iir_alpha_changed = QSignal(float)

    def __init__(self):
        AbstractWidget.__init__(self, layout=QFormLayout)

        # Start Button
        self.ss_state = False
        self.ss_button = QPushButton("Start")
        self.ss_button.pressed.connect(self.handle_ss_pressed)

        # Labels
        self.freq_label = QLabel("Center Frequency [MHz]")
        self.freq_correction_label = QLabel("Frequency Correction [PPM]")
        self.sr_label = QLabel("Sample Rate [MSPS]")
        self.bw_label = QLabel("Bandwidth [Hz]")
        self.gain_label = QLabel("Gain [dB]")
        self.agc_label = QLabel("AGC Enable")
        self.bias_tee_label = QLabel("Bias Tee Enable")
        self.direct_sampling_label = QLabel("Direct Sampling Enable")

        self.plot_rr_label = QLabel("Plot Refresh Rate [MS]")
        self.iir_alpha_label = QLabel("IIR Alpha")

        # Line Edits

        # Center Freq
        self.freq_line_edit = QLineEdit("103.1")
        self.freq_line_edit.setValidator(QDoubleValidator())
        self.freq_line_edit.returnPressed.connect(
            lambda: self.freq_changed.emit(float(self.freq_line_edit.text()) * 1e6))

        # Freq Correction
        self.freq_correction_line_edit = QLineEdit("1")
        self.freq_correction_line_edit.setValidator(QIntValidator())
        self.freq_correction_line_edit.returnPressed.connect(
            lambda: self.freq_correction_changed.emit(int(self.freq_correction_line_edit.text())))

        # Sample Rate
        self.sr_line_edit = QLineEdit("1.024")
        self.sr_line_edit.setValidator(QDoubleValidator())
        self.sr_line_edit.returnPressed.connect(
            lambda: self.sr_changed.emit(float(self.sr_line_edit.text()) * 1e6))

        # Bandwidth
        self.bw_line_edit = QLineEdit("200000")
        self.bw_line_edit.setValidator(QDoubleValidator())
        self.bw_line_edit.returnPressed.connect(
            lambda: self.bw_changed.emit(float(self.sr_line_edit.text())))

        # Gain
        self.gain_line_edit = QLineEdit("0")
        self.gain_line_edit.setValidator(QDoubleValidator())
        self.gain_line_edit.returnPressed.connect(
            lambda: self.gain_changed.emit(float(self.gain_line_edit.text())))

        # AGC
        self.agc_combo_box = QComboBox()
        self.agc_combo_box.addItems(["False", "True"])
        self.agc_combo_box.currentIndexChanged.connect(
            lambda: self.agc_changed.emit(bool(self.agc_combo_box.currentText())))

        # Bias Tee
        self.bias_tee_combo_box = QComboBox()
        self.bias_tee_combo_box.addItems(["False", "True"])
        self.bias_tee_combo_box.currentIndexChanged.connect(
            lambda: self.bias_tee_changed.emit(bool(self.bias_tee_combo_box.currentText())))

        # Direct Sampling
        self.direct_sampling_combo_box = QComboBox()
        self.direct_sampling_combo_box.addItems(["False", "True"])
        self.direct_sampling_combo_box.currentIndexChanged.connect(
            lambda: self.direct_sampling_changed.emit(bool(self.direct_sampling_combo_box.currentText())))

        # IIR Alpha
        self.iir_alpha_line_edit = QLineEdit(".99")
        self.iir_alpha_line_edit.setValidator(QDoubleValidator())
        self.iir_alpha_line_edit.returnPressed.connect(
            lambda: self.iir_alpha_changed.emit(float(self.iir_alpha_line_edit.text())))

        # Plot Refresh Rate
        self.plot_rr_line_edit = QLineEdit()
        self.plot_rr_line_edit.setPlaceholderText("1")

        # Setup Layout
        self.layout.addRow(self.ss_button)
        self.layout.addRow(self.freq_label, self.freq_line_edit)
        self.layout.addRow(self.freq_correction_label, self.freq_correction_line_edit)
        self.layout.addRow(self.sr_label, self.sr_line_edit)
        self.layout.addRow(self.bw_label, self.bw_line_edit)
        self.layout.addRow(self.gain_label, self.gain_line_edit)
        self.layout.addRow(self.agc_label, self.agc_combo_box)
        self.layout.addRow(self.bias_tee_label, self.bias_tee_combo_box)
        self.layout.addRow(self.direct_sampling_label, self.direct_sampling_combo_box)

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
