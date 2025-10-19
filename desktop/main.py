import sys
from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("KOReader Controller")
    app.setOrganizationName("KOReader Tools")

    # Set application style
    app.setStyleSheet("""
        QMainWindow {
            background-color: white;
        }
    """)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()