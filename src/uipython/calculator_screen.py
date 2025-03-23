from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class CalculatorScreen(QLabel):
# custom QLabel to handle text changes from math expressions and results

    textChanged = pyqtSignal(str)

    def setText(self, text: str) -> None:
	    # If the expression on screen changes, emit a signal
        if text != self.text():
            super().setText(text)
            self.textChanged.emit(text)

# eosc
