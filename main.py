from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from ergebnissframe import Ui_Form
from mainwindow import Ui_MainWindow
from uifunctions import *
from Apriori import dataset, apriori


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("GodundLassewerdenreich")
        self.setAcceptDrops(True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        self.flagMaxi = True
        self.initUI()

    def initUI(self):
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        frame = Ergebnissframe(self)
        frame2 = Ergebnissframe(self)
        frame3 = Ergebnissframe(self)
        frame4 = Ergebnissframe(self)

        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        frame.setGraphicsEffect(self.shadow)
        
        self.shadow1 = QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(20)
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow1.setColor(QColor(0, 0, 0, 60))
        frame2.setGraphicsEffect(self.shadow1)
        
        self.shadow2 = QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(20)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.shadow2.setColor(QColor(0, 0, 0, 60))
        frame3.setGraphicsEffect(self.shadow2)
        
        self.shadow3 = QGraphicsDropShadowEffect(self)
        self.shadow3.setBlurRadius(20)
        self.shadow3.setXOffset(0)
        self.shadow3.setYOffset(0)
        self.shadow3.setColor(QColor(0, 0, 0, 60))
        frame4.setGraphicsEffect(self.shadow3)
        
        frame2.clicked.connect(self.testing)
  
        self.ui.results.addWidget(frame)
        self.ui.results.addWidget(frame2)
        self.ui.results.addWidget(frame3)
        self.ui.results.addWidget(frame4)
  
        self.ui.results.addStretch()
        #Define UI action
        self.ui.closeEvent = self.closeEvent
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.maximizeButton.clicked.connect(self.maximize)
        self.ui.minimizeButton.clicked.connect(self.minimize)

        self.ui.btnToggle.clicked.connect(lambda bda: UIFunctions.toggleMenu(self,250,True))
        frame.clicked.connect(lambda: UIFunctions.toggleErgebnisse(frame,70,270,True))
        frame2.clicked.connect(lambda: UIFunctions.toggleErgebnisse(frame2,70,270,True))
        frame3.clicked.connect(lambda: UIFunctions.toggleErgebnisse(frame3,70,270,True))
        frame4.clicked.connect(lambda: UIFunctions.toggleErgebnisse(frame4,70,270,True))

        #Change View (Pages)
        self.ui.btnDashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard))
        self.ui.btnAnalyse.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.analyse))

    def testing(self):
        print("hallo")
         
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


class Ergebnissframe(QWidget):
    clicked = Signal()
    
    def __init__(self, parent=None):
        super(Ergebnissframe, self).__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ##Window wird Frameless gesetzt
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        
    
    def mousePressEvent(self, event):
        self.clicked.emit()
        
if __name__ == '__main__':

    # Param 
    # 1 = Produkte, 2 = Kategorien
    #param = "1"
    #ds = dataset.createDataset(param)
    #print(apriori.getResult(ds, param))

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())