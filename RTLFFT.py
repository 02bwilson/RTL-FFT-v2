"""
RTLFFT.py

Bryce W, 2024
"""
import sys

from PySide6.QtWidgets import QApplication

from Widgets.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
