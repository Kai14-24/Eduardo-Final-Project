import sys
from PyQt6.QtWidgets import QApplication
from Breed import Logic


def main():
    """Main entrences to the runing the PyQt6 application for and the logic"""
    app = QApplication(sys.argv)
    window = Logic()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
