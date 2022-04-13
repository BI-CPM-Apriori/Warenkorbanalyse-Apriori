from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from ui.ergebnissframe import Ui_Form
from ui.ergebnissframe1zu2 import Ui_Form2
from ui.ergebnissframe1zu1 import Ui_Form3
from ui.mainwindow import Ui_MainWindow
from uifunctions import *
from Apriori import dataset, apriori
from Database import dbConnection, read

# GLOBALS
counter = 0
jumper = 10
confidence = 80

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("")
        self.setAcceptDrops(True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        self.flagMaxi = True
        self.initUI()

    def initUI(self):
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        frame = Ergebnissframe(self)
        frame2 = Ergebnissframe1zu2(self)
        frame3 = Ergebnissframe1zu1(self)
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
        
         ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.progress(frame))
        # TIMER IN MILLISECONDS
        self.timer.start(15)
        
        conn = dbConnection.openConn()
        cursor = conn.cursor()

        retrieved_bytes = cursor.execute(read.getProductPhoto("Mountain-300 Black, 44")).fetchone()
        for row in retrieved_bytes:
            row_to_list = [elem for elem in row]
            
        pixmap = QPixmap()
        pixmap.loadFromData(bytearray(row_to_list))
        frame.ui.photo.setPixmap(pixmap)   
        
        pixmap1 = QPixmap()
        pixmap1.loadFromData(bytearray(row_to_list))
        frame.ui.photo2.setPixmap(pixmap1)     
        
        pixmap2 = QPixmap()
        pixmap2.loadFromData(bytearray(row_to_list))
        frame.ui.photo3.setPixmap(pixmap2)   
        
        pixmap3 = QPixmap()
        pixmap3.loadFromData(bytearray(row_to_list))
        frame2.ui.photo.setPixmap(pixmap3)   
        
        pixmap4 = QPixmap()
        pixmap4.loadFromData(bytearray(row_to_list))
        frame2.ui.photo2.setPixmap(pixmap4)     
        
        pixmap5 = QPixmap()
        pixmap5.loadFromData(bytearray(row_to_list))
        frame2.ui.photo3.setPixmap(pixmap5)       
        
        pixmap6 = QPixmap()
        pixmap6.loadFromData(bytearray(row_to_list))
        frame3.ui.photo.setPixmap(pixmap6)   
        
        pixmap7 = QPixmap()
        pixmap7.loadFromData(bytearray(row_to_list))
        frame3.ui.photo2.setPixmap(pixmap7)     
        
              
        
        
    def progress (self,frame):
        global counter
        global jumper
        value = counter
        

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:25pt;">{VALUE}</span><span style=" font-size:22pt; vertical-align:center;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            frame.ui.labelConfidence.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value,frame)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > confidence:
            # STOP TIMER
            self.timer.stop()

        # INCREASE COUNTER
        counter += 0.5
        
    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value, frame):
        

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 70px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0), stop:{STOP_2} rgba(13, 72, 72, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
      

        # APPLY STYLESHEET WITH NEW VALUES
        frame.ui.progressKreis.setStyleSheet(newStylesheet)

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
        event.accept()

        
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
        
class Ergebnissframe1zu2(QWidget):
    clicked = Signal()
    
    def __init__(self, parent=None):
        super(Ergebnissframe1zu2, self).__init__(parent=parent)
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        ##Window wird Frameless gesetzt
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
    
    def mousePressEvent(self, event):
        self.clicked.emit()
        
class Ergebnissframe1zu1(QWidget):
    clicked = Signal()
    
    def __init__(self, parent=None):
        super(Ergebnissframe1zu1, self).__init__(parent=parent)
        self.ui = Ui_Form3()
        self.ui.setupUi(self)
        ##Window wird Frameless gesetzt
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
    
    def mousePressEvent(self, event):
        self.clicked.emit()


if __name__ == '__main__':

    # Param 
    # 1 = Produkte, 2 = Kategorien
    param = "1"
    ds = dataset.createDataset(param)
    print(apriori.getResult(ds, param))

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())