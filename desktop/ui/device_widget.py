from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class DeviceWidget(QWidget):
    def __init__(self, ip, status, parent=None):
        super().__init__(parent)
        self.ip = ip
        self.status = status
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)

        ip_label = QLabel(self.ip)
        ip_label.setStyleSheet("""
            font-size: 16px;
            color: black;
            font-weight: bold;
            font-family: 'Courier New', monospace;
        """)
        layout.addWidget(ip_label)

        layout.addStretch()

        connect_btn = QPushButton("Connect")
        connect_btn.setFixedSize(100, 35)
        connect_btn.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
        """)
        connect_btn.clicked.connect(self.connect_device)
        layout.addWidget(connect_btn)

        self.setStyleSheet("""
            DeviceWidget {
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 8px;
                margin: 3px;
            }
            DeviceWidget:hover {
                background-color: #f9f9f9;
                border-color: #999999;
            }
        """)

    def connect_device(self):
        parent_window = self.parent()
        while parent_window and not hasattr(parent_window, 'connect_to_device'):
            parent_window = parent_window.parent()
        if parent_window:
            parent_window.connect_to_device(self.ip)