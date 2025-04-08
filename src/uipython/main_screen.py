from PyQt5.QtWidgets import  QPlainTextEdit
from PyQt6.QtGui import QTextOption
from PyQt5.QtCore import Qt
#from PyQt6.QtGui import QFontMetrics, QFont


class MainScreen(QPlainText):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)