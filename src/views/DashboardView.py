from PyQt6.QtWidgets import QDialog, QLabel, QGridLayout
from PyQt6.QtCore import Qt


class DashboardView(QDialog):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.setLayout(layout)

        generic_label = QLabel("Welcome to the Dashboard")
        layout.addWidget(generic_label, 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
