# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_organizer.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(468, 421)
        MainWindow.setStyleSheet(u"backgroun-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_path = QLineEdit(self.frame)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(0, 25))
        self.txt_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_path)

        self.open_button = QPushButton(self.frame)
        self.open_button.setObjectName(u"open_button")
        self.open_button.setMinimumSize(QSize(120, 25))
        font = QFont()
        font.setPointSize(11)
        self.open_button.setFont(font)
        self.open_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_button.setStyleSheet(u"QPushButton{border-radius:10px; background-color: rgb(234, 234, 234);}\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 157, 235);}\n"
"")

        self.horizontalLayout_2.addWidget(self.open_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.start_button = QPushButton(self.frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(200, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.start_button.setFont(font1)
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(u"QPushButton{border-radius:10px; background-color: rgb(234, 234, 234);}\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 157, 235);}")

        self.horizontalLayout.addWidget(self.start_button)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><img src=\"./img/icon.png\"/></span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#3d3da7;\">FILE ORGANIZE</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta", None))
        self.open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText("")
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Organize", None))
        self.label_3.setText("")
    # retranslateUi

