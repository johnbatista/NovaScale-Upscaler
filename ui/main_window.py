from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from ui.settings import SettingsPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NovaScale v1.0")
        self.setMinimumSize(400, 650)
        self.is_running = False
        
        self.init_ui()
        self.apply_theme()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Header
        header = QLabel("NOVASCALE")
        header.setFont(QFont("Segoe UI", 26, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("color: #00d2ff; margin-bottom: 20px;")
        main_layout.addWidget(header)

        # Settings
        self.settings = SettingsPanel()
        main_layout.addWidget(self.settings)

        # Stats
        self.status_label = QLabel("STATUS: IDLE")
        self.status_label.setStyleSheet("color: #666; font-family: 'Consolas'; font-size: 12px;")
        main_layout.addWidget(self.status_label)

        # Controls
        ctrl_layout = QHBoxLayout()
        self.start_btn = QPushButton("START ENGINE")
        self.start_btn.setFixedHeight(50)
        self.start_btn.clicked.connect(self.toggle_engine)
        
        self.stop_btn = QPushButton("STOP")
        self.stop_btn.setFixedHeight(50)
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.toggle_engine)
        
        ctrl_layout.addWidget(self.start_btn)
        ctrl_layout.addWidget(self.stop_btn)
        main_layout.addLayout(ctrl_layout)

    def apply_theme(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #0d0d0f; }
            QLabel { color: #ccc; }
            QGroupBox { border: 1px solid #2a2a2e; border-radius: 6px; margin-top: 10px; font-weight: bold; color: #888; }
            QPushButton { background-color: #00d2ff; color: #000; border-radius: 4px; font-weight: bold; }
            QPushButton:hover { background-color: #00b8e6; }
            QPushButton:disabled { background-color: #222; color: #444; }
        """)

    def toggle_engine(self):
        self.is_running = not self.is_running
        self.start_btn.setEnabled(not self.is_running)
        self.stop_btn.setEnabled(self.is_running)
        self.status_label.setText(f"STATUS: {'RUNNING' if self.is_running else 'IDLE'}")
