import virb_list

from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf

zeroconf = Zeroconf()
virb_mdns_key = "_garmin-virb._tcp.local."
browser = ServiceBrowser(zeroconf, virb_mdns_key, virb_list.VirbListener() )
try:
    virb = input("Scanning for VIRBs. Please enter one...\n")
    if( virb_mdns_key not in virb ):
        virb = virb + "." + virb_mdns_key
    print virb
finally:
    zeroconf.close()





