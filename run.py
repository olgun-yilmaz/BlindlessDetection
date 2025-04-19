import sys

from PyQt5.QtWidgets import QApplication

from src.ui.view.get_started_screen import GetStartedScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    get_started = GetStartedScreen()
    sys.exit(app.exec_())
