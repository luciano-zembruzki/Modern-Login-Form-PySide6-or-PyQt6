# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loginWwYRzh.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(450, 432)
        Login.setMinimumSize(QSize(450, 400))
        Login.setMaximumSize(QSize(450, 432))
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.023, stop:0 rgba(255, 140, 140, 255), stop:1 rgba(94, 122, 255, 255));\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame#frame{\n"
"	margin: 60px;\n"
"	border-radius: 20px;\n"
"	background-color: rgba(225, 228, 221, 120)\n"
"}\n"
"\n"
"QLineEdit{\n"
"	min-height: 45px;\n"
"	border-radius: 20px;\n"
"	background-color: #FFFFFF;\n"
"	padding-left: 20px;\n"
"	color: rgb(140, 140, 140);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(139, 142, 139);\n"
"}\n"
"\n"
"QPushButton#login_button{\n"
"	min-height: 45px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(140, 140, 140);\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton#login_button:hover{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox{\n"
"	font-size: 10px;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(95, 94, 108);\n"
"}\n"
"\n"
"QPushButton#forgot_button{\n"
"	border: 0px;\n"
"	font-style: italic;\n"
"	font-size: 10p"
                        "x;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton#close_button{\n"
"	background-color: rgb(186, 0, 0);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton#minimize_button{\n"
"	background-color: rgb(226, 226, 0);\n"
"	border-radius: 6px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 30))
        self.top_bar.setMaximumSize(QSize(16777215, 30))
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.top_bar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.top_bar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(60, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.minimize_button = QPushButton(self.frame_3)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.frame_3)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.top_bar)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.login_button = QPushButton(self.frame)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout.addWidget(self.login_button)

        self.bottom_frame = QFrame(self.frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMaximumSize(QSize(16777215, 20))
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.bottom_frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.forgot_button = QPushButton(self.bottom_frame)
        self.forgot_button.setObjectName(u"forgot_button")
        font = QFont()
        font.setItalic(True)
        self.forgot_button.setFont(font)

        self.horizontalLayout_2.addWidget(self.forgot_button)


        self.verticalLayout.addWidget(self.bottom_frame)


        self.verticalLayout_2.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.minimize_button.setText("")
        self.close_button.setText("")
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:20pt;\">Sign In</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"Email", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Sign In", None))
        self.checkBox.setText(QCoreApplication.translate("Login", u"Remember me", None))
        self.forgot_button.setText(QCoreApplication.translate("Login", u"Forgot Password", None))
    # retranslateUi

