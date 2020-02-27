from scapy.all import *
import time
def sniffer(packet):
         print(packet.summary())
         time.sleep(5)
         print()
         return
while True:
        sniff(iface="eth0",prn=sniffer)

