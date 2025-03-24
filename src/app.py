from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from uipython.calculator_screen import CalculatorScreen
from PyQt5.uic import loadUi
from typing import Self


class MainScreen(QMainWindow):

    def __init__(self) -> Self:
        super().__init__()
        loadUi("uixml/main_screen.ui", self)
        self.init_ui_components()


    def init_ui_components(self) -> None:
        # calculator screens
        self.main_screen: CalculatorScreen = self.findChild(CalculatorScreen, "expr_screen")
        self.result_screen: CalculatorScreen = self.findChild(CalculatorScreen, "res_screen")

        # function buttons
        self.clear_button: QPushButton = self.findChild(QPushButton, "button_clr")
        self.all_clear_button: QPushButton = self.findChild(QPushButton, "button_ac")

        # arithmetic operators
        self.percentage_button: QPushButton = self.findChild(QPushButton, "button_perc")
        self.division_button: QPushButton = self.findChild(QPushButton, "button_div")
        self.multiplication_button: QPushButton = self.findChild(QPushButton, "button_mul")
        self.subtraction_button: QPushButton = self.findChild(QPushButton, "button_min")
        self.addition_button: QPushButton = self.findChild(QPushButton, "button_add")
        self.equals_button: QPushButton = self.findChild(QPushButton, "button_eq")
        self.plus_minus_button: QPushButton = self.findChild(QPushButton, "button_pm")

        # digits and decimal point
        self.zero_button: QPushButton = self.findChild(QPushButton, "button_0")
        self.one_button: QPushButton = self.findChild(QPushButton, "button_1")
        self.two_button: QPushButton = self.findChild(QPushButton, "button_2")
        self.three_button: QPushButton = self.findChild(QPushButton, "button_3")
        self.four_button: QPushButton = self.findChild(QPushButton, "button_4")
        self.five_button: QPushButton = self.findChild(QPushButton, "button_5")
        self.six_button: QPushButton = self.findChild(QPushButton, "button_6")
        self.seven_button: QPushButton = self.findChild(QPushButton, "button_7")
        self.eight_button: QPushButton = self.findChild(QPushButton, "button_8")
        self.nine_button: QPushButton = self.findChild(QPushButton, "button_p")
        self.dot_button: QPushButton = self.findChild(QPushButton, "button_dot")


    def launch(self) -> None:
        self.show()


if __name__ == "__main__":

    app: QApplication = QApplication([])
    main: MainScreen = MainScreen()
    main.launch()
    app.exec_()

# eosc