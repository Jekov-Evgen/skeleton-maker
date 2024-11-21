from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from GUI.style.style import CONST_MAIN_WINDOW
from Logics.logic_for_Qt import create_project_Qt

def error_window():
    error = QMessageBox()
    error.setWindowTitle("Ошибка")
    error.setWindowIcon(QIcon("image\icon.webp"))
    error.setText("Скорее всего такая уже существует")
    error.exec()
    
def window_of_success():
    success = QMessageBox()
    success.setWindowTitle("Успех")
    success.setWindowIcon(QIcon("image\icon.webp"))
    success.setText("Ваш проект создан")
    success.exec()

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
        try:
            name_folder = self.input_field.text()
            create_project_Qt(name_folder)
        except:
            error_window()
            
        window_of_success()