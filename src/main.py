from PyQt6 import uic
from models.login import Login
from views.LoginView import LoginView
from views.DashboardView import DashboardView

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QIcon("src\images\demon_devil_2.png")
    app.setWindowIcon(app_icon)

    # with open("src/styles.qss", "r") as style_file:
    # style = style_file.read()
    # app.setStyleSheet(style)

    stacked_widget = QStackedWidget()
    stacked_widget.setWindowTitle("Google Books")

    login_view = LoginView(widget=stacked_widget)
    dashboard_view = DashboardView()

    stacked_widget.addWidget(login_view)
    stacked_widget.addWidget(dashboard_view)
    stacked_widget.show()

    sys.exit(app.exec())


# login = Login("danteclark66@gmail.com", "HelloWorld12$")
