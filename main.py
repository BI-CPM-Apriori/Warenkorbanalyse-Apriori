from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from mainwindow import Ui_MainWindow
from uifunctions import *
import pyodbc


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("GodundLassewerdenreich")
        self.setAcceptDrops(True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.flagMaxi = True
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Define UI action
        self.ui.closeEvent = self.closeEvent
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.maximizeButton.clicked.connect(self.maximize)
        self.ui.minimizeButton.clicked.connect(self.minimize)

        self.ui.btnToggle.clicked.connect(lambda bda: UIFunctions.toggleMenu(self,250,True))

        #Change View (Pages)
        self.ui.btnDashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard))
        self.ui.btnAnalyse.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.analyse))


    def maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.flagMaxi = True
        else:
            self.showMaximized()
            self.flagMaxi = False

    def closeEvent(self, event):
        userInfo = QMessageBox.question(self,"Bestätigung","Wollen sie die Applikation schließen ?", QMessageBox.Yes | QMessageBox.No)

        if userInfo == QMessageBox.Yes:
            event.accept()

        elif userInfo == QMessageBox.No:
            event.ignore()

    def minimize(self):
        self.showMinimized()

    def mousePressEvent(self, event):

        self.oldPos = event.globalPos()
        self.lastpos = event.pos()

    def mouseMoveEvent(self, event):
        #gesperrt Wenn Feedback Fenster geöffnet
        if (self.flagMaxi is True):
            self.showNormal()
            delta = QPoint(event.globalPos() - self.oldPos)
            # print(delta)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()



if __name__ == '__main__':
    # Create the Qt Application

    server_name = 'NB-DK-DELL\SQLEXPRESS' 
    db_name = 'AdventureWorks2019' 
    connection_str =  'Driver={SQL Server};' + 'Server=' + server_name + ";Database=" + db_name + ";Trusted_Connection=yes;"
    conn = pyodbc.connect(connection_str)

    #Sample select query
    conn.execute("SELECT * FROM Production.Product;") 
    row = conn.fetchone() 
    while row: 
        print(row[0])
        row = conn.fetchone()

    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.show()


    sys.exit(app.exec_())