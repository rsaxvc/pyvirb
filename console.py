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
		v = virb.Virb(l[host])
		while( True ):
			command = input(
				"Please select a command:\n"
				"\tq\n"
				"\tstartRecording\n"
				"\tstopRecording\n"
				)
			if( command == "q"):
				break
			elif( command == "startRecording" ):
				if( v.startRecording() ):
					print "started recording.",
				else:
					print "failed to start recording.",
			elif( command == "stopRecording" ):
				if( v.stopRecording() ):
					print "stopped recording.",
				else:
					print "failed to stop recording.",
	except KeyError:
		print "No such VIRB. Known VIRBs:"
