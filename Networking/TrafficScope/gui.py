from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton
from monitor import PacketMonitor
import threading

class NetworkMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Network Traffic Monitor')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel('Monitor Incoming and Outgoing Traffic', self)
        layout.addWidget(self.label)

        # Protocol Filters
        self.tcp_filter = QCheckBox('TCP', self)
        self.udp_filter = QCheckBox('UDP', self)
        self.http_filter = QCheckBox('HTTP', self)
        layout.addWidget(self.tcp_filter)
        layout.addWidget(self.udp_filter)
        layout.addWidget(self.http_filter)

        # Start and Stop buttons
        self.start_btn = QPushButton('Start Monitoring', self)
        self.start_btn.clicked.connect(self.start_monitoring)
        layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton('Stop Monitoring', self)
        self.stop_btn.clicked.connect(self.stop_monitoring)
        layout.addWidget(self.stop_btn)

        self.setLayout(layout)
        self.monitor_thread = None
        self.packet_monitor = None

    def start_monitoring(self):
        protocol = 'TCP' if self.tcp_filter.isChecked() else 'UDP' if self.udp_filter.isChecked() else 'HTTP'
        self.packet_monitor = PacketMonitor(protocol, self.display_packet)
        self.monitor_thread = threading.Thread(target=self.packet_monitor.start)
        self.monitor_thread.start()

    def stop_monitoring(self):
        if self.packet_monitor:
            self.packet_monitor.stop()
        if self.monitor_thread:
            self.monitor_thread.join()

    def display_packet(self, packet):
        self.label.setText(str(packet.summary()))
