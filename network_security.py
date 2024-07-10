from scapy.all import sniff


def monitor_network():
    def packet_callback(packet):
        print(packet.show())

    print("Starting network monitoring...")
    sniff(prn=packet_callback, count=10)
