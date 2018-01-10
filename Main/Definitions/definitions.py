import os
P = os.path.join(os.getcwd(),'Definitions/html_resources/')


class Definitions():
	def __init__(self):
		pass 

	def maschine(self):
		txt = """
		„Maschine“

		— eine mit einem anderen Antriebssystem als der unmittelbar eingesetzten menschlichen oder tierischen Kraft ausgestattete oder dafür vorgesehene Gesamtheit miteinander verbundener Teile oder Vorrichtungen, von denen mindestens eines bzw. eine beweglich ist und die für eine bestimmte Anwendung zusammengefügt sind;
		— eine Gesamtheit im Sinne des ersten Gedankenstrichs, der lediglich die Teile fehlen, die sie mit ihrem Einsatzort oder mit ihren Energie- und Antriebsquellen verbinden;
		— eine einbaufertige Gesamtheit im Sinne des ersten und zweiten Gedankenstrichs, die erst nach Anbringung auf einem Beförderungsmittel oder Installation in einem Gebäude oder Bauwerk funktionsfähig ist;
		— eine Gesamtheit von Maschinen im Sinne des ersten, zweiten und dritten Gedankenstrichs oder von unvollständigen Maschinen im Sinne des Buchstabens g, die, damit sie zusammenwirken, so angeordnet sind und betätigt werden, dass sie als Gesamtheit funktionieren;
		— eine Gesamtheit miteinander verbundener Teile oder Vorrichtungen, von denen mindestens eines bzw. eine beweglich ist und die für Hebevorgänge zusammengefügt sind und deren einzige Antriebsquelle die unmittelbar eingesetzte menschliche Kraft ist;
		"""
		html_source = P+'maschine.html'
		return txt, html_source

	def ausweAusr(self):
		txt="""
		„auswechselbare Ausrüstung“ eine Vorrichtung, die der Bediener einer Maschine oder Zugmaschine nach deren Inbetriebnahme selbst an ihr anbringt, um ihre Funktion zu ändern oder zu erweitern, sofern diese Ausrüstung kein Werkzeug ist;
		"""
		html_source = P+'auswAusr'
		return txt, html_source

	def sichBaut(self):
		txt="""	„Sicherheitsbauteil“ ein Bauteil,
			— das zur Gewährleistung einer Sicherheitsfunktion dient,
			— gesondert in Verkehr gebracht wird,
			— dessen Ausfall und/oder Fehlfunktion die Sicherheit von Personen gefährdet und
			— das für das Funktionieren der Maschine nicht erforderlich ist oder durch für das Funktionieren der Maschine übliche Bauteile ersetzt werden kann.
		Eine nicht erschöpfende Liste von Sicherheitsbauteilen findet sich in Anhang V, der gemäß Artikel 8 Absatz 1 Buchstabe a aktualisiert werden kann;
		"""
		html_source = P+'sichBaut'
		return txt, html_source