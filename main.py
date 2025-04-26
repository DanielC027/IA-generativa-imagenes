from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from mainwindow import MainWindow
import sys

app = QApplication()

window = MainWindow()
window.setWindowTitle("STABLE DIFFUSION")
window.setWindowIcon(QIcon("./icon.ico"))
window.show()
sys.exit(app.exec())
