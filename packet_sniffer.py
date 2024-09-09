from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime

# Define a function to process each captured packet
def packet_analyzer(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        if TCP in packet:
            protocol_name = "TCP"
        elif UDP in packet:
            protocol_name = "UDP"
        else:
            protocol_name = "Other"
        
        # Print
