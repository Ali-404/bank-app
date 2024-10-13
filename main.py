from PyQt6.QtWidgets import QApplication
from sys import argv


class App(QApplication):
    def __init__(self):
        super().__init__(argv)
        
    

    






if __name__ == "__main__":
    app = App()
    app.exec()