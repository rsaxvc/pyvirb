import requests

class Virb:
	def __init__(self,host):
		import ipaddress
		self.host = ipaddress.IPv4Address(host.address).exploded
		self.url = 'http://'+self.host +'/virb'

	def status(self):
		r = requests.post(self.url, data = '{"command":"deviceInfo"}')
		print r.status_code
		print r.content

	def startRecording(self):
		r = requests.post(self.url, data='{"command":"startRecording"}')
		if( r.status_code == 200 ):
			return self.parseResult(r)
		return false

	def stopRecording(self):
		r = requests.post(self.url, data='{"command":"stopRecording"}')
		if( r.status_code == 200 ):
			return self.parseResult(r)
		return false

	def parseResult(self,r):
		return r.json()["result"]

	def sansa():
		pass
