CONST_COD_MAIN = """
from PyQt6.QtWidgets import QApplication
from GUI.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    
    start = MainWindow()
    
    app.exec()
"""

CONST_COD_MAIN_WINDOW = """
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ваш заголовок")

        
        self.show()
"""