import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QDialog

from src.ui.model.disease import Disease
from src.module.ui_module import icon_folder, customize_widget


# gerekli modüller import ediliyor.


class DetectionScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.layout = QVBoxLayout()

        self.detected_disease = self.get_random_disease()

        self.init_ui()


    def get_random_disease(self):
        random_disease = random.randint(0,5)
        file_name = f"disease_{random_disease}"
        image = f"{icon_folder}/{file_name}.jpg"

        with open(f"src/ui/disease_info/{file_name}.txt","r",encoding="utf-8") as file:
            text = file.read()

        detected_disease = Disease(image,text)

        return detected_disease


    def init_ui(self):
        x,y = 1600,900

        image = QLabel(self)
        image.setPixmap(QPixmap(self.detected_disease.image))
        image.adjustSize()

        text = QLabel(self)
        customize_widget(text, text=self.detected_disease.text,text_size=30,color="white",font="arial")

        self.layout.addWidget(text)

        self.setLayout(self.layout)
        self.setFixedSize(x,y)
        self.setWindowTitle("HASTALIK TEŞHİSİ")
        self.setWindowIcon(QIcon(icon_folder + "glasses.png"))