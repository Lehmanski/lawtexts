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

		self.comments = []

		self.MRL = None
		self.NSR = None


	def printResponse(self):
		sortedPages = sorted(self.html_pages, key=lambda page: page[0])
		if not self.description is None:
			html = self.description
		else:
			html = ''
		html += '<h2>Anzuwendende Maßnamen und Prüfverfahren: </h2>'
		for page in sortedPages:
			t = open(page[1])
			lines = t.readlines()
			for line in lines:
				html += line
			t.close()
			html+='<br>'
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
		self.description += '<br><br><br><br><br><h1>Ergebnisse:</h1> \n'

	def addToDescription(self, title, text):
		self.description += '<h2>{0}</h2>'.format(title)
		self.description += text


	def addToPages(self, name, path):
		if not name in self.html_names:
			self.html_pages.append((name,P+path))

	def setNSR(self,bool,text):
		if bool:
			self.NSR = True
			self.addToDescription('Niederspannungsrichtlinie',
				'Zutreffend aufgrund von: {0}'.format(text))
		elif bool is None:
			self.addToDescription('Niederspannungsrichtlinie',
				'trifft nicht zu')
		else:
			self.NSR = False
			self.addToDescription('Niederspannungsrichtlinie',
				'Aus dem Anwendungsbereich ausgenommen aufgrund von: {0}'.format(text))


	def setMRLApplies(self, bool, text):
		if (not self.MRL) and bool:
			self.__setMRLApplies()
			self.MRL = True
		if bool:
			self.addToDescription('Maschinenrichtlinie',
				'Zutreffend aufgrund von: {0}'.format(text))
		elif bool is None:
			self.addToDescription('Maschinenrichtlinie',
				'trifft nicht zu')
		else:
			self.addToDescription('Maschinenrichtlinie',
				'Aus dem Anwendungsbereich ausgenommen aufgrund von: {0}'.format(text))



	def __setMRLApplies(self):
		self.addToPages('0','allg_grundsaetze.html')
		self.addToPages('1.1.2','1.1.2.html')
		self.addToPages('1.7.3','1.7.3.html')
		self.addToPages('1.7.4','1.7.4.html')
		self.comments.append('MRL trifft zu')


	def setVollst(self):
		self.addToPages('z_02_A','Anhang_II_A.html')
		self.comments.append('vollständig')

	def setUnvollst(self):
		self.addToPages('z_02_B','Anhang_II_B.html')
		self.addToPages('z_06','Anhang_VI.html')
		self.addToPages('z_08B','Anhang_VII_B.html')
		self.comments.append('unvollständig')

	def setNichtIV(self):
		self.addToPages('z_08','Anhang_VIII.html')
		self.addToPages('z_07A','Anhang_VII_A.html')
		self.addToPages('z_06','Anhang_VI.html')
		self.comments.append('Maschine')
		self.comments.append('Nicht im Anhang IV aufgeführt')

	def setIVA(self):
		self.addToPages('z_001','IV_A.html')
		self.addToPages('z_08','Anhang_VIII.html')
		self.addToPages('z_09','Anhang_IX.html')
		self.addToPages('z_10','Anhang_X.html')
		self.comments.append('Im Anhang IV aufgeführt')
		self.comments.append('Nach harmonisierter Norm hergestellt.')

	def setIVB(self):
		self.addToPages('z_001','IV_B.html')
		self.addToPages('z_09','Anhang_IX.html')
		self.addToPages('z_10','Anhang_X.html')
		self.comments.append('Im Anhang IV aufgeführt')
		self.comments.append('Nach harmonisierter Norm hergestellt.')
		self.comments.append('Norm ber[cksichtigt allerdings nicht alle relevanten grundlegenden Sicherheits- und Gesundheitsschutzanforderungen.')


	def setNahrungsmittelMaschine(self):
		self.addToPages('z_01_2.1','Anhang_I_2.1.html')
		self.comments.append('NAHRUNGSMITTELMASCHINEN UND MASCHINEN FÜR KOSMETISCHE ODER PHARMAZEUTISCHE ERZEUGNISSE')

	def setHandMaschine(self):
		self.addToPages('z_01_2.2','Anhang_I_2.2.html')		
		self.comments.append('HANDGEHALTENE UND/ODER HANDGEFÜHRTE TRAGBARE MASCHINEN')

	def setHolzMaschine(self):
		self.addToPages('z_01_2.3','Anhang_I_2.3.html')	
		self.comments.append('MASCHINEN ZUR BEARBEITUNG VON HOLZ UND VON WERKSTOFFEN MIT ÄHNLICHEN PHYSIKALISCHEN EIGENSCHAFTEN')


	def setBeweglich(self):
		self.addToPages('z_01_3','Anhang_I_3.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN ZUR AUSSCHALTUNG DER GEFÄHRDUNGEN, DIE VON DER BEWEGLICHKEIT VON MASCHINEN AUSGEHEN')

	def setLastAufnM(self):
		self.addToPages('z_01_4','Anhang_I_4.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN ZUR AUSSCHALTUNG DER DURCH HEBEVORGÄNGE BEDINGTEN GEFÄHRDUNGEN')

	def setUntertage(self):
		self.addToPages('z_01_5','Anhang_I_5.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN AN MASCHINEN, DIE ZUM EINSATZ UNTER TAGE BESTIMMT SIND')

	def setHebtPersonen(self):
		self.addToPages('z_01_6','Anhang_I_6.html')
		self.comments.append('ZUSÄTZLICHE GRUNDLEGENDE SICHERHEITS- UND GESUNDHEITSSCHUTZANFORDERUNGEN AN MASCHINEN, VON DENEN DURCH DAS HEBEN VON PERSONEN BEDINGTE GEFÄHRDUNGEN AUSGEHEN ')







