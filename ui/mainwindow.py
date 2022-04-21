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
        MainWindow.resize(1535, 846)
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
        icon.addFile(u"images/unterstrich.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u"images/viereck.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u"images/x.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"images/HamburgerButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnToggle.setIcon(icon3)
        self.btnToggle.setIconSize(QSize(16, 16))
        self.btnToggle.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.btnToggle)

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
        icon4 = QIcon()
        icon4.addFile(u"images/Analyse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDashboard.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u"images/Einstellungen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSettings.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u"images/help-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon6)

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
        self.frame_4 = QFrame(self.dashboard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 140))
        self.frame_5.setMaximumSize(QSize(16777215, 200))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(0, 140))
        self.frame_7.setMaximumSize(QSize(16777215, 140))
        self.frame_7.setStyleSheet(u"background-color: #052f2b;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(140, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 2, -1, 11)
        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 20))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light"])
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_2)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_14)
        self.verticalLayout_24.setSpacing(11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, -1, 0, -1)
        self.rbProducts = QRadioButton(self.frame_14)
        self.rbProducts.setObjectName(u"rbProducts")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift Light Condensed"])
        font3.setPointSize(11)
        self.rbProducts.setFont(font3)
        self.rbProducts.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.rbProducts)

        self.rbCategory = QRadioButton(self.frame_14)
        self.rbCategory.setObjectName(u"rbCategory")
        self.rbCategory.setFont(font3)
        self.rbCategory.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.rbCategory)

        self.checkBoxItems = QCheckBox(self.frame_14)
        self.checkBoxItems.setObjectName(u"checkBoxItems")
        self.checkBoxItems.setFont(font3)
        self.checkBoxItems.setStyleSheet(u"color:white;")

        self.verticalLayout_24.addWidget(self.checkBoxItems)


        self.verticalLayout_13.addWidget(self.frame_14)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(150, 16777215))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 2, 0, -1)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_4)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border:0px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_15)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_15)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"border-right:1px solid white;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 22, 0)
        self.spinBoxSupport = QSpinBox(self.frame_30)
        self.spinBoxSupport.setObjectName(u"spinBoxSupport")
        self.spinBoxSupport.setMinimumSize(QSize(45, 0))
        self.spinBoxSupport.setMaximumSize(QSize(45, 16777215))
        self.spinBoxSupport.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_9.addWidget(self.spinBoxSupport)

        self.label_7 = QLabel(self.frame_30)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:0px;")

        self.horizontalLayout_9.addWidget(self.label_7)


        self.verticalLayout_25.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_15)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"border-right:1px solid white;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 1, 18, -1)
        self.spinBoxConfidence = QSpinBox(self.frame_31)
        self.spinBoxConfidence.setObjectName(u"spinBoxConfidence")
        self.spinBoxConfidence.setMinimumSize(QSize(45, 0))
        self.spinBoxConfidence.setMaximumSize(QSize(45, 16777215))
        self.spinBoxConfidence.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_10.addWidget(self.spinBoxConfidence)

        self.label_8 = QLabel(self.frame_31)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:0px;")

        self.horizontalLayout_10.addWidget(self.label_8)


        self.verticalLayout_25.addWidget(self.frame_31)


        self.verticalLayout_15.addWidget(self.frame_15)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 2, 0, -1)
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_5)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 103))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnAllCountries = QPushButton(self.frame_16)
        self.btnAllCountries.setObjectName(u"btnAllCountries")
        self.btnAllCountries.setMinimumSize(QSize(80, 80))
        self.btnAllCountries.setMaximumSize(QSize(80, 80))
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift Light Condensed"])
        font4.setPointSize(20)
        self.btnAllCountries.setFont(font4)
        self.btnAllCountries.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAllCountries.setFocusPolicy(Qt.ClickFocus)
        self.btnAllCountries.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"images/Globe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAllCountries.setIcon(icon7)
        self.btnAllCountries.setIconSize(QSize(55, 55))

        self.horizontalLayout_7.addWidget(self.btnAllCountries)

        self.btnNorthAmerica = QPushButton(self.frame_16)
        self.btnNorthAmerica.setObjectName(u"btnNorthAmerica")
        self.btnNorthAmerica.setMinimumSize(QSize(80, 80))
        self.btnNorthAmerica.setMaximumSize(QSize(80, 80))
        self.btnNorthAmerica.setFont(font4)
        self.btnNorthAmerica.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNorthAmerica.setFocusPolicy(Qt.ClickFocus)
        self.btnNorthAmerica.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"images/North America.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNorthAmerica.setIcon(icon8)
        self.btnNorthAmerica.setIconSize(QSize(55, 55))

        self.horizontalLayout_7.addWidget(self.btnNorthAmerica)

        self.btnEurope = QPushButton(self.frame_16)
        self.btnEurope.setObjectName(u"btnEurope")
        self.btnEurope.setMinimumSize(QSize(80, 80))
        self.btnEurope.setMaximumSize(QSize(80, 80))
        self.btnEurope.setFont(font4)
        self.btnEurope.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEurope.setFocusPolicy(Qt.ClickFocus)
        self.btnEurope.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"images/Europe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEurope.setIcon(icon9)
        self.btnEurope.setIconSize(QSize(55, 55))

        self.horizontalLayout_7.addWidget(self.btnEurope)

        self.btnPacific = QPushButton(self.frame_16)
        self.btnPacific.setObjectName(u"btnPacific")
        self.btnPacific.setMinimumSize(QSize(80, 80))
        self.btnPacific.setMaximumSize(QSize(80, 80))
        self.btnPacific.setFont(font4)
        self.btnPacific.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPacific.setFocusPolicy(Qt.ClickFocus)
        self.btnPacific.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"images/Pacific.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPacific.setIcon(icon10)
        self.btnPacific.setIconSize(QSize(55, 55))

        self.horizontalLayout_7.addWidget(self.btnPacific)


        self.verticalLayout_16.addWidget(self.frame_16)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(11, 2, -1, -1)
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:11px;")

        self.verticalLayout_17.addWidget(self.label_6)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 103))
        self.frame_17.setAutoFillBackground(False)
        self.frame_17.setStyleSheet(u"border-left:1px solid white;\n"
"border-right:1px solid white;")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(22, -1, 22, -1)
        self.btnJahreszeitenAll = QPushButton(self.frame_17)
        self.btnJahreszeitenAll.setObjectName(u"btnJahreszeitenAll")
        self.btnJahreszeitenAll.setMinimumSize(QSize(80, 80))
        self.btnJahreszeitenAll.setMaximumSize(QSize(80, 80))
        self.btnJahreszeitenAll.setFont(font4)
        self.btnJahreszeitenAll.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnJahreszeitenAll.setFocusPolicy(Qt.ClickFocus)
        self.btnJahreszeitenAll.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"images/Jahreszeiten.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnJahreszeitenAll.setIcon(icon11)
        self.btnJahreszeitenAll.setIconSize(QSize(55, 55))

        self.horizontalLayout_5.addWidget(self.btnJahreszeitenAll)

        self.btnFruehling = QPushButton(self.frame_17)
        self.btnFruehling.setObjectName(u"btnFruehling")
        self.btnFruehling.setMinimumSize(QSize(80, 80))
        self.btnFruehling.setMaximumSize(QSize(80, 80))
        self.btnFruehling.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnFruehling.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"images/Astrology-Spring-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFruehling.setIcon(icon12)
        self.btnFruehling.setIconSize(QSize(55, 55))

        self.horizontalLayout_5.addWidget(self.btnFruehling)

        self.btnSommer = QPushButton(self.frame_17)
        self.btnSommer.setObjectName(u"btnSommer")
        self.btnSommer.setMinimumSize(QSize(80, 80))
        self.btnSommer.setMaximumSize(QSize(80, 80))
        self.btnSommer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSommer.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"images/Astrology-Summer-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSommer.setIcon(icon13)
        self.btnSommer.setIconSize(QSize(55, 55))

        self.horizontalLayout_5.addWidget(self.btnSommer)

        self.btnHerbst = QPushButton(self.frame_17)
        self.btnHerbst.setObjectName(u"btnHerbst")
        self.btnHerbst.setMinimumSize(QSize(80, 80))
        self.btnHerbst.setMaximumSize(QSize(80, 80))
        self.btnHerbst.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHerbst.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon14 = QIcon()
        icon14.addFile(u"images/Astrology-Autumn-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHerbst.setIcon(icon14)
        self.btnHerbst.setIconSize(QSize(55, 55))

        self.horizontalLayout_5.addWidget(self.btnHerbst)

        self.btnWinter = QPushButton(self.frame_17)
        self.btnWinter.setObjectName(u"btnWinter")
        self.btnWinter.setMinimumSize(QSize(80, 80))
        self.btnWinter.setMaximumSize(QSize(80, 80))
        self.btnWinter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnWinter.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#010f0e ;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color:#0b6d63  ;\n"
"}\n"
"\n"
"")
        icon15 = QIcon()
        icon15.addFile(u"images/Astrology-Winter-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnWinter.setIcon(icon15)
        self.btnWinter.setIconSize(QSize(55, 55))

        self.horizontalLayout_5.addWidget(self.btnWinter)


        self.verticalLayout_17.addWidget(self.frame_17)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(11, 11, 0, 11)
        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboSortierung = QComboBox(self.frame_19)
        self.comboSortierung.setObjectName(u"comboSortierung")
        self.comboSortierung.setMinimumSize(QSize(130, 28))
        self.comboSortierung.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.comboSortierung)

        self.label_12 = QLabel(self.frame_19)
        self.label_12.setObjectName(u"label_12")
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift Light Condensed"])
        font5.setPointSize(14)
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"color:white;")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.verticalLayout_18.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btnReset = QPushButton(self.frame_18)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setMinimumSize(QSize(0, 30))
        self.btnReset.setMaximumSize(QSize(70, 16777215))
        self.btnReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnReset.setFocusPolicy(Qt.ClickFocus)
        self.btnReset.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 0, 0);\n"
"}")
        self.btnReset.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.btnReset)

        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color:white;")

        self.horizontalLayout_13.addWidget(self.label_9)


        self.verticalLayout_18.addWidget(self.frame_18)

        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setSpacing(7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnAccept = QPushButton(self.frame_21)
        self.btnAccept.setObjectName(u"btnAccept")
        self.btnAccept.setMinimumSize(QSize(0, 30))
        self.btnAccept.setMaximumSize(QSize(70, 16777215))
        self.btnAccept.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAccept.setFocusPolicy(Qt.ClickFocus)
        self.btnAccept.setStyleSheet(u"QPushButton{\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 100, 0);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"images/haken.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAccept.setIcon(icon16)

        self.horizontalLayout_12.addWidget(self.btnAccept)

        self.label_10 = QLabel(self.frame_21)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color:white;")

        self.horizontalLayout_12.addWidget(self.label_10)


        self.verticalLayout_18.addWidget(self.frame_21)


        self.horizontalLayout_4.addWidget(self.frame_12)


        self.verticalLayout_10.addWidget(self.frame_7)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:0px solid black;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1419, 635))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.results = QVBoxLayout()
        self.results.setObjectName(u"results")

        self.verticalLayout_12.addLayout(self.results)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.verticalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.dashboard)
        self.analyse = QWidget()
        self.analyse.setObjectName(u"analyse")
        self.verticalLayout_7 = QVBoxLayout(self.analyse)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.analyse)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift"])
        font6.setPointSize(28)
        font6.setBold(True)
        self.label_3.setFont(font6)
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
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.rbProducts.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.rbCategory.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.checkBoxItems.setText(QCoreApplication.translate("MainWindow", u"Show Itemsets", None))
        self.label_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"min Support", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"min Confidence", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Locations", None))
#if QT_CONFIG(tooltip)
        self.btnAllCountries.setToolTip(QCoreApplication.translate("MainWindow", u"All Locations", None))
#endif // QT_CONFIG(tooltip)
        self.btnAllCountries.setText("")
#if QT_CONFIG(tooltip)
        self.btnNorthAmerica.setToolTip(QCoreApplication.translate("MainWindow", u"North America", None))
#endif // QT_CONFIG(tooltip)
        self.btnNorthAmerica.setText("")
#if QT_CONFIG(tooltip)
        self.btnEurope.setToolTip(QCoreApplication.translate("MainWindow", u"Europe", None))
#endif // QT_CONFIG(tooltip)
        self.btnEurope.setText("")
#if QT_CONFIG(tooltip)
        self.btnPacific.setToolTip(QCoreApplication.translate("MainWindow", u"Pacific", None))
#endif // QT_CONFIG(tooltip)
        self.btnPacific.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Season", None))
#if QT_CONFIG(tooltip)
        self.btnJahreszeitenAll.setToolTip(QCoreApplication.translate("MainWindow", u"All Seasons", None))
#endif // QT_CONFIG(tooltip)
        self.btnJahreszeitenAll.setText("")
#if QT_CONFIG(tooltip)
        self.btnFruehling.setToolTip(QCoreApplication.translate("MainWindow", u"Spring", None))
#endif // QT_CONFIG(tooltip)
        self.btnFruehling.setText("")
#if QT_CONFIG(tooltip)
        self.btnSommer.setToolTip(QCoreApplication.translate("MainWindow", u"Summer", None))
#endif // QT_CONFIG(tooltip)
        self.btnSommer.setText("")
#if QT_CONFIG(tooltip)
        self.btnHerbst.setToolTip(QCoreApplication.translate("MainWindow", u"Autumn", None))
#endif // QT_CONFIG(tooltip)
        self.btnHerbst.setText("")
#if QT_CONFIG(tooltip)
        self.btnWinter.setToolTip(QCoreApplication.translate("MainWindow", u"Winter", None))
#endif // QT_CONFIG(tooltip)
        self.btnWinter.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Sorting", None))
        self.btnReset.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"reset Filters", None))
        self.btnAccept.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"confirm Filters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
    # retranslateUi

