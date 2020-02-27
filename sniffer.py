from scapy.all import *
import time
__author__ = 'mjoker23'
__version__ = '1.0'
__email__ = 'mjoker22mjoker22@gmail.com'
def sniffer(packet):
         print(packet.summary())
         time.sleep(5)
         print()
         return
while True:
        sniff(iface="eth0",prn=sniffer)

