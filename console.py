import virb_list
import virb

from six.moves import input

l = virb_list.VirbLister()
while( True ):
	for v in l:
		print "\t",v
	try:
		host = input("Scanning for VIRBs. Please enter one, q to quit...\n")
	except EOFError:
		break
	if( host == "q" ):
		break
	try:
		simpleCommands = [
			"q",
			"deviceInfo",
			"found",
			"locate",
			"snapPicture",
			"startRecording",
			"stopRecording",
			"status",
			"features"
			]

		v = virb.Virb(l[host])
		while( True ):
			try:
				command = input(
					"Please select a command:\n"
					"\t" + "\n\t".join(simpleCommands)+"\n"
					)
			except EOFError:
				break
			if( command == "q"):
				break
			elif( command == "features" ):
				r = v.command( command )
				if( r["result"] ):
					feature_list = {}
					while( True ):
						print "Please select a feature, or q to quit:"
						for f in r["features"]:
							if "value" in f:
								print "\t" + f["feature"] + ":" + str(f["value"])
							elif "enabled" in f:
								print "\t" + f["feature"] + ":" + str(f["enabled"])
							else:
								print "\t" + f["feature"]
							feature_list[f["feature"]] = f
						try:
							feature_name = input()
						except EOFError:
							break
						if feature_name == "q":
							break
						elif feature_name in feature_list:
							feature = feature_list[feature_name]
							#print feature_list[feature]
							if( feature["type"] == 2 ):
								feature["options"] = ["0","1"]
							if( "options" in feature ):
								option_list = feature["options"]
								while( True ):
									try:
										option = input(
											"Please select an option, or q to quit:\n"
											"\t" + "\n\t".join(option_list)+"\n"
											)
									except EOFError:
										break
									if option == "q":
										break
									elif option in option_list:
										r = v.updateFeature(feature_name,option)
										if( r["result"] ):
											break
									print "unknown option"
							else:
								print "no configurable options for " + feature_name
						else:
							print "Unable to fetch feature:", feature_name
				else:
					print "Unable to fetch features"
			elif( command == "status" ):
				r = v.command( command )
				if( r["result"] ):
					for key in r:
						print "\t"+str(key)+":"+str(r[key])
				else:
					print "Unable to fetch status"
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
			else:
				print "unknown command:",command
	except KeyError:
		print "No such VIRB. Known VIRBs:"
