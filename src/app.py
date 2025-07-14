from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from uipython.main_screen import MainScreen
from uipython.result_screen import ResultScreen
from collections.abc import Callable
from PyQt5.QtGui import QIcon
from functools import partial
from PyQt5.uic import loadUi
from typing import Any
from utils.util_functions import (
    clear_last_input,
    clear_screen,
    insert_digit,
    insert_optr,
    insert_dcp,
    insert_percent,
    negate_value,
    evaluate_expression
)
from utils.assets import APP_NAME, APP_ICON


class DentakuMain(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        loadUi("src/uixml/main_screen.ui", self)
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(APP_ICON)) 
        self.setup_ui_components()


    def mapwidget(self, name: str, w_type: type = QPushButton) -> Any:
        return self.findChild(w_type, name)


    def mapfunction(self, button: QPushButton, func: Callable, val: str = None) -> None:
        if not val:
            button.clicked.connect(partial(func, self.main_screen))
            return
        button.clicked.connect(partial(func, val, self.main_screen))


    def setup_ui_components(self) -> None:
        # calculator screens
        self.main_screen: MainScreen = self.mapwidget("expr_screen", w_type=MainScreen)
        self.result_screen: ResultScreen = self.mapwidget("res_screen", w_type=ResultScreen)

        # function buttons
        self.clear_button: QPushButton = self.mapwidget("button_clr")
        self.all_clear_button: QPushButton = self.mapwidget("button_ac")

        # arithmetic operators
        self.percentage_button: QPushButton = self.mapwidget("button_perc")
        self.division_button: QPushButton = self.mapwidget("button_div")
        self.multiplication_button: QPushButton = self.mapwidget("button_mul")
        self.subtraction_button: QPushButton = self.mapwidget("button_min")
        self.addition_button: QPushButton = self.mapwidget("button_add")
        self.equals_button: QPushButton = self.mapwidget("button_eq")
        self.plus_minus_button: QPushButton = self.mapwidget("button_pm")

        # digits and decimal point
        self.zero_button: QPushButton = self.mapwidget("button_0")
        self.one_button: QPushButton = self.mapwidget("button_1")
        self.two_button: QPushButton = self.mapwidget("button_2")
        self.three_button: QPushButton = self.mapwidget("button_3")
        self.four_button: QPushButton = self.mapwidget("button_4")
        self.five_button: QPushButton = self.mapwidget("button_5")
        self.six_button: QPushButton = self.mapwidget("button_6")
        self.seven_button: QPushButton = self.mapwidget("button_7")
        self.eight_button: QPushButton = self.mapwidget("button_8")
        self.nine_button: QPushButton = self.mapwidget("button_9")
        self.dot_button: QPushButton = self.mapwidget("button_dot")

        # map buttons to functions
        self.mapfunction(self.zero_button, insert_digit, val="0")
        self.mapfunction(self.one_button, insert_digit, val="1")
        self.mapfunction(self.two_button, insert_digit, val="2")
        self.mapfunction(self.three_button, insert_digit, val="3")
        self.mapfunction(self.four_button, insert_digit, val="4")
        self.mapfunction(self.five_button, insert_digit, val="5")
        self.mapfunction(self.six_button, insert_digit, val="6")
        self.mapfunction(self.seven_button, insert_digit, val="7")
        self.mapfunction(self.eight_button, insert_digit, val="8")
        self.mapfunction(self.nine_button, insert_digit, val="9")

        self.mapfunction(self.dot_button, insert_dcp)
        self.mapfunction(self.percentage_button, insert_percent)
        self.mapfunction(self.clear_button, clear_last_input)
        self.mapfunction(self.all_clear_button, clear_screen)

        self.mapfunction(self.addition_button, insert_optr, val="+")
        self.mapfunction(self.multiplication_button, insert_optr, val='×')
        self.mapfunction(self.subtraction_button, insert_optr, val="-")
        self.mapfunction(self.division_button, insert_optr, val='÷')

        self.mapfunction(self.plus_minus_button, negate_value)

        self.equals_button.clicked.connect(partial(evaluate_expression, self.main_screen, self.result_screen))


    def launch(self) -> None:
        self.show()


if __name__ == "__main__":

    app: QApplication = QApplication([])
    main: DentakuMain = DentakuMain()
    main.launch()
    app.exec_()

# eosc