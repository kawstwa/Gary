from PySide6.QtWidgets import QPushButton

class CreateButton(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(230,50)
        self.setStyleSheet("text-align: left; padding-left: 10px; font: bold 20px;")
        self.setAutoDefault(True)