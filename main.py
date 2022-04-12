from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen

from login import Ui_Login


class LoginUI(QMainWindow, Ui_Login):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # center = QScreen.availableGeometry(QApplication.primaryScreen()).center()

        # self.move(center.x() - self.width() / 2, center.y() - self.height() / 2)

        self.close_button.clicked.connect(self.close)
        self.minimize_button.clicked.connect(self.minimize)

    def close(self):
        return super().close()

    def minimize(self):
        self.showMinimized()


app = QApplication([])

w = LoginUI()
w.show()

app.exec()