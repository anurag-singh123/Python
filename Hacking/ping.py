import os
from scapy.all import ARP, Ether, srp

def scan_and_ping(ip_range):
    arp_req = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    ans, _ = srp(broadcast/arp_req, timeout=2, verbose=False)
    
    for sent, received in ans:
        ip = received.psrc
        print(f"Pinging {ip}...")
        if os.system(f"ping -c 1 {ip} > /dev/null 2>&1") == 0:
            print(f"{ip} is reachable.")
        else:
            print(f"{ip} is not reachable.")

if __name__ == "__main__":
    scan_and_ping("192.168.1.1/24")  # Replace with your network range
