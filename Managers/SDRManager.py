import threading

from PySide6.QtCore import QObject, Signal as QSignal, QThread

from rtlsdr import RtlSdr


class SDRManager(QObject):
    # FFT Data, Center Freq, BW
    new_data = QSignal(list, list)

    def __init__(self):
        super().__init__()

        self.sdr = RtlSdr()

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
            print(self.sdr.get_gain())
            # print(self.sdr.get_sample_rate() / 500)
            # self.new_data.emit(self.sdr.read_samples(2), self.sdr.get_sample_rate(), self.sdr.get_bandwidth())
