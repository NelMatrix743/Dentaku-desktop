# MATH FUNCTIONS

def add(first_num: int | float, second_num: int | float) -> int | float:
    return first_num + second_num


def subtract(this_num: int | float, from_num: int | float) -> int | float:
    return from_num - this_num


def multiply(first_num: int | float, second_num: int) -> int | float:
    return first_num * second_num


def divide(this_num: int | float, by_num: int | float) -> int | float:
    if isinstance(this_num, float) or isinstance(by_num, float):
        # floating-point division
        # round to 5 decimal digits
        return round((this_num / by_num), 5)
    # integer division
    return this_num // by_num


def invert_sign(number: int | float) -> int | float:
    return -(number)


# eosc
