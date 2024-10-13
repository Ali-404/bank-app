from PyQt6.QtWidgets import QSplashScreen,QApplication #QApplication for test
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
import screeninfo
from math import floor

import os.path as path
# for test
import sys

class SplashScreen(QSplashScreen):
    # had onSplashClose ghan7toha mn main.py bach ngolih fach mor splashScreen ybyn login page
    def __init__(self, onSplashClose):
        
        # splash screen size
        SCREEN_WIDTH = screeninfo.get_monitors()[0].width
        SCREEN_HEIGHT = screeninfo.get_monitors()[0].height
        
        # duration bach tsd splash screen
        DURATION = 5000
        
        
        # loadit image bach tban f splashScreen
        pxMap = QPixmap()
        pxMap.load( path.join(path.pathsep , "../assets/1.png"))
        pxMap.scaledToWidth(SCREEN_WIDTH)
        pxMap.scaledToHeight(SCREEN_HEIGHT)
        
        # sawb splashScreen(parent) o loadi liha pixelMap (image)
        super().__init__(pxMap)

   
        # changer size dial window
        self.geometry().setWidth(floor(SCREEN_WIDTH * 0.3))
        self.geometry().setHeight(floor(SCREEN_HEIGHT * 0.4))
        # bynha
        self.show()
        
        # closi splashScreen o runi dik onSplashClose mor DURATION
        QTimer.singleShot(DURATION, lambda: self.close() and onSplashClose() )
        


# just for test
# had part khsha tkon normalement f app li kayna f main.py 
# but madam kola wa7d fina khdam f page raso khaso ydir tests haka tal lkhr 3ad najouti dik window f main.py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    spl = SplashScreen(app.quit)
    sys.exit(app.exec())
        