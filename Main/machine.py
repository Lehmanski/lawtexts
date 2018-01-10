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

		self.html_pages = [('0',P+'allg_grundsaetze.html'),
						   ('1.1.2',P+'1.1.2.html'),
						   ('1.7.3',P+'1.7.3.html'),
						   ('1.7.4',P+'1.7.4.html')]

		self.comments = []


	def printResponse(self):
		sortedPages = sorted(self.html_pages, key=lambda page: page[0])
		html = '<h1>Results</h1> \n'
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

	def addToPages(self, name, path):
		self.html_pages.append((name,P+path))

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
		self.addToPages('z_06','anhang_VI.html')
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



