import webbrowser, os 

P = os.path.join(os.getcwd(),'html_resources/snippets/')

htmlOutPath = os.path.abspath('temp.html')
url = 'file://' + htmlOutPath

class Machine():
	'''
	HTML:
		Anhang I
			Allg. Grundsaetze
			1.1.2
			1.7.3
			1.7.4
	'''
	def __init__(self):
		self.parts = {}

		self.html_pages = []
		self.html_names = []

		self.description = None
		self.procedures = None 
		self.applicability = None

		self.HTML_description = {}
		self.HTML_Results = {'MRL':[],'NSR':[]}
		self.HTML_Procedures = {} 

		self.comments = []

		self.MRL = None
		self.NSR = None



	def addToProcedures(self, directiveName, idx, htmlFile):
		if not directiveName in self.HTML_Procedures:
			self.HTML_Procedures[directiveName] = []
		self.HTML_Procedures[directiveName].append((idx, htmlFile))

	def compileProcedures(self):
		self.procedures = '<h1>Anzuwendende Verfahren</h1>'
		for directiveName in self.HTML_Procedures:
			self.procedures += '<h2>{0}</h2>'.format(directiveName)
			sortedProcedures = sorted(
					self.HTML_Procedures[directiveName], 
					key=lambda page: page[0])
			for procedure in sortedProcedures:
				with open(P+procedure[1]) as f:
					lines = ' '.join(f.readlines())
					self.procedures += lines
		self.procedures += '<br><br><br>'

	def stateUpdate(self, dN, bool):
		if dN == 'MRL':
			self.MRL = bool
		if dN == 'NSR':
			self.NSR = bool



	def updateComponentDirectiveRelationList(self, directiveName, component, bool, type):
		if not directiveName in self.HTML_Results:
			self.HTML_Results[directiveName] = []
		self.HTML_Results[directiveName].append((component, bool, type))

	def compileComponentDirectiveRelationList(self):
		self.applicability = '<h1>Anwendbarkeit auf Richtlinien</h1>'
		for directiveName in self.HTML_Results:
			self.applicability += '<h2>{0}</h2>'.format(directiveName)
			# check if there is a major reason to exclude directive
			for rel in self.HTML_Results[directiveName]:
				if rel[-1]=='MAJOR':
					self.stateUpdate(directiveName, rel[1])
				if rel[-1]=='MAJOR' and rel[1]==False:
					self.applicability += 'Nicht anwendbar: {0}'.format(rel[0])
					break 
				if rel[1]:
					self.applicability += 'Anwendbar: {0}'.format(rel[0])
		self.applicability += '<br><br><br>'



	def printResponse(self):
		html = ''
		html += self.description
		html += self.applicability 
		html += self.procedures 
		# write temp file
		with open(htmlOutPath, 'w') as f:
			f.write(html)
		webbrowser.open(url)

	def htmlDescriptionLine(self,items):
		return '<strong>'+':'.join(items)+'</strong><br>'

	def htmlDescriptionList(self,title,items):
		html = '<h3>{0}</h3><ul>'.format(title)
		for i in items:
			html += '<li>{0}</li>'.format(i)
		html +='</ul>'
		return html

	def htmlDescriptionDict(self,title,items):
		return self.htmlDescriptionList(title,items)


	def addDescription(self):
		self.description = '<h1>Beschreibung der Maschine:</h1>'
		for item in self.json.items():
			if type(item[1]) is dict:
				self.description += self.htmlDescriptionList(item[0],item[1:][0])
			elif type(item[1]) is list:
				self.description += self.htmlDescriptionDict(item[0],item[1:][0])
			else:
				self.description += self.htmlDescriptionLine(item)

	def addToDescription(self, title, text):
		self.description += '<h2>{0}</h2>'.format(title)
		self.description += text


	def addToPages(self, name, path):
		if not name in self.html_names:
			self.html_pages.append((name,P+path))

	def setNSR(self, component, bool, type='MAJOR'):
		self.NSR = bool
		self.updateComponentDirectiveRelationList('NSR', component, bool, type)
		

	def setMRL(self,component, bool, type='MAJOR'):
		self.NSR = bool
		self.updateComponentDirectiveRelationList('MRL', component, bool, type)

	def setMRLApplies(self):
		self.addToProcedures('MRL','0','allg_grundsaetze.html')
		self.addToProcedures('MRL','1.1.2','1.1.2.html')
		self.addToProcedures('MRL','1.7.3','1.7.3.html')
		self.addToProcedures('MRL','1.7.4','1.7.4.html')
		self.comments.append('MRL trifft zu')

	def setVollst(self):
		self.addToProcedures('MRL','z_02_A','Anhang_II_A.html')
		self.comments.append('vollständig')

	def setUnvollst(self):
		self.addToProcedures('MRL','z_02_B','Anhang_II_B.html')
		self.addToProcedures('MRL','z_06','Anhang_VI.html')
		self.addToProcedures('MRL','z_08B','Anhang_VII_B.html')
		self.comments.append('unvollständig')

	def setNichtIV(self):
		self.addToProcedures('MRL','z_08','Anhang_VIII.html')
		self.addToProcedures('MRL','z_07A','Anhang_VII_A.html')
		self.addToProcedures('MRL','z_06','Anhang_VI.html')
		self.comments.append('Maschine')
		self.comments.append('Nicht im Anhang IV aufgeführt')

	def setIVA(self):
		self.addToProcedures('MRL','z_001','IV_A.html')
		self.addToProcedures('MRL','z_08','Anhang_VIII.html')
		self.addToProcedures('MRL','z_09','Anhang_IX.html')
		self.addToProcedures('MRL','z_10','Anhang_X.html')
		self.comments.append('Im Anhang IV aufgeführt')
		self.comments.append('Nach harmonisierter Norm hergestellt.')

	def setIVB(self):
		self.addToProcedures('MRL','z_001','IV_B.html')
		self.addToProcedures('MRL','z_09','Anhang_IX.html')
		self.addToProcedures('MRL','z_10','Anhang_X.html')
		self.comments.append('Im Anhang IV aufgeführt')
		self.comments.append('Nach harmonisierter Norm hergestellt.')
		self.comments.append('Norm ber[cksichtigt allerdings nicht alle relevanten grundlegenden Sicherheits- und Gesundheitsschutzanforderungen.')


	def setNahrungsmittelMaschine(self):
		self.addToProcedures('MRL','z_01_2.1','Anhang_I_2.1.html')
		self.comments.append('NAHRUNGSMITTELMASCHINEN UND MASCHINEN FÜR KOSMETISCHE ODER PHARMAZEUTISCHE ERZEUGNISSE')

	def setHandMaschine(self):
		self.addToProcedures('MRL','z_01_2.2','Anhang_I_2.2.html')		
		self.comments.append('HANDGEHALTENE UND/ODER HANDGEFÜHRTE TRAGBARE MASCHINEN')

	def setHolzMaschine(self):
		self.addToProcedures('MRL','z_01_2.3','Anhang_I_2.3.html')	
		self.comments.append('MASCHINEN ZUR BEARBEITUNG VON HOLZ UND VON WERKSTOFFEN MIT ÄHNLICHEN PHYSIKALISCHEN EIGENSCHAFTEN')


	def setBeweglich(self):
		self.addToProcedures('MRL','z_01_3','Anhang_I_3.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN ZUR AUSSCHALTUNG DER GEFÄHRDUNGEN, DIE VON DER BEWEGLICHKEIT VON MASCHINEN AUSGEHEN')

	def setLastAufnM(self):
		self.addToProcedures('MRL','z_01_4','Anhang_I_4.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN ZUR AUSSCHALTUNG DER DURCH HEBEVORGÄNGE BEDINGTEN GEFÄHRDUNGEN')

	def setUntertage(self):
		self.addToProcedures('MRL','z_01_5','Anhang_I_5.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN AN MASCHINEN, DIE ZUM EINSATZ UNTER TAGE BESTIMMT SIND')

	def setHebtPersonen(self):
		self.addToProcedures('MRL','z_01_6','Anhang_I_6.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN AN MASCHINEN, VON DENEN DURCH DAS HEBEN VON PERSONEN BEDINGTE GEFÄHRDUNGEN AUSGEHEN ')







