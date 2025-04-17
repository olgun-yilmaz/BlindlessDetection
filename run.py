import sys

from PyQt5.QtWidgets import QApplication

from src.ui.view.loading_dialog import LoadingDialog
from src.ui.view.main_menu import MainMenu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    sys.exit(app.exec_())
