from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from mainwindow import Ui_MainWindow
from uifunctions import *
import pyodbc
import pandas as pd
from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder


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
    dataset = []
    products = []

    server_name = 'NB-DK-DELL\SQLEXPRESS' 
    db_name = 'AdventureWorks2019' 
    connection_str =  'Driver={SQL Server};' + 'Server=' + server_name + ";Database=" + db_name + ";Trusted_Connection=yes;"
    conn = pyodbc.connect(connection_str)
    cursor = conn.cursor()

    #Sample select query
    cursor.execute("SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[Product].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] ORDER BY [SalesOrderID] ASC;") 
    row = cursor.fetchone()
    lastID = row[0]
    while row: 
        if lastID == row[0]:
            products.append(row[1])
        else:
            dataset.append(products)
            products = []
            products.append(row[1])
        print("x")
        lastID = row[0]
        row = cursor.fetchone()

    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    
    frequent_itemsets = apriori(df,min_support=0.025,use_colnames=True)
    frequent_itemsets.sort_values('support',ascending=False)
    rules = association_rules(frequent_itemsets,metric='lift',min_threshold=10)
    rules.sort_values('lift',ascending=False)

    result = rules[['antecedents','consequents','support','confidence','lift']]

    result.sort_values('confidence',ascending=False)

    print(result)

    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.show()


    sys.exit(app.exec_())