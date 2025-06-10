from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent

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
            color: blue;
            background-color: white;
            border-style: outset;
            border-width: 3px;
            border-radius: 18px;
            border-color: blue;
            padding: 4px;
            }
            QPushButton:hover {
                background-color: #a0c4ff;
            }
            QPushButton:focus {
                background-color: #a0c4ff;
                border: 2px solid #1d3557;
            }
            """)
        self.setAutoDefault(True)
