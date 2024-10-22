from scapy.all import sniff
from filters import filter_packets

class PacketMonitor:
    def __init__(self, protocol, callback):
        self.protocol = protocol
        self.callback = callback
        self.sniffing = False

    def start(self):
        self.sniffing = True
        sniff(prn=self.packet_handler, store=0)

    def stop(self):
        self.sniffing = False

    def packet_handler(self, packet):
        if self.sniffing and filter_packets(packet, self.protocol):
            self.callback(packet)
