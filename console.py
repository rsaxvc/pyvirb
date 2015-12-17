import virb_list
import virb

from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf

zeroconf = Zeroconf()
virb_mdns_key = "_garmin-virb._tcp.local."
browser = ServiceBrowser(zeroconf, virb_mdns_key, virb_list.VirbListener() )
try:
	host = input("Scanning for VIRBs. Please enter one...\n")
	if( virb_mdns_key not in host ):
		host = host + "." + virb_mdns_key
	v = virb.Virb(host)
finally:
    zeroconf.close()





