from PySide6.QtWidgets import QWidget, QGridLayout

class AbstractWidget(QWidget):
    """

    """

    def __init__(self, *args, **kwargs):
        """
        Creates an abstract widget.
        :param args:
        :param kwargs:
        """
        super().__init__()

        parent = kwargs.pop('parent', None)
        self.parent = parent

        _layout = kwargs.pop('layout', QGridLayout)
        self.layout = _layout()
        self.setLayout(self.layout)