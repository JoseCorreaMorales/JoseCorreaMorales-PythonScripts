import scapy.all as scapy

def sniff_packets(iface=None):
    scapy.sniff(store=0, prn=process_packet, iface=iface)

def process_packet(packet):
    if packet.haslayer(scapy.Raw):
        print(packet[scapy.Raw].load)

sniff_packets("Ethernet")  # Reemplazar "Ethernet" con el nombre de la interfaz de red a escuchar