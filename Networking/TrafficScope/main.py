from PyQt5.QtWidgets import QApplication
from gui import NetworkMonitor
import sys

def main():
    app = QApplication(sys.argv)
    window = NetworkMonitor()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
