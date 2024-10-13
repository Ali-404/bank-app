from PyQt6.QtWidgets import QApplication
from sys import argv,exit


class App(QApplication):
    def __init__(self):
        super().__init__(argv)
        
    

    






if __name__ == "__main__":
    app = App()
    exit(app.exec())