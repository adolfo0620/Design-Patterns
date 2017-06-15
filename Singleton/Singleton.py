class Singleton():
	singleton = None
	def __init__(self):
		if singleton == None:
			self.singleton = Singleton()
		return singleton
