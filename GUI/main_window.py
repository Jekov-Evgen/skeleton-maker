from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from GUI.style.style import CONST_MAIN_WINDOW

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Создание скелетов")
        self.setFixedSize(500, 500)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setWindowIcon(QIcon("image\icon.webp"))
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        project_name = QLabel(text="Введите имя вашего проекта")
        self.input_field = QLineEdit()
        button_for_Qt = QPushButton(text="Создать проект Qt")
        button_for_Qt.clicked.connect(self.create_Qt)
        
        control_UI.addWidget(project_name, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.input_field)
        control_UI.addWidget(button_for_Qt)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
    
    def create_Qt(self):
        print("Допустим создался")