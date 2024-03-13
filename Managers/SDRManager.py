import threading
import time

from PySide6.QtCore import QObject, Signal as QSignal, QThread

from rtlsdr import RtlSdr

from numpy import fft, log
import numpy as np
from scipy.interpolate import make_interp_spline

from scipy.signal import resample_poly, firwin, bilinear, lfilter

class SDRManager(QObject):
    new_fft_data = QSignal(list, list)
    new_iq_data = QSignal(list)
    def __init__(self):
        super().__init__()

        self.sdr = RtlSdr()

        # Set default settings
        self.sdr.set_gain(10)
        self.sdr.set_bandwidth(1.024e3)
        self.sdr.set_center_freq(103.1e6)
        self.sdr.set_sample_rate(1024e3)

        self.iir_data = []

        self.alpha = .99

        self.data_flag = False

    def set_iir_alpha(self, alpha):
        self.alpha = float(alpha)

    def start_gather_data(self):
        self.data_flag = True
        data_thread = threading.Thread(target=self.gather_data)
        data_thread.daemon = True
        data_thread.start()

    def stop_gather_data(self):
        self.data_flag = False

    def gather_data(self):
        while self.data_flag:
            time.sleep(.01)
            # Get the center freq and bandwidth
            cf = self.sdr.get_center_freq()
            bw = 1024e3

            # Create the freq list
            freq_list = []
            inc = 0
            low = cf - (bw / 2)
            hi = cf + (bw / 2)
            while low + inc < hi:
                freq_list.append(low + inc)
                inc += bw / 2048
            freq_list = freq_list[1:]

            # Read samples
            samples = self.sdr.read_samples(2048)

            self.new_iq_data.emit(samples)

            samples = fft.fft(samples)
            samples = samples[1:]
            samples = fft.fftshift(samples)
            samples = [10 * log(10 * ((s.real * s.real) + (s.imag * s.imag))) for s in samples]


            # Send throgh IIR Filter
            if len(self.iir_data) == 0:
                self.iir_data = samples
            else:
                for idx, s in enumerate(samples):
                    oma = 1 - self.alpha
                    self.iir_data[idx] = s * oma + self.iir_data[idx] * self.alpha


            # Send to plot
            self.new_fft_data.emit(freq_list, self.iir_data)


