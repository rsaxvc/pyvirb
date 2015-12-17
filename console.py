import virb_list
import virb

from six.moves import input

l = virb_list.VirbLister()
host = input("Scanning for VIRBs. Please enter one...\n")
v = virb.Virb(host)
