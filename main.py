from PyQt6.QtWidgets import QApplication
from GUI.initial_window import CreationSelectionWindow

if __name__ == "__main__":
    app = QApplication([])
    
    start = CreationSelectionWindow()
    
    app.exec()