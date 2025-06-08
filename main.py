from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from button import CreateButton
import sys
from automate import string

app = QApplication(sys.argv)
layout = QVBoxLayout()
widget = QWidget()
widget.setWindowTitle("Accel ERP")
widget.setGeometry(100, 100, 300, 450)
widget.show()

def clear_layout():
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)

exec(string)

widget.setLayout(layout)
sys.exit(app.exec())
