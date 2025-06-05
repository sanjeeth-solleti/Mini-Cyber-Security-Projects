from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def process_packet(packet):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        print(f"\n[{timestamp}] Packet: {src} -> {dst} | Protocol: {proto}")

        if TCP in packet:
            print(f"  - TCP Segment: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"  - UDP Segment: {packet[UDP].sport} -> {packet[UDP].dport}")
        elif ICMP in packet:
            print("  - ICMP Packet")

# Sniff packets on eth0 (or change to your active interface like wlan0)
print("Starting packet capture... (Press Ctrl+C to stop)")
sniff(filter="ip", prn=process_packet, store=False)

