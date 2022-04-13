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
        self.frame_6.setMinimumSize(QSize(600, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.photo = QLabel(self.frame_16)
        self.photo.setObjectName(u"photo")

        self.verticalLayout_12.addWidget(self.photo)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 25))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.produkt1 = QLabel(self.frame_17)
        self.produkt1.setObjectName(u"produkt1")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(14)
        self.produkt1.setFont(font)
        self.produkt1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.produkt1)


        self.verticalLayout_8.addWidget(self.frame_17)


        self.horizontalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.photo2 = QLabel(self.frame_18)
        self.photo2.setObjectName(u"photo2")

        self.verticalLayout_13.addWidget(self.photo2)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 25))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.produkt2 = QLabel(self.frame_19)
        self.produkt2.setObjectName(u"produkt2")
        self.produkt2.setFont(font)
        self.produkt2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.produkt2)


        self.verticalLayout_10.addWidget(self.frame_19)


        self.horizontalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u"images/pfeil_lang.png"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_6)


        self.horizontalLayout_4.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.photo3 = QLabel(self.frame_20)
        self.photo3.setObjectName(u"photo3")

        self.verticalLayout_14.addWidget(self.photo3)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 25))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_21)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.produkt3 = QLabel(self.frame_21)
        self.produkt3.setObjectName(u"produkt3")
        self.produkt3.setFont(font)
        self.produkt3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.produkt3)


        self.verticalLayout_11.addWidget(self.frame_21)


        self.horizontalLayout_4.addWidget(self.frame_15)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMaximumSize(QSize(331, 16777215))
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
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(28)
        font1.setBold(False)
        self.labelConfidence.setFont(font1)
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.label_127.setFont(font2)
        self.label_127.setStyleSheet(u"background-color:none;\n"
"color: rgb(141, 141, 141);")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_127)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(250, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_181 = QFrame(self.frame_8)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setStyleSheet(u"border:1px solid lightgrey;")
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_181)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_190 = QFrame(self.frame_181)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setStyleSheet(u"border:0px;")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_190)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.labelSupport = QLabel(self.frame_190)
        self.labelSupport.setObjectName(u"labelSupport")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift Light"])
        font3.setPointSize(20)
        font3.setBold(False)
        self.labelSupport.setFont(font3)
        self.labelSupport.setStyleSheet(u"background-color:none;\n"
"color:black;\n"
"border:0px;")
        self.labelSupport.setAlignment(Qt.AlignCenter)

        self.verticalLayout_118.addWidget(self.labelSupport)


        self.horizontalLayout_50.addWidget(self.frame_190)

        self.frame_191 = QFrame(self.frame_181)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setStyleSheet(u"border:0px;")
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_191)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.frame_192 = QFrame(self.frame_191)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_192)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.label_137 = QLabel(self.frame_192)
        self.label_137.setObjectName(u"label_137")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.label_137.setFont(font4)
        self.label_137.setStyleSheet(u"background-color:none;\n"
"color: rgb(141, 141, 141);\n"
"border:0p;")
        self.label_137.setAlignment(Qt.AlignCenter)

        self.verticalLayout_120.addWidget(self.label_137)


        self.verticalLayout_119.addWidget(self.frame_192)


        self.horizontalLayout_50.addWidget(self.frame_191)


        self.verticalLayout_9.addWidget(self.frame_181)

        self.frame_180 = QFrame(self.frame_8)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setStyleSheet(u"border:1px solid lightgrey;")
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.frame_186 = QFrame(self.frame_180)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setStyleSheet(u"border:0px;")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_186)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.labelLift = QLabel(self.frame_186)
        self.labelLift.setObjectName(u"labelLift")
        self.labelLift.setFont(font3)
        self.labelLift.setStyleSheet(u"background-color:none;\n"
"color:black;\n"
"border:0px;")
        self.labelLift.setAlignment(Qt.AlignCenter)

        self.verticalLayout_114.addWidget(self.labelLift)


        self.horizontalLayout_49.addWidget(self.frame_186)

        self.frame_187 = QFrame(self.frame_180)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setStyleSheet(u"border:0px;")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_187)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.frame_188 = QFrame(self.frame_187)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_188)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.label_135 = QLabel(self.frame_188)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font4)
        self.label_135.setStyleSheet(u"background-color:none;\n"
"color: rgb(141, 141, 141);\n"
"border:0p;")
        self.label_135.setAlignment(Qt.AlignCenter)

        self.verticalLayout_116.addWidget(self.label_135)


        self.verticalLayout_115.addWidget(self.frame_188)


        self.horizontalLayout_49.addWidget(self.frame_187)


        self.verticalLayout_9.addWidget(self.frame_180)

        self.frame_182 = QFrame(self.frame_8)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setStyleSheet(u"border:1px solid lightgrey;")
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_182)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.frame_194 = QFrame(self.frame_182)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setStyleSheet(u"border:0px;")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_194)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.labelConf = QLabel(self.frame_194)
        self.labelConf.setObjectName(u"labelConf")
        self.labelConf.setFont(font3)
        self.labelConf.setStyleSheet(u"background-color:none;\n"
"color:black;\n"
"border:0px;")
        self.labelConf.setAlignment(Qt.AlignCenter)

        self.verticalLayout_122.addWidget(self.labelConf)


        self.horizontalLayout_51.addWidget(self.frame_194)

        self.frame_195 = QFrame(self.frame_182)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setStyleSheet(u"border:0px;")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_195)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.frame_196 = QFrame(self.frame_195)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_196)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_139 = QLabel(self.frame_196)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font4)
        self.label_139.setStyleSheet(u"background-color:none;\n"
"color: rgb(141, 141, 141);\n"
"border:0p;")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.verticalLayout_124.addWidget(self.label_139)


        self.verticalLayout_123.addWidget(self.frame_196)


        self.horizontalLayout_51.addWidget(self.frame_195)


        self.verticalLayout_9.addWidget(self.frame_182)


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
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        font5.setPointSize(20)
        self.label.setFont(font5)
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
        self.label_2.setFont(font5)
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
        self.produkt1.setText(QCoreApplication.translate("Form", u"Mountainbike 1", None))
        self.photo2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.produkt2.setText(QCoreApplication.translate("Form", u"Mountainbike 2", None))
        self.label_6.setText("")
        self.photo3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.produkt3.setText(QCoreApplication.translate("Form", u"Mountainbike 3", None))
        self.labelConfidence.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; vertical-align:super;\">95%</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("Form", u"Confidence", None))
        self.labelSupport.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">300</span></p></body></html>", None))
        self.label_137.setText(QCoreApplication.translate("Form", u"Support", None))
        self.labelLift.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">200</span></p></body></html>", None))
        self.label_135.setText(QCoreApplication.translate("Form", u"Lift", None))
        self.labelConf.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">200</span></p></body></html>", None))
        self.label_139.setText(QCoreApplication.translate("Form", u"Conviction", None))
        self.label.setText(QCoreApplication.translate("Form", u"Interpretation der Eregbnisse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Marketingstrategie", None))
    # retranslateUi

