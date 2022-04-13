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
import pandas as pd

# GLOBALS
counter = 0
jumper = 10


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
        
        #frame.clicked.connect(self.testing)
  
        
        #Define UI action
        self.ui.closeEvent = self.closeEvent
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.maximizeButton.clicked.connect(self.maximize)
        self.ui.minimizeButton.clicked.connect(self.minimize)

        self.ui.btnToggle.clicked.connect(lambda bda: UIFunctions.toggleMenu(self,250,True))
        

        #Change View (Pages)
        self.ui.btnDashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard))
        self.ui.btnAnalyse.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.analyse))
        
        
        
        
        
    def addPanel(self, row):
        
        conn = dbConnection.openConn()
        cursor = conn.cursor()

        print(list(row['antecedents']), list(row['consequents']), row['support'], row['confidence'], row['lift'], row['conviction'])
        print(row['support'])
        
        if (len(list(row['antecedents'])) == 2 and len(list(row['consequents'])) == 1):
            
            frame = Ergebnissframe(self)
            retrieved_bytes = cursor.execute(read.getProductPhoto(list(row['antecedents'])[0])).fetchone()
            retrieved_bytes2 = cursor.execute(read.getProductPhoto(list(row['antecedents'])[1])).fetchone()
            retrieved_bytes3 = cursor.execute(read.getProductPhoto(list(row['consequents'])[0])).fetchone()
            
            for rows in retrieved_bytes:
                row_to_list = [elem for elem in rows]
            
            for rows in retrieved_bytes2:
                row_to_list1 = [elem for elem in rows]
            
            for rows in retrieved_bytes3:
                row_to_list2 = [elem for elem in rows]
            
            pixmap = QPixmap()
            pixmap.loadFromData(bytearray(row_to_list))
            frame.ui.photo.setPixmap(pixmap)       
            
            pixmap1 = QPixmap()
            pixmap1.loadFromData(bytearray(row_to_list1))
            frame.ui.photo2.setPixmap(pixmap1)   
            
            pixmap2 = QPixmap()
            pixmap2.loadFromData(bytearray(row_to_list2))
            frame.ui.photo3.setPixmap(pixmap2)
            
            frame.ui.produkt1.setText(str(list(row['antecedents'])[0]))
            frame.ui.produkt2.setText(str(list(row['antecedents'])[1]))
            frame.ui.produkt3.setText(str(list(row['consequents'])[0]))
              
        elif (len(list(row['antecedents'])) == 1 and len(list(row['consequents'])) == 2):
            frame = Ergebnissframe1zu2(self)
            retrieved_bytes = cursor.execute(read.getProductPhoto(list(row['antecedents'])[0])).fetchone()
            retrieved_bytes2 = cursor.execute(read.getProductPhoto(list(row['consequents'])[0])).fetchone()
            retrieved_bytes3 = cursor.execute(read.getProductPhoto(list(row['consequents'])[1])).fetchone()
            
            for rows in retrieved_bytes:
                row_to_list = [elem for elem in rows]
            
            for rows in retrieved_bytes2:
                row_to_list1 = [elem for elem in rows]
            
            for rows in retrieved_bytes3:
                row_to_list2 = [elem for elem in rows]
            
            pixmap = QPixmap()
            pixmap.loadFromData(bytearray(row_to_list))
            frame.ui.photo.setPixmap(pixmap)       
            
            pixmap1 = QPixmap()
            pixmap1.loadFromData(bytearray(row_to_list1))
            frame.ui.photo2.setPixmap(pixmap1)   
            
            pixmap2 = QPixmap()
            pixmap2.loadFromData(bytearray(row_to_list2))
            frame.ui.photo3.setPixmap(pixmap2)
            
            frame.ui.produkt1.setText(str(list(row['antecedents'])[0]))
            frame.ui.produkt2.setText(str(list(row['consequents'])[0]))
            frame.ui.produkt3.setText(str(list(row['consequents'])[1]))
            
        elif (len(list(row['antecedents'])) == 1 and len(list(row['consequents'])) == 1):
            frame = Ergebnissframe1zu1(self)
            retrieved_bytes = cursor.execute(read.getProductPhoto(list(row['antecedents'])[0])).fetchone()
            retrieved_bytes2 = cursor.execute(read.getProductPhoto(list(row['consequents'])[0])).fetchone()
            
            for rows in retrieved_bytes:
                row_to_list = [elem for elem in rows]
            
            for rows in retrieved_bytes2:
                row_to_list1 = [elem for elem in rows]
            
            pixmap = QPixmap()
            pixmap.loadFromData(bytearray(row_to_list))
            frame.ui.photo.setPixmap(pixmap)       
            
            pixmap1 = QPixmap()
            pixmap1.loadFromData(bytearray(row_to_list1))
            frame.ui.photo2.setPixmap(pixmap1)   
            
            frame.ui.produkt1.setText(str(list(row['antecedents'])[0]))
            frame.ui.produkt2.setText(str(list(row['consequents'])[0]))
            
        confidence = round(int((row['confidence']) * 100 ),0)
       
        frame.ui.labelSupport.setText(str(round(float((row['support']) * 100 ),2))+ "%")
        frame.ui.labelLift.setText(str(round((row['lift'] ),2)))
        frame.ui.labelConf.setText(str(round((row['conviction'] ),2)))
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 60))
        frame.setGraphicsEffect(shadow)
        
        self.ui.results.addWidget(frame)
        self.ui.results.addStretch()
        
        frame.clicked.connect(lambda: UIFunctions.toggleErgebnisse(frame,70,270,True))
        
        htmlText = """<p><span style=" font-size:25pt;">{VALUE}</span><span style=" font-size:22pt; vertical-align:center;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(confidence))

        frame.ui.labelConfidence.setText(newHtml)
                
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 70px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0), stop:{STOP_2} rgba(13, 72, 72, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - confidence) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
      

        # APPLY STYLESHEET WITH NEW VALUES
        frame.ui.progressKreis.setStyleSheet(newStylesheet)
        
         ## QTIMER ==> START
        #self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(lambda: self.progress(frame,confidence))
        # TIMER IN MILLISECONDS
        #self.timer.start(15)
        
        
    def progress (self,frame,confidence):
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
    #print(apriori.getResult(ds, param))
    #dataFrame = apriori.getResult(ds, param)

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    
    for index, row in apriori.getResult(ds, param).iterrows():
        mainWindow.addPanel(row)
        
    

    sys.exit(app.exec_())