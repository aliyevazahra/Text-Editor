from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


font_Title = QFont("Arial", 30)
font_Text = QFont("Arial", 20)


class Help(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Us")
        self.setGeometry(200, 200, 450, 250)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout(self)
        text_Title = QLabel("About Us")
        text_Title.setAlignment(Qt.AlignCenter)
        text_About = QLabel("Creat and Edit Text.\nThe sophisticated basic text editor for text.")
        text_About.setAlignment(Qt.AlignCenter)
        text_Title.setFont(font_Title)
        text_About.setFont(font_Text)
        vbox.addWidget(text_Title)
        vbox.addWidget(text_About)
        self.setLayout(vbox)
