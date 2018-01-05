class Directive():
	'''
	'''
	def __init__(self, name, code):
		self.name = name 
		self.code = code 
		self.userConfirmed = False
		self.programSuggested = False 


class MRL(Directive):
	'''
	'''
	def __init__(self):
		super(MRL, self).__init__('MRL','2006/42/EG')

	def decide(self):
		pass
