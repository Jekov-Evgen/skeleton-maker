from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from GUI.style.style import CONST_CREATION_SELECTION_WINDOW

class CreationSelectionWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle("Окно выбора деректории")
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        self.setStyleSheet(CONST_CREATION_SELECTION_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Выберите деректорию куда сохранить проект")
        directory_selection = QPushButton(text="Выберите дерикторию")
        directory_selection.clicked.connect(self.start_of_work)
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(directory_selection)      
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def start_of_work(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите путь к проекту")
        
        print(folder_path)