from PyQt6.QtWidgets import QSplashScreen,QApplication #QApplication for test
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
import screeninfo
from math import floor

import os.path as path
# for test
import sys

class SplashScreen(QSplashScreen):
    def __init__(self, onSplashClose):
        
        # splash screen size
        SCREEN_WIDTH = screeninfo.get_monitors()[0].width
        SCREEN_HEIGHT = screeninfo.get_monitors()[0].height
        
        DURATION = 5000
        
        
        pxMap = QPixmap()
        pxMap.load( path.join(path.pathsep , "../assets/1.png"))
        pxMap.scaledToWidth(SCREEN_WIDTH)
        pxMap.scaledToHeight(SCREEN_HEIGHT)
        
        super().__init__(pxMap)

        # load image

        self.geometry().setWidth(floor(SCREEN_WIDTH * 0.3))
        self.geometry().setHeight(floor(SCREEN_HEIGHT * 0.4))
        
        self.show()
        QTimer.singleShot(DURATION, lambda: self.close() and onSplashClose() )
        


# just for test
if __name__ == "__main__":
    app = QApplication(sys.argv)
    spl = SplashScreen(app.quit)
    sys.exit(app.exec())
        