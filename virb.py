import json
import requests

class Virb:
	def __init__(self,host):
		import ipaddress
		self.host = ipaddress.IPv4Address(host.address).exploded
		self.url = 'http://'+self.host +'/virb'
		self.session = requests.Session()

	def command(self,command):
		d = {"command": command }
		r = self.session.post(self.url, data=json.dumps(d))
		if( r.status_code == 200 ):
			return r.json()
		return None

	def deviceInfo(self):
		return self.command("deviceInfo")

	def snapPicture(self):
		return self.command("snapPicture")

	def startRecording(self):
		return self.command("startRecording")

	def stopRecording(self):
		return self.command("stopRecording")
