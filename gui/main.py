# main.py — WiFi Cloner Pro GUI Interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WiFi Cloner Pro")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("WiFi Cloner Pro GUI", self)
        self.label.move(130, 50)

        self.scan_button = QPushButton("Scan WiFi", self)
        self.scan_button.move(150, 120)
        self.scan_button.clicked.connect(self.scan_wifi)

    def scan_wifi(self):
        self.label.setText("Scanning nearby WiFi...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
