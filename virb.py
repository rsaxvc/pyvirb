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
		return self.session.post(self.url, data=json.dumps(d))

	def deviceInfo(self):
		r = self.command("deviceInfo")
		if( r.status_code == 200 ):
			return r.json()["deviceInfo"][0]
		return None

	def startRecording(self):
		r = self.command("startRecording")
		if( r.status_code == 200 ):
			return self.parseResult(r)
		return false

	def stopRecording(self):
		r = self.command("stopRecording")
		if( r.status_code == 200 ):
			return self.parseResult(r)
		return false

	def parseResult(self,r):
		return r.json()["result"]

	def sansa():
		pass
