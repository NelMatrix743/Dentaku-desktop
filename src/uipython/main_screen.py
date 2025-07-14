from PyQt5.QtWidgets import  QPlainTextEdit
from PyQt6.QtGui import QTextOption
from PyQt5.QtCore import Qt
from PyQt6.QtGui import QTextCursor #QFontMetrics, QFont
from utils.assets import OPERATORS, PARCELABLE_OPERATORS

class MainScreen(QPlainTextEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.parcelable_expr: str = ""
        # read only
        self.setReadOnly(True)
        # right-alignment
        default_opt: QTextOption = self.document().defaultTextOption()
        default_opt.setAlignment(Qt.AlignRight)
        self.document().setDefaultTextOption(default_opt)
        # default value
        self.cursor: QTextCursor = self.textCursor()
        self.cursor.movePosition(self.cursor.End)
        self.setText('0')

    def text(self) -> str:
        return self.toPlainText()

    def setText(self, text: str) -> None:
        self.setPlainText(text)
        self.parcelable_expr = ''.join(
            [PARCELABLE_OPERATORS[token] if token in OPERATORS else token 
            for token in text]
        )
        # cursor position
        self.setTextCursor(self.cursor)

    def clear(self):
        self.parcelable_expr = ""
        super().clear()


# eosc