from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt6.QtGui import QFontMetrics, QFont


class CalculatorScreen(QLabel):
# custom QLabel to handle text changes from math expressions and results

    textChanged = pyqtSignal(str)

    def __init__(self, text):
        super().__init__(text)
        self.setWordWrap(True)
        self.setSizePolicy(self.sizePolicy().Preferred, self.sizePolicy().Minimum)
        self.adjustSize()

    def setText(self, text: str) -> None:
	    # If the expression on screen changes, emit a signal
        if text != self.text():
            super().setText(text)
            self.textChanged.emit(text)

# eosc
