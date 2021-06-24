
import sys
from PyQt5.QtWidgets import QApplication, QWidget


def app():
    application = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("My First PyQt Application")
    w.show()
    sys.exit(application.exec_())

app()