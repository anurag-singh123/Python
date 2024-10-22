from scapy.layers.inet import TCP, UDP
from scapy.packet import Raw

def filter_packets(packet, protocol):
    if protocol == "TCP" and packet.haslayer(TCP):
        return True
    elif protocol == "UDP" and packet.haslayer(UDP):
        return True
    elif protocol == "HTTP" and packet.haslayer(TCP) and packet.haslayer(Raw):
        return b"HTTP" in bytes(packet[Raw])
    return False
