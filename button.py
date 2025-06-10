from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtCore import Qt


class CreateButton(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.hasMouseTracking()
        self.setText(text)
        self.setFixedSize(230,50)
        self.setStyleSheet("""
            QPushButton {
            text-align: left; 
            padding-left: 10px;
            font: bold 20px;
            background-color: #1d2373;
            border-style: outset;
            border-width: 3px;
            border-radius: 18px;
            border-color: blue;
            padding: 4px;
            }
            QPushButton:hover {
                background-color: #0e5c8f;
            }
            """)
        self.setAutoDefault(True)