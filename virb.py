class Virb:
	def __init__(self,host):
		import requests
		self.host = host
		self.url = 'http://'+self.host+'/virb'
		#{"command":"deviceInfo"}
		r = requests.post(self.url, data = '{"command":"deviceInfo"}')
		print r.status_code
		print r.content

	def sansa():
		pass
