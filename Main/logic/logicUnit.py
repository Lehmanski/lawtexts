import json

purposesPath = 'json/purposes.json'
sitesPath = 'json/sites.json'


NSR_ac_high = 1000
NSR_ac_low  = 50

NSR_dc_high = 1000
NSR_dc_low  = 50

class LOGIC():
	def __init__(self, Product):
		self.Product = Product
		self.loadPurposes()
		self.loadSites()

	def loadPurposes(self):
		with open(purposesPath) as f:
			self.purposes = json.load(f)

	def loadSites(self):
		with open(sitesPath) as f:
			self.sites = json.load(f)

	def checkMRL(self):
		# check verwendungszwecke
		for purpose in self.Product.json['Verwendungszwecke']:
			if purpose in self.purposes:
				if 'MRL' in self.purposes[purpose]:
					positive_entry = self.purposes[purpose]['MRL']['+']
				else:
					continue
				# activate MRL, if not already active
				if not self.Product.MRL:
					self.Product.setMRLApplies(True, purpose)
				for p in positive_entry:
					#switch case
					if p == 'Anhang_I_2.1':
						self.Product.setNahrungsmittelMaschine()
					elif p == 'Anhang_I_2.2':
						self.Product.setHandMaschine()
					elif p == 'Anhang_I_2.3':
						self.Product.setHolzMaschine()
					elif p == 'Anhang_I_3':
						self.Product.setBeweglich()
					elif p == 'Anhang_I_4':
						self.Product.setLastAufnM()
					elif p == 'Anhang_I_5':
						self.Product.setUntertage()
					elif p == 'Anhang_I_6':
						self.Product.setHebtPersonen()
		# for every site the machine is going to be used at
		for site in self.Product.json['Verwendungsorte']:
			# check if site is known
			if site in self.sites:
				# if site effects MRL
				if 'MRL' in self.sites[site]:
					positive_entry = self.sites[site]['MRL']['+']
					# go through positive examples (activating directive)
					for s in positive_entry:
						if s == 'Anhang_I_5':
							self.Product.setUntertage()


	def checkNSR(self):
		"""
		Check if purpose or site exclude product from NSR
		"""
		# check verwendungszwecke
		for purpose in self.Product.json['Verwendungszwecke']:
			if purpose in self.purposes:
				if 'NSR' in self.purposes[purpose]:
					negative_entry = self.purposes[purpose]['NSR']['-']
				else:
					continue
				if 'NSR' in negative_entry:
					text = '<br> <strong>Verwendungszweck</strong>: {0}'.format(purpose)
					self.Product.setNSR(False, text)
					return

		for purpose in self.Product.json['Verwendungsorte']:
			if purpose in self.purposes:
				if 'NSR' in self.purposes[purpose]:
					negative_entry = self.purposes[purpose]['NSR']['-']
				else:
					continue
				if 'NSR' in negative_entry:
					text = '<br> <strong>Verwendungsort</strong>: {0}'.format(purpose)
					self.Product.setNSR(False, text)
					return 

		"""
		Check if component features activate NSR
		(Basically if anything has voltage in certain range)
		"""
		for component in self.Product.json['Komponenten'].items():
			for feature in component[1].keys():
				if feature == 'Spannung':
					val = component[1][feature]
					if list(val.keys())[0] == 'Volt AC':
						x = float(list(val.values())[0])
						if NSR_ac_low < x < NSR_ac_high:
							if not self.Product.NSR:
								self.Product.setNSRApllies()
							text = '<br> <strong>Komponente </strong>: {0}'.format(component)
							self.Product.setNSR(True,text)
					if list(val.keys())[0] == 'Volt DC':
						x = float(list(val.values())[0])
						if NSR_dc_low < x < NSR_dc_high:
							if not self.Product.NSR:
								self.Product.setNSRApllies()
							text = '<br> <strong>Komponente </strong>: {0}'.format(component)
							self.Product.setNSR(True,text)

		if not self.Product.NSR:
			self.Product.setNSR(None,None)






