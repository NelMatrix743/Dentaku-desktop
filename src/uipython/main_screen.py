from PyQt5.QtWidgets import  QPlainTextEdit
from PyQt6.QtGui import QTextOption
from PyQt5.QtCore import Qt
from PyQt6.QtGui import QTextCursor #QFontMetrics, QFont


class MainScreen(QPlainTextEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
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
        # cursor position
        self.setTextCursor(self.cursor)

# eosc