import virb_list
import virb

from six.moves import input

l = virb_list.VirbLister()
while( True ):
	for v in l:
		print "\t",v
	host = input("Scanning for VIRBs. Please enter one, q to quit...\n")
	if( host == "q" ):
		break
	try:
		simpleCommands = ["q","deviceInfo","snapPicture","startRecording","stopRecording"]

		v = virb.Virb(l[host])
		while( True ):
			command = input(
				"Please select a command:\n"
				"\t" + "\n\t".join(simpleCommands)+"\n"
				)
			if( command == "q"):
				break
			elif( command == "deviceInfo" ):
				info = v.deviceInfo()
				if( info["result"] ):
					for device in info["deviceInfo"]:
						print "deviceInfo:"
						for item in device:
							print "\t" + str(item) + ":" + str(device[item])
				else:
					print "failed to fetch info"
			elif( command in simpleCommands ):
				r = v.command( command )
				if( r["result"] ):
					print "Command " + command + " succeeded"
				else:
					print "Command " + command + " failed"
	except KeyError:
		print "No such VIRB. Known VIRBs:"
