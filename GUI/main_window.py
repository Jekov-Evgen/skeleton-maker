from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QFileDialog
from GUI.style.style import CONST_MAIN_WINDOW
from Logics.Qt.logic_for_Qt import create_project_Qt
from Logics.Django.logic_for_django import create_project_Django
from Logics.Web.Standart_web.standart_web import create_standard_web_project
from Logics.Flask.logic_for_flask import create_project_Flask
from Logics.Click.logic_for_click import create_project_click
from Logics.Docker_.logic_for_docker import create_project_Docker

def error_window():
    error = QMessageBox()
    error.setWindowTitle("Ошибка")
    error.setWindowIcon(QIcon(r"image\icon.webp"))
    error.setText("Скорее всего такая уже существует")
    error.exec()
    
def window_of_success():
    success = QMessageBox()
    success.setWindowTitle("Успех")
    success.setWindowIcon(QIcon(r"image\icon.webp"))
    success.setText("Ваш проект создан")
    success.exec()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Создание скелетов")
        self.showFullScreen()
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setWindowIcon(QIcon("image\icon.webp"))
        
        self.success_window_output = True
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        project_name = QLabel(text="Введите имя вашего проекта")
        self.input_field = QLineEdit()
        button_for_Qt = QPushButton(text="Создать проект Qt")
        button_for_Django = QPushButton(text="Создать проект Django")
        button_for_standart_web = QPushButton(text="Создать стандартый проект веба")
        button_for_Flask = QPushButton(text="Создать проект Flask")
        button_for_click = QPushButton(text="Создать проект click")
        button_for_Docker = QPushButton(text="Создать проект Docker")
        
        button_for_Qt.clicked.connect(self.create_Qt)
        button_for_Django.clicked.connect(self.create_Django)
        button_for_standart_web.clicked.connect(self.create_standart_web)
        button_for_Flask.clicked.connect(self.create_Flask)
        button_for_click.clicked.connect(self.create_click)
        button_for_Docker.clicked.connect(self.create_Docker)
        
        control_UI.addWidget(project_name, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.input_field)
        control_UI.addWidget(button_for_Qt)
        control_UI.addWidget(button_for_Django)
        control_UI.addWidget(button_for_standart_web)
        control_UI.addWidget(button_for_Flask)
        control_UI.addWidget(button_for_click)
        control_UI.addWidget(button_for_Docker)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
    
    def create_Qt(self):
        try:
            name_folder = self.input_field.text()
            folder_path = QFileDialog.getExistingDirectory(self, "Выберите путь к проекту")
            create_project_Qt(name_folder, folder_path)
        except:
            error_window()
            self.success_window_output = False
            
        if self.success_window_output == True: 
            window_of_success()
    
    def create_Django(self):
        try:
            name_folder = self.input_field.text()
            folder_path = QFileDialog.getExistingDirectory(self, "Выберите путь к проекту")
            create_project_Django(name_folder, folder_path)
        except:
            error_window()
            self.success_window_output = False
            
        if self.success_window_output == True: 
            window_of_success()
        
    def create_standart_web(self):
        try:
            name_folder = self.input_field.text()
            folder_path = QFileDialog.getExistingDirectory(self, "Выберите путь к проекту")
            create_standard_web_project(name_folder, folder_path)
        except:
            error_window()
            self.success_window_output = False
        
        if self.success_window_output == True:
            window_of_success()
        
    def create_Flask(self):
        try:
            name_folder = self.input_field.text()
            folder_path = QFileDialog.getExistingDirectory(self, "Выберите путь к проекту")
            create_project_Flask(name_folder, folder_path)
        except:
            error_window()
            self.success_window_output = False
            
        if self.success_window_output == True: 
            window_of_success()
            
    def create_click(self):
        try:
            name_folder = self.input_field.text()
            folder_path = QFileDialog.getExistingDirectory(self, "Выберите путь к проекту")
            create_project_click(name_folder, folder_path)
        except:
            error_window()
            self.success_window_output = False
            
        if self.success_window_output == True: 
            window_of_success()
            
    def create_Docker(self):
        try:
            name_folder = self.input_field.text()
            folder_path = QFileDialog.getExistingDirectory(self, "Выберите путь к проекту")
            create_project_Docker(name_folder, folder_path)
        except:
            error_window()
            self.success_window_output = False
            
        if self.success_window_output == True: 
            window_of_success()