import tkinter as tk
from tkinter import filedialog

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QCheckBox, QLabel

from src.ui.view.detection_screen import DetectionScreen
from src.module.ui_module import set_checkbox_icon, icon_folder, customize_widget, get_features
from src.ui.view.loading_dialog import LoadingDialog


# gerekli modüller import ediliyor.

class MainMenu(QWidget):  # kullanıcının ilk karşılaştığı pencere

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.model = None

    def get_model(self):
        loader_app = LoadingDialog()
        loader_app.exec_()
        return loader_app.model

    def open_file(self):  # dosya işlemi yapan fonksiyon
        root = tk.Tk()
        root.withdraw()

        path = filedialog.askopenfilename()  # dosyayı aç

        if not path:  # dosya var mı?
            return

        if self.model is None:
            self.model = self.get_model()

        self.go_to_detection_screen(path)


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


    def go_to_detection_screen(self,path):
        detection_screen = DetectionScreen(path,self.model)  # analiz sonucunu gösteren pencere
        detection_screen.exec_()

    def init_ui(self):
        x,y = 1600,900  # pencere boyutu
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
        self.setWindowIcon(QIcon(icon_folder+"doctor.png"))
        self.show()