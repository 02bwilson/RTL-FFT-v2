"""
ConfigurationWidget.py

Bryce W, 2024
"""
from PySide6.QtWidgets import QPushButton

from Widgets.AbstractWidget import AbstractWidget


class Configuration(AbstractWidget):

    def __init__(self):
        super().__init__()

        self.save_config_button = QPushButton("Save Configuration")

        self.load_config_button = QPushButton("Load Configuration")


        self.layout.addWidget(self.save_config_button, 0, 0)
        self.layout.addWidget(self.load_config_button, 1, 0)