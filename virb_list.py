from zeroconf import Zeroconf

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
	def virb_list(self):
		for virb in self.virbs:
			yield virb

