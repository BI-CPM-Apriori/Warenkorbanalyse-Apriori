# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ergebnissframe.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1298, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(0, 200))
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setStyleSheet(u"background-color:white;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.photo = QLabel(self.frame_6)
        self.photo.setObjectName(u"photo")

        self.verticalLayout_8.addWidget(self.photo)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 80)
        self.ProgressBarBase_3 = QFrame(self.frame_10)
        self.ProgressBarBase_3.setObjectName(u"ProgressBarBase_3")
        self.ProgressBarBase_3.setMinimumSize(QSize(150, 150))
        self.ProgressBarBase_3.setMaximumSize(QSize(80, 80))
        self.ProgressBarBase_3.setStyleSheet(u"")
        self.ProgressBarBase_3.setFrameShape(QFrame.NoFrame)
        self.ProgressBarBase_3.setFrameShadow(QFrame.Raised)
        self.progressKreis = QFrame(self.ProgressBarBase_3)
        self.progressKreis.setObjectName(u"progressKreis")
        self.progressKreis.setGeometry(QRect(10, 10, 140, 140))
        self.progressKreis.setStyleSheet(u"QFrame{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.494444 rgba(13, 72, 72, 255), stop:0.495444 rgba(13, 72, 72, 255));\n"
"border-radius:70px;\n"
"\n"
"}")
        self.progressKreis.setFrameShape(QFrame.NoFrame)
        self.progressKreis.setFrameShadow(QFrame.Raised)
        self.frame_142 = QFrame(self.ProgressBarBase_3)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setGeometry(QRect(10, 10, 140, 140))
        self.frame_142.setStyleSheet(u"QFrame{\n"
"border-radius:70px;\n"
"	\n"
"	background-color:#bdbdbd;\n"
"\n"
"}")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.frame_172 = QFrame(self.ProgressBarBase_3)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setGeometry(QRect(31, 31, 98, 98))
        self.frame_172.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-radius:49px;\n"
"}")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_172)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(20, 30, 71, 41))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelConfidence = QLabel(self.frame_11)
        self.labelConfidence.setObjectName(u"labelConfidence")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(28)
        font.setBold(False)
        self.labelConfidence.setFont(font)
        self.labelConfidence.setStyleSheet(u"background-color:none;\n"
"color:black;")
        self.labelConfidence.setScaledContents(True)
        self.labelConfidence.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.labelConfidence)

        self.frame_142.raise_()
        self.progressKreis.raise_()
        self.frame_172.raise_()

        self.horizontalLayout_3.addWidget(self.ProgressBarBase_3)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 30))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(7, 0, 0, 0)
        self.label_127 = QLabel(self.frame_9)
        self.label_127.setObjectName(u"label_127")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.label_127.setFont(font1)
        self.label_127.setStyleSheet(u"background-color:none;\n"
"color: rgb(141, 141, 141);")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_127)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"background-color:white;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: white;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.photo.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.labelConfidence.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; vertical-align:super;\">95%</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("Form", u"Confidence", None))
        self.label.setText(QCoreApplication.translate("Form", u"Interpretation der Eregbnisse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Marketingstrategie", None))
    # retranslateUi

