from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from uipython.calculator_screen import CalculatorScreen
from  collections.abc import Callable
from functools import partial
from PyQt5.uic import loadUi
from typing import Self
from utils.util_functions import (
    insert_digit,
    clear_last_input,
    clear_screen,
    insert_decimal_point,
    insert_operator
)


class MainScreen(QMainWindow):

    def __init__(self) -> Self:
        super().__init__()
        loadUi("uixml/main_screen.ui", self)
        self.setup_ui_components()


    def setup_ui_components(self) -> None:
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
        self.nine_button: QPushButton = self.findChild(QPushButton, "button_9")
        self.dot_button: QPushButton = self.findChild(QPushButton, "button_dot")

        # map buttons to functions
        self.map_function(self.zero_button, insert_digit, "0")
        self.map_function(self.one_button, insert_digit, "1")
        self.map_function(self.two_button, insert_digit, "2")
        self.map_function(self.three_button, insert_digit, "3")
        self.map_function(self.four_button, insert_digit, "4")
        self.map_function(self.five_button, insert_digit, "5")
        self.map_function(self.six_button, insert_digit, "6")
        self.map_function(self.seven_button, insert_digit, "7")
        self.map_function(self.eight_button, insert_digit, "8")
        self.map_function(self.nine_button, insert_digit, "9")
        self.map_function(self.zero_button, insert_digit, "0")

        self.dot_button.clicked.connect(partial(insert_decimal_point, self.main_screen))
        self.clear_button.clicked.connect(partial(clear_last_input, self.main_screen))
        self.all_clear_button.clicked.connect(partial(clear_screen, self.main_screen))

        self.addition_button.clicked.connect(partial(insert_operator, '+', self.main_screen))
        self.subtraction_button.clicked.connect(partial(insert_operator, '-', self.main_screen))
        self.multiplication_button.clicked.connect(partial(insert_operator, '×', self.main_screen))
        self.division_button.clicked.connect(partial(insert_operator, '÷', self.main_screen))

        
    def map_function(self, button: QPushButton, func: Callable, val: str) -> None:
        button.clicked.connect(partial(func, val, self.main_screen))


    def launch(self) -> None:
        self.show()


if __name__ == "__main__":

    app: QApplication = QApplication([])
    main: MainScreen = MainScreen()
    main.launch()
    app.exec_()

# eosc