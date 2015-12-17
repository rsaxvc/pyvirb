from zeroconf import ServiceBrowser, Zeroconf

class VirbLister(object):
	virb_mdns_key = "_garmin-virb._tcp.local."

	class VirbListener(object):
		virbs = {}
		def remove_service(self, zeroconf, type, name):
			if( name in self.virbs ):
				del self.virbs[name]
				print("VIRB %s left" % (name,))

		def add_service(self, zeroconf, type, name):
			info = zeroconf.get_service_info(type, name)
			if( name not in self.virbs ):
				self.virbs[name] = info
				print("VIRB %s found" % (name,))
		def list(self):
			for virb in self.virbs:
				yield virb
		def info(self,virb):
			return self.virbs[virb]

	def __init__(self):
		self.zeroconf = Zeroconf()
		self.listener = self.VirbListener()
		self.browser = ServiceBrowser(self.zeroconf, self.virb_mdns_key, self.listener )
	def __del__(self):
		self.zeroconf.close();
	def __getitem__(self,virb):
		return self.listener.info(virb)
	def __iter__(self):
		return self.listener.virbs.__iter__()
	def next(self):
		return self.listener.virbs.next()
