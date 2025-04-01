from PyQt5.QtWidgets import QLabel
from uipython.calculator_screen import CalculatorScreen

DEFAULT_VALUE: str = '0'

def reset(screen: CalculatorScreen) -> None:
    screen.setText(DEFAULT_VALUE)

def clear_screen(screen: CalculatorScreen) -> None:
    screen.clear()
    reset(screen)

def clear_digit(screen: CalculatorScreen) -> None:
    content: str = screen.text()[:-1]
    if content:
        screen.setText(content)
    else:
        reset(screen)

def clear_operator(screen: CalculatorScreen) -> None:
    content: str = screen.text()[:-3]
    screen.setText(content)

def clear_last_input(screen: CalculatorScreen) -> None:
    content: str = screen.text()
    if content.endswith(' '): # operator
        clear_operator(screen)
    else: # digit
        clear_digit(screen)

def insert_digit(digit: str, screen: CalculatorScreen) -> None:
    content: str = screen.text()
    if content == DEFAULT_VALUE:
        content = ''
    screen.setText(content + digit)

def insert_decimal_point(screen: CalculatorScreen) -> None:
    content: str = screen.text()
    if '.' in content:
        return
    screen.setText(content + '.')

def insert_operator(operator: str, screen: CalculatorScreen) -> None:
    content: str = screen.text()
    if not content[-1].isdigit() and content[-1] != "%":
        return
    screen.setText(f"{content} {operator} ")

# eosc
