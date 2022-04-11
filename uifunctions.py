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


