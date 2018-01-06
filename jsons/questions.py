from productClasses_all import Generic

class Question():
	def __init__(self, text):
		self.text = text
		self.posChild = None
		self.negChild = None

class Result():
	def __init__(self, text, bool, pClass = Generic()):
		self.text = text
		self.bool = bool 
		self.pClass = pClass

class Test():
	def __init__(self):
		pass

	def start(self,Q1):
		result = self.iter(Q1)
		return result 


	def next(self, question, answer):
		if answer == 'y':
			return question.posChild
		elif answer == 'n':
			return question.negChild
		else:
			print('fuck')

	def iter(self, question):
		while not type(question) is Result:
			print(question.text)
			a = None
			while not a in ['y','n']:
				a = input('y/n \n')
			question = self.next(question,a)
		print(question.text)
		return question