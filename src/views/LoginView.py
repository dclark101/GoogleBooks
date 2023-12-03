from models.login import Login
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QStackedWidget,
)
from PyQt6.QtGui import QFont, QFontDatabase, QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys


class LoginView(QWidget):
    def __init__(self, widget: QStackedWidget):
        super().__init__()
        self.widget = widget
        id = QFontDatabase.addApplicationFont(r"src\fonts\NovaSquare-Regular.ttf")

        if id < 0:
            print("error")

        families = QFontDatabase.applicationFontFamilies(id)

        print(families[0])

        self.setWindowTitle("Google Books")
        self.setContentsMargins(30, 30, 30, 30)
        layout = QGridLayout()
        self.setLayout(layout)

        image = QLabel(self)
        pixmap = QPixmap("src\images\demon_devil_2.png")

        image.setPixmap(pixmap)
        # image.setScaledContents(True)

        layout.addWidget(image, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("Google Books Login")
        title_label.setMargin(100)
        title_label.setFont(QFont("Nova Square", 20))
        layout.addWidget(title_label, 1, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        self.username_label = QLabel("Username:")
        self.username_label.setFont(QFont("Nova Square", 16))
        layout.addWidget(self.username_label, 2, 0)

        self.password_label = QLabel("Password:")
        self.password_label.setFont(QFont("Nova Square", 16))
        layout.addWidget(self.password_label, 3, 0)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setFont(QFont("Nova Square", 16))
        self.username_input.contentsMargins()
        layout.addWidget(self.username_input, 2, 1, 1, 2)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setFont(QFont("Nova Square", 16))
        layout.addWidget(self.password_input, 3, 1, 1, 2)

        login_btn = QPushButton("Login")
        login_btn.setFont(QFont("Nova Square", 16))
        layout.addWidget(login_btn, 4, 1)

        register_btn = QPushButton("Register")
        register_btn.setFont(QFont("Nova Square", 16))
        layout.addWidget(register_btn, 4, 2)

        login_btn.clicked.connect(self.is_valid)

    def is_valid(self):
        account = Login(self.username_input.text(), self.password_input.text())
        if account.does_exist():
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            print("User account does exist")
        else:
            print("User account does not exist")
