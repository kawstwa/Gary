from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent

class CreateButton(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.hasMouseTracking()
        # self.hasTabletTracking()
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
            QPushButton:focus {
                background-color: #a0c4ff;
                border: 2px solid #1d3557;
            }
            """)
        self.setAutoDefault(True)
