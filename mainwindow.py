# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1215, 741)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar = QFrame(self.centralwidget)
        self.topbar.setObjectName(u"topbar")
        self.topbar.setMinimumSize(QSize(0, 45))
        self.topbar.setMaximumSize(QSize(16777215, 45))
        self.topbar.setStyleSheet(u"background-color: black;")
        self.topbar.setFrameShape(QFrame.NoFrame)
        self.topbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topbar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.brand = QFrame(self.topbar)
        self.brand.setObjectName(u"brand")
        self.brand.setMaximumSize(QSize(70, 16777215))
        self.brand.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.brand.setFrameShape(QFrame.NoFrame)
        self.brand.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.brand)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 0, 0)
        self.stonks = QLabel(self.brand)
        self.stonks.setObjectName(u"stonks")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.stonks.setFont(font)
        self.stonks.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stonks.setTextFormat(Qt.PlainText)
        self.stonks.setScaledContents(True)
        self.stonks.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.stonks)


        self.horizontalLayout_2.addWidget(self.brand)

        self.space = QFrame(self.topbar)
        self.space.setObjectName(u"space")
        self.space.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.space.setFrameShape(QFrame.NoFrame)
        self.space.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.space)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(30, -1, -1, -1)
        self.label = QLabel(self.space)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic"])
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:white;\n"
"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.space)

        self.buttons = QFrame(self.topbar)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMaximumSize(QSize(150, 16777215))
        self.buttons.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.buttons.setFrameShape(QFrame.NoFrame)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.minimizeButton = QPushButton(self.buttons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(15, 0, 45, 45))
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeButton.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(57, 71, 81);\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/unterstrich.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.maximizeButton = QPushButton(self.buttons)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setGeometry(QRect(60, 0, 45, 45))
        self.maximizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeButton.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(57, 71, 81);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/viereck.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon1)
        self.exitButton = QPushButton(self.buttons)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(105, 0, 45, 45))
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(170, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.buttons)


        self.verticalLayout.addWidget(self.topbar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftbar = QFrame(self.content)
        self.leftbar.setObjectName(u"leftbar")
        self.leftbar.setMinimumSize(QSize(0, 0))
        self.leftbar.setMaximumSize(QSize(70, 16777215))
        self.leftbar.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.leftbar.setFrameShape(QFrame.NoFrame)
        self.leftbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftbar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftbar)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 165))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnToggle = QToolButton(self.frame)
        self.btnToggle.setObjectName(u"btnToggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnToggle.sizePolicy().hasHeightForWidth())
        self.btnToggle.setSizePolicy(sizePolicy)
        self.btnToggle.setMinimumSize(QSize(70, 55))
        self.btnToggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnToggle.setFocusPolicy(Qt.ClickFocus)
        self.btnToggle.setStyleSheet(u"QToolButton{\n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(39, 39, 39);\n"
"    border:0px solid;\n"
"    font-size:9px;\n"
"    font-style:futura;\n"
"	padding:7px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgb(17, 17, 17);\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/HamburgerButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnToggle.setIcon(icon3)
        self.btnToggle.setIconSize(QSize(16, 16))
        self.btnToggle.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.btnToggle)

        self.btnAnalyse = QToolButton(self.frame)
        self.btnAnalyse.setObjectName(u"btnAnalyse")
        sizePolicy.setHeightForWidth(self.btnAnalyse.sizePolicy().hasHeightForWidth())
        self.btnAnalyse.setSizePolicy(sizePolicy)
        self.btnAnalyse.setMinimumSize(QSize(70, 55))
        self.btnAnalyse.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyse.setFocusPolicy(Qt.StrongFocus)
        self.btnAnalyse.setStyleSheet(u"QToolButton{\n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(39, 39, 39);\n"
"    border:0px solid;\n"
"    font-size:9px;\n"
"    font-style:futura;\n"
"	padding:7px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgb(17, 17, 17);\n"
"\n"
"}\n"
"QToolButton:focus{\n"
"\n"
"	background-color: rgb(105, 105, 105);\n"
"border-left: 3px solid #E1A100;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/Home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAnalyse.setIcon(icon4)
        self.btnAnalyse.setIconSize(QSize(18, 18))
        self.btnAnalyse.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.btnAnalyse.setAutoRaise(False)

        self.verticalLayout_4.addWidget(self.btnAnalyse)

        self.btnDashboard = QToolButton(self.frame)
        self.btnDashboard.setObjectName(u"btnDashboard")
        sizePolicy.setHeightForWidth(self.btnDashboard.sizePolicy().hasHeightForWidth())
        self.btnDashboard.setSizePolicy(sizePolicy)
        self.btnDashboard.setMinimumSize(QSize(70, 55))
        self.btnDashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDashboard.setFocusPolicy(Qt.ClickFocus)
        self.btnDashboard.setStyleSheet(u"QToolButton{\n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(39, 39, 39);\n"
"    border:0px solid;\n"
"    font-size:9px;\n"
"    font-style:futura;\n"
"	padding:7px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgb(17, 17, 17);\n"
"\n"
"}\n"
"QToolButton:focus{\n"
"\n"
"	background-color: rgb(105, 105, 105);\n"
"border-left: 3px solid #E1A100;\n"
"\n"
"\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/Analyse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDashboard.setIcon(icon5)
        self.btnDashboard.setIconSize(QSize(18, 18))
        self.btnDashboard.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.btnDashboard)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftbar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.leftbar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 110))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnSettings = QToolButton(self.frame_3)
        self.btnSettings.setObjectName(u"btnSettings")
        sizePolicy.setHeightForWidth(self.btnSettings.sizePolicy().hasHeightForWidth())
        self.btnSettings.setSizePolicy(sizePolicy)
        self.btnSettings.setMinimumSize(QSize(70, 55))
        self.btnSettings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSettings.setFocusPolicy(Qt.ClickFocus)
        self.btnSettings.setStyleSheet(u"QToolButton{\n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(39, 39, 39);\n"
"    border:0px solid;\n"
"    font-size:9px;\n"
"    font-style:futura;\n"
"	padding:7px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgb(17, 17, 17);\n"
"\n"
"}\n"
"QToolButton:focus{\n"
"\n"
"	background-color: rgb(105, 105, 105);\n"
"border-left: 3px solid #E1A100;\n"
"\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/Einstellungen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSettings.setIcon(icon6)
        self.btnSettings.setIconSize(QSize(18, 18))
        self.btnSettings.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_3.addWidget(self.btnSettings)

        self.btnHelp = QToolButton(self.frame_3)
        self.btnHelp.setObjectName(u"btnHelp")
        sizePolicy.setHeightForWidth(self.btnHelp.sizePolicy().hasHeightForWidth())
        self.btnHelp.setSizePolicy(sizePolicy)
        self.btnHelp.setMinimumSize(QSize(70, 55))
        self.btnHelp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHelp.setFocusPolicy(Qt.ClickFocus)
        self.btnHelp.setStyleSheet(u"QToolButton{\n"
"    color:rgb(255,255,255);\n"
"  background-color: rgb(39, 39, 39);\n"
"    border:0px solid;\n"
"    font-size:9px;\n"
"    font-style:futura;\n"
"	padding:7px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgb(17, 17, 17);\n"
"\n"
"}\n"
"QToolButton:focus{\n"
"\n"
"	background-color: rgb(105, 105, 105);\n"
"border-left: 3px solid #E1A100;\n"
"\n"
"\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"../../../PycharmProjects/Reichwerdenamk/images/help-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.btnHelp)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.leftbar)

        self.data = QFrame(self.content)
        self.data.setObjectName(u"data")
        self.data.setMaximumSize(QSize(16777215, 16777215))
        self.data.setFrameShape(QFrame.NoFrame)
        self.data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.data)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.data)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout_6 = QVBoxLayout(self.dashboard)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.dashboard)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(28)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.dashboard)
        self.analyse = QWidget()
        self.analyse.setObjectName(u"analyse")
        self.verticalLayout_7 = QVBoxLayout(self.analyse)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.analyse)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.analyse)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.data)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.stonks.setText(QCoreApplication.translate("MainWindow", u"BI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BI  - Warenkorbanalyse", None))
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.exitButton.setText("")
        self.btnToggle.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnAnalyse.setText("")
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
    # retranslateUi

