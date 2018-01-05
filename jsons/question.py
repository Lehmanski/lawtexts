class Question():
	def __init__(self, text, posChild, negChild):
		self.text = text
		self.posChild = posChild
		self.negChild = negChild

class Result():
	def __init__(self, text, bool):
		self.text = text
		self.bool = bool 

class Test():
	def __init__(self,Q1):
		self.iter(Q1)


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



q1_rml = Question('Besteht das Erzeugniss aus miteinander Verbundenen Teilen?',
				  None,
				  None)

q2a_mrl = Question('Ist mindestens ein Teil davon beweglich?',
				None,
				None)

q2b_mrl = Question('Teile nur zu Transportzwecken getrennt?',
				None,
				None)

q3_mrl = Question('Kann das Erzeugniss fuer sich genommen die bestimmte Funktion erfuellen?',
				None,
				None)

q4a_mrl = Question('Ist das Produkt mit einem Antriebssystem ausgestattet?',
				None,
				None)

q4b_mrl = Question('Ist das Produkt zum Zusammenbau imt anderen (unvollständigen) Maschinen/Ausrüstungen gedacht?',
				None,
				None)

q5a_mrl = Question('Das Antriebssystem ist die unmittelbar eingesetzte menschliche Kraft?',
				None,
				None)
q5b_mrl = Question('Fuer ein Antriebssystem vorgesehen?',
				None,
				None)
q5c_mrl = Question('Ist das Produkt fast eine Maschine?',
				None,
				None)

q6a_mrl = Question('Ist das Antriebssystem genau spezifiziert?',
				None,
				None)
q6b_mrl = Question('Handelt es sich um ein Produkt fuer Hebevorgaenge?',
				None,
				None)
q6c_mrl = Question('Das Antriebssystem ist die unmittelbar eingesetzte tierische Kraft?',
				None,
				None)




T = Result('MRL trifft zu', False)
F = Result('MRL trifft nicht zu!', False)

resultUnvollstaendigeMaschine = Result('Unvollstaendige Maschine! (daten hier einpflegen)',True)
resultMaschine = Result('Maschine! (daten hier einpflegen)',True)

q1_rml.posChild = q2a_mrl
q1_rml.negChild = q2b_mrl

q2a_mrl.posChild = q3_mrl
q2a_mrl.negChild = F

q2b_mrl.posChild = F
q2b_mrl.negChild = q2a_mrl

q3_mrl.posChild = q4a_mrl
q3_mrl.negChild = q4b_mrl

q4a_mrl.posChild = q5a_mrl
q4a_mrl.negChild = q5b_mrl
q4b_mrl.posChild = q5c_mrl
q4b_mrl.negChild = F

q5a_mrl.posChild = q6b_mrl
q5a_mrl.negChild = q6c_mrl
q5c_mrl.posChild = resultUnvollstaendigeMaschine
q5c_mrl.negChild = F

q6a_mrl.posChild = q5a_mrl
q6a_mrl.negChild = F

q6b_mrl.posChild = resultMaschine
q6b_mrl.negChild = F


t = Test(q1_rml)