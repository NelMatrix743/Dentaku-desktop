from PyQt5.QtWidgets import QLabel
from uipython.calculator_screen import CalculatorScreen

DEFAULT_VALUE: str = '0'
OPERATORS: list[str] = ['+', '-', '×', '÷']


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

def is_operator(value: str) -> bool:
    return value in OPERATORS

def is_percent(value: str) -> bool:
    return value == '%'

def is_decimal_point(value: str) -> bool:
    return value == '.'

def insert_digit(digit: str, screen: CalculatorScreen) -> str:
    content: str = screen.text()
    if content == DEFAULT_VALUE:
        content = digit
    elif is_percent(content[-1]): # ends with %
        content = content + f" {OPERATORS[2]} " + digit
    else:
        content = content + digit
    screen.setText(content)

def insert_optr(operator: str, screen: CalculatorScreen) -> str:
    content: str = screen.text()
    if not content[-1].isdigit() and not is_percent(content[-1]):
        pass
    else:
        content = f"{content} {operator} "
    screen.setText(content)

def insert_dcp(screen: CalculatorScreen) -> str:
    content: str = screen.text()
    if ('.' in content) or (not content[-1].isdigit()):
        pass
    else:
        content = content + '.'
    screen.setText(content)

def insert_percent(screen: CalculatorScreen) -> str:
    content: str = screen.text()
    if content[-1].isdigit():
        screen.setText(content + '%')

# eosc