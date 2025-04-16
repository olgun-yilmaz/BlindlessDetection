import os
import numpy as np
import tkinter as tk
from tkinter import filedialog

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QMessageBox, QLabel

from src.ui.detection_screen import DetectionScreen
from src.ui.ui_module import set_checkbox_icon, icon_folder, customize_widget, get_features


# gerekli modüller import ediliyor.

class MainMenu(QWidget):  # kullanıcının ilk karşılaştığı pencere

    def __init__(self):
        super().__init__()
        self.init_ui()

    def open_file(self):  # dosya işlemi yapan fonksiyon
        root = tk.Tk()
        root.withdraw()

        path = filedialog.askopenfilename()  # dosyayı aç

        if not path:  # dosya var mı?
            return

        self.go_to_detection_screen()


    def click(self):  # seçme butonlarına tıklandığında çağrılan fonksiyon
        button = self.sender()
        icon_name = button.objectName()

        if button.isChecked():  # işaretlendiyse
            icon_name = icon_name[5:]  # renki icon
        else:  # işaretlenmediyse
            icon_name = "dont_" + icon_name  # siyah-beyaz icon

        button.setObjectName(icon_name)  # nesne ismi sonraki sefer için güncelleniyor.
        path = icon_folder + icon_name + ".png"  # icon yolu

        set_checkbox_icon(checkbox=button, path=path)  # icon güncelleniyor.


    def create_check_box(self, icon_name):  # check_box oluşturan fonksiyon
        check_box = QCheckBox(self)

        check_box.setText(icon_name)

        path = icon_folder + icon_name + ".png"
        check_box.setObjectName(icon_name)  # tıklanma durumuna göre değişmesi için nesne ismi olarak atanıyor.

        customize_widget(widget=check_box)  # default olarak özelleştiriliyor.
        set_checkbox_icon(checkbox=check_box, path=path)  # icon yerleştir.

        check_box.clicked.connect(self.click)  # tıklanırsa fonksiyona git.

        return check_box


    def go_to_detection_screen(self):
        detection_screen = DetectionScreen()  # analiz sonucunu gösteren pencere
        detection_screen.exec_()

    def init_ui(self):
        x, y = 1600, 900  # pencere boyutu
        button_size = 100  # buton ikonu boyutu

        background = QLabel(self)
        background.setPixmap(QPixmap(icon_folder + "main_background.jpg"))  # arka plan
        background.adjustSize()

        open_button = QPushButton(self)  # dosya yükleme butonu
        open_button.setToolTip("DOSYA YÜKLE")

        open_button.setIcon(QIcon(icon_folder + "load_button.png"))
        open_button.setIconSize(QSize(button_size, button_size))
        open_button.setStyleSheet(get_features(color="white"))

        open_button.clicked.connect(self.open_file)

        v_box = QVBoxLayout()

        v_box.addWidget(open_button)

        self.setLayout(v_box)
        self.setWindowTitle("BLINDLESS DETECTION")
        self.setFixedSize(x, y)
        self.setWindowIcon(QIcon("analysis_icon.png"))
        self.show()
