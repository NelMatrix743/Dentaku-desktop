from PyQt5.QtWidgets import QLabel


def clear_screen(screen: QLabel) -> bool:
    screen.clear()
    if len(screen.text()) == 0:
        return True
    return False


# eosc
