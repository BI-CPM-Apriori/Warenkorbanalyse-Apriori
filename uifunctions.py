from main import *

class UIFunctions(MainWindow):

    def toggleMenu(self,maxWidth,enable):
        if enable:
            #Get Width
            width = self.ui.leftbar.width()
            maxExtend = maxWidth
            standard = 70

            #set max width
            if width == 70:
                widthExtended = maxExtend

            else:
                widthExtended = standard

            #animation
            self.animation = QPropertyAnimation(self.ui.leftbar,b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
    def toggleErgebnisse(self,maxWidth,maxWidth2,enable):
        if enable:
            #Get Width
            height = self.ui.frame_2.height()
            height2 = self.height()
            
            maxExtend = maxWidth
            maxExtend2 = maxWidth2
            standard = 0
            standard2 = 200
           
            #set max width
            if height == 0:
                heightExtended = maxExtend
            else:
                heightExtended = standard
                
            if height2 == 200:
                heightExtended2 = maxExtend2
            else:
                heightExtended2 = standard2

            #animation
            self.animation = QPropertyAnimation(self.ui.frame_2,b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(height)
            self.animation.setEndValue(heightExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
            #animation2
            self.animation2 = QPropertyAnimation(self,b"minimumHeight")
            self.animation2.setDuration(400)
            self.animation2.setStartValue(height2)
            self.animation2.setEndValue(heightExtended2)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            
