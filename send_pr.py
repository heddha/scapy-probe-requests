# The script used to transmit probe requests via Scapy. 
# A function is designed in which all necessary parameters are set, using the specific Scapy syntax. 
# The only IE fields required to be transmitted are Supported Rates and the SSID, both can also be empty.
    
from scapy.all import *

ssid = ""
interface = "wlan0"
sender = "22:22:22:22:22:22"
dest = "ff:ff:ff:ff:ff:ff"


def send_probe_req(senderaddr, destaddr, ssid, interface):
        radiotap = RadioTap()    
        dot11 = Dot11(type=0, subtype=0x04, addr1=destaddr, addr2=senderaddr, addr3=destaddr)
        dot11_probe_req = Dot11ProbeReq() / Dot11Elt(ID="SSID", info=ssid)
        
        rates_content = b'\x00'
        rates  = Dot11Elt(ID='Rates', info=rates_content)
        
        frame = radiotap / dot11 / dot11_probe_req / rates
        sendp(frame, iface=interface)

send_probe_req(sender, dest, ssid, interface)
