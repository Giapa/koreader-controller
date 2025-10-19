from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton, QScrollArea,
    QLabel, QProgressBar, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from services.device_scanner import DeviceScanner
from services.device_controller import DeviceController
from ui.device_widget import DeviceWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scanner = DeviceScanner()
        self.controller = DeviceController()
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        self.setWindowTitle("KOReader Controller")
        self.setGeometry(300, 300, 600, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("KOReader Controller")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #2c3e50; margin-bottom: 10px;")
        layout.addWidget(title)

        # Add rescan button under title (centered)
        rescan_container = QWidget()
        rescan_layout = QHBoxLayout(rescan_container)
        rescan_layout.setContentsMargins(0, 0, 0, 0)

        rescan_layout.addStretch()  # Left spacer

        self.rescan_button = QPushButton("Rescan devices")
        self.rescan_button.setFixedSize(150, 35)
        self.rescan_button.setVisible(False)  # Hidden by default
        self.rescan_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
                margin-bottom: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.rescan_button.clicked.connect(self.rescan_network)
        rescan_layout.addWidget(self.rescan_button)

        rescan_layout.addStretch()  # Right spacer

        layout.addWidget(rescan_container)

        self.instructions = QLabel(
            "Click 'Scan Network' to find KOReader devices with HTTP servers running on port 8080"
        )
        self.instructions.setWordWrap(True)
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions.setStyleSheet("color: #7f8c8d; font-size: 12px; margin-bottom: 15px;")
        layout.addWidget(self.instructions)

        self.scan_button = QPushButton("Scan Network")
        self.scan_button.setMinimumHeight(45)
        self.scan_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
            }
        """)
        layout.addWidget(self.scan_button)


        self.devices_label = QLabel("Found Devices:")
        self.devices_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.devices_label.setStyleSheet("color: #2c3e50; margin-top: 10px;")
        self.devices_label.setVisible(False)
        layout.addWidget(self.devices_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setVisible(False)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid #cccccc;
                border-radius: 8px;
                background-color: white;
            }
        """)

        self.devices_container = QWidget()
        self.devices_container.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.devices_layout = QVBoxLayout(self.devices_container)
        self.devices_layout.setSpacing(5)
        self.devices_layout.setContentsMargins(10, 10, 10, 10)

        self.scroll_area.setWidget(self.devices_container)
        layout.addWidget(self.scroll_area)

        self.connected_widget = QWidget()
        self.connected_widget.setVisible(False)
        self.connected_layout = QVBoxLayout(self.connected_widget)

        self.connected_label = QLabel("")
        self.connected_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.connected_label.setStyleSheet("""
            font-size: 18px;
            color: black;
            font-weight: bold;
            margin: 20px;
        """)
        self.connected_layout.addWidget(self.connected_label)

        self.buttons_widget = QWidget()
        self.buttons_layout = QHBoxLayout(self.buttons_widget)

        self.prev_button = QPushButton("Previous Page")
        self.prev_button.setFixedSize(150, 50)
        self.prev_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
        self.prev_button.clicked.connect(self.previous_page)
        self.buttons_layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Next Page")
        self.next_button.setFixedSize(150, 50)
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
        self.next_button.clicked.connect(self.next_page)
        self.buttons_layout.addWidget(self.next_button)

        self.connected_layout.addWidget(self.buttons_widget)

        layout.addWidget(self.connected_widget)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("color: #7f8c8d; font-style: italic;")
        layout.addWidget(self.status_label)

    def connect_signals(self):
        self.scan_button.clicked.connect(self.start_scan)
        self.scanner.device_found.connect(self.add_device)
        self.scanner.scan_finished.connect(self.scan_complete)

    def start_scan(self):
        if self.scanner.is_scanning:
            return

        for i in reversed(range(self.devices_layout.count())):
            child = self.devices_layout.itemAt(i).widget()
            if child:
                child.setParent(None)

        self.scroll_area.setVisible(False)
        self.devices_label.setVisible(False)
        self.scan_button.setText("Scanning...")
        self.scan_button.setEnabled(False)
        self.status_label.setText("Scanning network for KOReader devices...")

        self.scanner.start()

    def add_device(self, ip, status):
        if not self.scroll_area.isVisible():
            self.scroll_area.setVisible(True)
            self.devices_label.setVisible(True)
            self.status_label.setText("Found devices:")

        device_widget = DeviceWidget(ip, status)
        self.devices_layout.addWidget(device_widget)


    def scan_complete(self):
        self.scan_button.setText("Scan Network")
        self.scan_button.setEnabled(True)

        device_count = self.devices_layout.count()
        if device_count == 0:
            self.status_label.setText("No KOReader devices found. Make sure HTTP server is running.")
        else:
            self.status_label.setText(f"Scan complete. Found {device_count} device(s).")

    def connect_to_device(self, ip):
        self.controller.connect_device(ip)
        self.connected_label.setText(f"Connected to: {ip}")
        self.connected_widget.setVisible(True)

        # Show rescan button when connected
        self.rescan_button.setVisible(True)

        # Hide device scanning UI when connected
        self.scroll_area.setVisible(False)
        self.devices_label.setVisible(False)
        self.scan_button.setVisible(False)
        self.status_label.setVisible(False)
        self.instructions.setVisible(False)

    def previous_page(self):
        success = self.controller.previous_page()
        if not success:
            self.show_device_error()

    def next_page(self):
        success = self.controller.next_page()
        if not success:
            self.show_device_error()

    def show_device_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Device Error")
        msg.setText("Maybe the device you selected is not a KOReader device, try another one")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def rescan_network(self):
        # Disconnect from current device
        self.controller.disconnect_device()

        # Hide connected device view and rescan button
        self.connected_widget.setVisible(False)
        self.rescan_button.setVisible(False)

        # Show scanning UI again
        self.scan_button.setVisible(True)
        self.status_label.setVisible(True)
        self.instructions.setVisible(True)

        # Start scan automatically
        self.start_scan()