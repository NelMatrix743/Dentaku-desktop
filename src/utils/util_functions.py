from uipython.main_screen import MainScreen
from uipython.result_screen import ResultScreen
from utils.assets import DEFAULT_VALUE, OPERATORS
import tinypost as tp
import re


def reset(screen: MainScreen | ResultScreen) -> None:
    screen.setText(DEFAULT_VALUE)

def clear_screens(main_scr: MainScreen, res_scr: ResultScreen) -> None:
    main_scr.clear(); res_scr.clear()
    reset(main_scr); reset(res_scr)

def clear_digit(screen: MainScreen) -> None:
    content: str = screen.text()[:-1]
    if content:
        screen.setText(content)
    else:
        reset(screen)

def clear_operator(screen: MainScreen) -> None:
    content: str = screen.text()[:-3]
    screen.setText(content)

def clear_last_input(screen: MainScreen) -> None:
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

def insert_digit(digit: str, screen: MainScreen) -> None:
    content: str = screen.text()
    if content == DEFAULT_VALUE:
        content = digit
    elif is_percent(content[-1]): # ends with %
        content = content + f" {OPERATORS[2]} " + digit
    else:
        content = content + digit
    screen.setText(content)

def insert_optr(operator: str, screen: MainScreen) -> None:
    content: str = screen.text()
    if not content[-1].isdigit() and not is_percent(content[-1]):
        pass
    else:
        content = f"{content} {operator} "
    screen.setText(content)

def insert_dcp(screen: MainScreen) -> None:
    content: str = screen.text()
    # Split expression at operators (+, , -, ×, ÷)
    terms: list[str] = re.split(r' \+ | - | \* | / ', content)
    last_term: str = terms[-1]
    if not last_term.isdigit():
        return
    else:
        content = content + '.'
    screen.setText(content)

def insert_percent(screen: MainScreen) -> None:
    content: str = screen.text()
    if content[-1].isdigit():
        screen.setText(content + '%')

def negate_value(screen: MainScreen) -> None:
    content: str = screen.text()
    try:
        content = f"{-(int(content))}"
        screen.setText(content)
    except ValueError:
        pass

def evaluate_expression(in_screen: MainScreen, out_screen: ResultScreen) -> None:
    if out_screen.text() != "0":
        in_screen.setText(out_screen.text())
        reset(out_screen)
        return
    expr: str = in_screen.parcelable_expr
    if expr.isdigit():
        return
    if '%' in expr:
        expr = expr.replace('%', ' / 100')
    result: float | int = tp.eval_expr(expr)
    if result % 1 == 0.0:
        result = int(result)
    out_screen.setText(str(result))


# eosc
