# Project Structure

```
desktop/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── test.py                   # Original test file (kept for reference)
├── README.md                 # Installation and usage instructions
├── PROJECT_STRUCTURE.md      # This file
│
├── services/                 # Backend business logic
│   ├── __init__.py
│   ├── device_scanner.py     # Network scanning functionality
│   └── device_controller.py  # Device communication logic
│
└── ui/                       # Frontend user interface
    ├── __init__.py
    ├── main_window.py        # Main application window
    └── device_widget.py      # Individual device display component
```

## Architecture Overview

### Backend Services (`services/`)
- **DeviceScanner**: Handles network scanning using socket connections
- **DeviceController**: Manages device communication and state

### Frontend UI (`ui/`)
- **MainWindow**: Main application interface and coordination
- **DeviceWidget**: Reusable component for displaying individual devices

### Benefits of This Structure
1. **Separation of Concerns**: UI and business logic are separate
2. **Modularity**: Components can be developed and tested independently
3. **Reusability**: Services can be used in different UI contexts
4. **Maintainability**: Easier to locate and modify specific functionality
5. **Scalability**: Easy to add new features without affecting existing code

## Running the Application

```bash
python main.py
```

The main.py file now serves as a clean entry point that imports and coordinates the modular components.