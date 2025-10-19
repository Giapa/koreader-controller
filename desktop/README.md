# KOReader Controller Desktop

A PyQt desktop application for scanning and controlling KOReader devices on your network.

## Installation Options

### Option 1: PyQt6 (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
pip install -r requirements.txt
python main.py
```

### Option 2: PyQt5 (If PyQt6 has compatibility issues)
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
pip install -r requirements-alt.txt
python main_qt5.py
```

### Option 3: System Package Manager (Linux)
```bash
# Ubuntu/Debian
sudo apt install python3-pyqt5 python3-requests
python main_qt5.py

# Fedora
sudo dnf install python3-qt5 python3-requests
python main_qt5.py

# Arch
sudo pacman -S python-pyqt5 python-requests
python main_qt5.py
```

## Troubleshooting

If you get PyQt6 import errors:
1. Try the PyQt5 version: `python main_qt5.py`
2. Use system packages instead of pip
3. Check if you need Qt development libraries

## Features

- Network device scanning for KOReader HTTP servers
- Device list display with connection status
- Simple and clean interface
- Cross-platform support
- Both PyQt5 and PyQt6 versions available