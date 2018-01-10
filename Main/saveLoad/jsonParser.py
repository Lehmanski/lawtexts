import os, json 

class Parser():
	def __init__(self):
		pass

	def parse(self,path):
		self.path = path
		with open(self.path) as f:
			self.data = json.load(f)
		return self.data 


