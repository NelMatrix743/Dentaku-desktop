from PyQt5.QtWidgets import QLabel
from uipython.calculator_screen import CalculatorScreen


def reset(screen: CalculatorScreen) -> None:
    screen.setText('0')

def clear_screen(screen: CalculatorScreen) -> None:
    screen.clear()
    reset(screen)

def clear_last_input(screen: CalculatorScreen) -> None:
    content: str = screen.text()
    content = content[0:len(content)-1]
    if not len(content):
        reset(screen)
        return
    screen.setText(content)

def insert_digit(digit: str, screen: CalculatorScreen) -> None:
    if screen.text().startswith("0"):
        screen.clear()
    screen.setText(screen.text() + digit)

# eosc
