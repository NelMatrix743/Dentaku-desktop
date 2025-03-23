from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from uipython.calculator_screen import CalculatorScreen
from PyQt5.uic import loadUi
from typing import Self


class MainScreen(QMainWindow):

    def __init__(self) -> Self:
        super().__init__()
        loadUi("uixml/main_screen.ui", self)

    def launch(self) -> None:
        self.show()


if __name__ == "__main__":

    app: QApplication = QApplication([])
    main: MainScreen = MainScreen()
    main.launch()
    app.exec_()

# eosc
