from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QSlider, QComboBox, QGroupBox, QCheckBox, QPushButton)
from PySide6.QtCore import Qt, Signal

class SettingsPanel(QWidget):
    config_changed = Signal(dict)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        # Mode Selection
        mode_group = QGroupBox("Upscaling Mode")
        mode_layout = QVBoxLayout(mode_group)
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Spatial (Fast)", "Balanced", "CNN (Ultra)"])
        mode_layout.addWidget(self.mode_combo)
        layout.addWidget(mode_group)

        # Scale Factor
        scale_group = QGroupBox("Scaling")
        scale_layout = QVBoxLayout(scale_group)
        scale_layout.addWidget(QLabel("Factor (1.2x - 2.0x)"))
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setRange(12, 20)
        self.scale_slider.setValue(15)
        scale_layout.addWidget(self.scale_slider)
        layout.addWidget(scale_group)

        # Sharpening
        sharp_group = QGroupBox("Image Quality")
        sharp_layout = QVBoxLayout(sharp_group)
        sharp_layout.addWidget(QLabel("Sharpness"))
        self.sharp_slider = QSlider(Qt.Horizontal)
        self.sharp_slider.setRange(0, 100)
        self.sharp_slider.setValue(50)
        sharp_layout.addWidget(self.sharp_slider)
        
        self.temporal_check = QCheckBox("Temporal Stabilization")
        sharp_layout.addWidget(self.temporal_check)
        layout.addWidget(sharp_group)

        layout.addStretch()
