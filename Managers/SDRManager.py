import threading

from PySide6.QtCore import QObject, Signal as QSignal, QThread

from rtlsdr import RtlSdr

from numpy import fft, log


class SDRManager(QObject):
    new_data = QSignal(list, list)

    def __init__(self):
        super().__init__()

        self.sdr = RtlSdr()

        # Set default settings
        self.sdr.set_gain(10)
        self.sdr.set_bandwidth(3e6)
        self.sdr.set_center_freq(100e6)
        self.sdr.set_sample_rate(1024e3)

        self.data_flag = False


    def start_gather_data(self):
        self.data_flag = True
        data_thread = threading.Thread(target=self.gather_data)
        data_thread.daemon = True
        data_thread.start()

    def stop_gather_data(self):
        self.data_flag = False

    def gather_data(self):
        while self.data_flag:
            cf = self.sdr.get_center_freq()
            bw = self.sdr.get_bandwidth()
            freq_list = []
            inc = 0
            low = cf - (bw / 2)
            hi = cf + (bw /2)
            while low + inc < hi:
                freq_list.append(low + inc)
                inc += bw / 1024
            samples = self.sdr.read_samples(1024)
            samples = fft.fft(samples)
            #print(samples)
            samples = [10 * log((s.real * s.real) + (s.imag * s.imag)) for s in samples]
            self.new_data.emit(freq_list, samples)
