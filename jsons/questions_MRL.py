from MRLExceptionList import MRLExceptions
from productClasses_MRL import *
from questions import Question, Result, Test 

done = False



"""
Results
"""
#machine results
resultUnvollstaendigeMaschine = Result('Unvollstaendige Maschine! (daten hier einpflegen) \n',False, UnvollstMaschine())
resultMaschine = Result('Maschine! (daten hier einpflegen) \n\n', False, Maschine())
resultKeinProdukt_a_g = Result('Keine Produkt nach Artikel 1(1)a / 1(1)g \n\n', True)

# intermittent results
resultVerbindung = Result('Verbindungen müssen in Betriebsanleitung spezifiziert werden.\n\n',True)
resultEinbau = Result('Ein- bzw. Anbau muss in Betriebsanleitung genau spezifiziert werden.\n\n',True)
resultSchnittstelle = Result('Einzelne Maschinen bzw. Produkt Schnittstellen beachten!\n\n',True)


resultFalschesWerkzeug = Result('Die Verwendung des Werkzeugs ist nicht vom (Zug-)Maschinen Hersteller vorgesehen. Verwendung unter Verantwortung des Betreibers.\n\n',True)
resultWerkzeug =  Result('Werkzeug; beschrieben in Betriebsanleitung nach MRL Anhang I 1.7.4.2 n)\n\n',False, Werkzeug())

resultAuswAusruestung =  Result('Auswechselbare Ausruestung. (Anweisungen hier rein packen)\n\n',False, AuswAusruestung())
resultKeineAuswAusruestung = Result('Das Produkt ist keine Auswechselbare Ausruestung.\n\n',True)


resultKeinSicherheitsBauteil = Result('Das Produkt ist kein Sicherheitsbauteil.\n\n',True)
resultSicherheitsBauteil = Result('Das Produkt ist ein Sicherheitsbauteil. (Anweisung hier rein packen)\n\n',False, Sicherheitsbauteil())
resultAusgeschlossenesSicherheitsBauteil = Result('Das Produkt ist ein Sicherheitsbauteil, allerdings aus der Richtlinie ausgenommen.\n\n',True)


resultKeinLastenaufnahmeMittel = Result('Kein Produkt nach Artikel 1 (1) d) / e)\n\n', True)
resultLastenaufnahmeMittel = Result('Das Produkt ist ein Lastenaufnahmemittel\n\n', False, Lastenaufnahmemittel())


resultKetten = Result('Es handelt sich bei dem Produkt um Ketten, Seile oder Gurte (Anweisungen hier einfuegen)\n\n', False)

resultGelenkwelle = Result('Das Produkt ist eine Gelenkwelle. (Anweisungen einpflegen)\n\n', False, Gelenkwelle())
resultKeineGelenkwelle = Result('Es handelt sich bei dem Produkt nicht um eine abnehmbare Gelenkwelle\n\n', True)




T = Result('Produkt ist nicht aus der Richtlinie ausgenommen \n', True)
F = Result('MRL trifft nicht zu! \n', False)


"""
MRL_M Exceptions
"""
q1_mrl_E = Question('Handelt es sich bei dem Produkt um eines der Folgenden Erzeugnisse?')
q1_mrl_E.text += MRLExceptions

q1_mrl_E.posChild = F 
q1_mrl_E.negChild = T 


"""
Maschine vs Unvollstaendige Maschine
"""

q1_mrl_M = Question('Besteht das Erzeugniss aus miteinander Verbundenen Teilen?')

q2a_mrl_M = Question('Ist mindestens ein Teil davon beweglich?')

q2b_mrl_M = Question('Teile nur zu Transportzwecken getrennt?')

q3_mrl_M = Question('Kann das Erzeugniss fuer sich genommen die bestimmte Funktion erfuellen?')

q4a_mrl_M = Question('Ist das Produkt mit einem Antriebssystem ausgestattet?')

q4b_mrl_M = Question('Ist das Produkt zum Zusammenbau imt anderen (unvollständigen) Maschinen/Ausrüstungen gedacht?')

q5a_mrl_M = Question('Das Antriebssystem ist die unmittelbar eingesetzte menschliche Kraft?')
q5b_mrl_M = Question('Fuer ein Antriebssystem vorgesehen?')
q5c_mrl_M = Question('Ist das Produkt fast eine Maschine?')

q6a_mrl_M = Question('Ist das Antriebssystem genau spezifiziert?')
q6b_mrl_M = Question('Handelt es sich um ein Produkt fuer Hebevorgaenge?')
q6c_mrl_M = Question('Das Antriebssystem ist die unmittelbar eingesetzte tierische Kraft?')


q7a_mrl_M = Question('Ist eine Verbindung zum Einsatzort, oder zur Energie- bzw. Antriebsquelle vorhanden?')

q8a_mrl_M = Question('Produkt ist zur Anbringung auf einem Fahrzeug / in einem Gebäude gedacht?')


q9a_mrl_M = Question('Produkt ist Einbaufertig für die Anbringung auf einem Fahrzeug / in einem Gebäude?')
q9b_mrl_M = Question('Handelt es sich bei dem Produkt um miteinander verbundene Maschinen/unvollständige Maschinen?')

q10a_mrl_M = Question('Ist eine Funktionale bzw. Steuerungs- order Sicherheitstechnische Verbindung vorhanden?')


q1_mrl_M.posChild = q2a_mrl_M
q1_mrl_M.negChild = q2b_mrl_M

q2a_mrl_M.posChild = q3_mrl_M
q2a_mrl_M.negChild = F

q2b_mrl_M.posChild = F
q2b_mrl_M.negChild = q2a_mrl_M

q3_mrl_M.posChild = q4a_mrl_M
q3_mrl_M.negChild = q4b_mrl_M

q4a_mrl_M.posChild = q5a_mrl_M
q4a_mrl_M.negChild = q5b_mrl_M
q4b_mrl_M.posChild = q5c_mrl_M
q4b_mrl_M.negChild = F

q5a_mrl_M.posChild = q6b_mrl_M
q5a_mrl_M.negChild = q6c_mrl_M
q5b_mrl_M.posChild = q6b_mrl_M
q5b_mrl_M.negChild = F
q5c_mrl_M.posChild = resultUnvollstaendigeMaschine
q5c_mrl_M.negChild = F

q6a_mrl_M.posChild = q5a_mrl_M
q6a_mrl_M.negChild = F
q6b_mrl_M.posChild = resultMaschine
q6b_mrl_M.negChild = resultKeinProdukt_a_g
q6c_mrl_M.posChild = F 
q6c_mrl_M.negChild = q7a_mrl_M

q7a_mrl_M.posChild = q8a_mrl_M
q7a_mrl_M.negChild = resultVerbindung

q8a_mrl_M.posChild = q9a_mrl_M
q8a_mrl_M.negChild = q9b_mrl_M

q9a_mrl_M.posChild = resultEinbau
q9a_mrl_M.negChild = q4b_mrl_M
q9b_mrl_M.posChild = q10a_mrl_M
q9b_mrl_M.negChild = resultMaschine

q10a_mrl_M.posChild = resultMaschine
q10a_mrl_M.negChild = resultSchnittstelle




"""
Auswechselbare Ausreustung
"""
q1_mrl_AA = Question('Ist das Produkt zum Anbringen an eine (Zug-)Maschine durch den Bediener der (Zug-)Maschine gedacht?')

q2_mrl_AA = Question('Ist das Produkt ein einfaches Fertigungsteil (keine beweglichen Teile), das in direkter Berührung mit dem zu bearbeiteten Gegenstand oder Werkstoff steht?')

q3a_mrl_AA = Question('Ist vom Hersteller der Maschine als geeignetes Werkzeug beschrieben?')
q3b_mrl_AA = Question('Produkt Ändert / Erweitert die Funktion der Maschine?')

q1_mrl_AA.posChild = q2_mrl_AA
q1_mrl_AA.negChild = resultKeineAuswAusruestung

q2_mrl_AA.posChild = q3a_mrl_AA
q2_mrl_AA.negChild = q3b_mrl_AA

q3a_mrl_AA.posChild = resultWerkzeug
q3a_mrl_AA.negChild = resultFalschesWerkzeug
q3b_mrl_AA.posChild = resultAuswAusruestung


"""
Sicherheitsbauteil
"""
q1_mrl_SB = Question('Dient zur Gewährleistung einer Sicherheitsfunktion?')

q2_mrl_SB = Question('Wird das Produkt gesondert in Verkehr gebracht?')

q3_mrl_SB = Question('Ausfall des Bauteils gefährdet die Sicherheit von Personen?')

q4_mrl_SB = Question('Für das Funktionieren der Maschine Notwendig?')

q5a_mrl_SB = Question('Kann durch ein - für die reine Funktion der Maschine - übliches Bauteil ersetzt werden?')

q5b_mrl_SB = Question('Wird vom Hersteller der Maschine als Ersatzteil für identisches Produkt verkauft?')


q1_mrl_SB.posChild = q2_mrl_SB
q1_mrl_SB.negChild = resultKeinSicherheitsBauteil

q2_mrl_SB.posChild = q3_mrl_SB
q2_mrl_SB.negChild = resultKeinSicherheitsBauteil

q3_mrl_SB.posChild = q4_mrl_SB
q3_mrl_SB.negChild = resultKeinSicherheitsBauteil

q4_mrl_SB.posChild = q5a_mrl_SB
q4_mrl_SB.negChild = q5b_mrl_SB

q5a_mrl_SB.posChild = q5b_mrl_SB
q5a_mrl_SB.negChild = resultKeinSicherheitsBauteil
q5b_mrl_SB.posChild = resultAusgeschlossenesSicherheitsBauteil
q5b_mrl_SB.negChild = resultSicherheitsBauteil



"""
Lasten 
"""
q1_mrl_L = Question('Dient zum Ergreifen einer Last?')

q2_mrl_L = Question('Ist Bestandteil des Hebezeugs / Lastaufnahmemittels?')

q3a_mrl_L = Question('Ist Kette, Seil oder Gurt?')
q3b_mrl_L = Question('Ist dazu bestimmt, zwischen Last und Maschine angebracht zu werden?')

q4_mrl_L = Question('Ist dazu bestimmt, an der Last angebracht zu werden?')

q5_mrl_L = Question('Dazu bestimmt, Bestandteil der Last zu werden?')

q6_mrl_L = Question('Wird gesondert in Verkehr gebracht?')


q1_mrl_L.posChild = q2_mrl_L
q1_mrl_L.negChild = resultKeinLastenaufnahmeMittel

q2_mrl_L.posChild = q3a_mrl_L
q2_mrl_L.negChild = q3b_mrl_L

q3a_mrl_L.posChild = resultKetten
q3a_mrl_L.negChild = resultKeinLastenaufnahmeMittel

q3b_mrl_L.posChild = resultLastenaufnahmeMittel
q3b_mrl_L.negChild = q4_mrl_L

q4_mrl_L.posChild = resultLastenaufnahmeMittel
q4_mrl_L.negChild = q5_mrl_L

q5_mrl_L.posChild = resultKeinLastenaufnahmeMittel
q5_mrl_L.negChild = q6_mrl_L

q6_mrl_L.posChild = resultLastenaufnahmeMittel
q6_mrl_L.negChild = resultKeinLastenaufnahmeMittel



"""
Gelenkwellen 
"""

q1_mrl_GW = Question('Zur Kraftbertragung zwischen einer Antriebs- oder Zugmaschine und einer anderen Maschine gedacht?')

q2_mrl_GW = Question('Produkt verbindet die ersten Festlager beider Maschinen?')

q1_mrl_GW.posChild = q2_mrl_GW
q1_mrl_GW.negChild = resultKeineGelenkwelle

q2_mrl_GW.posChild = resultGelenkwelle
q1_mrl_GW.negChild = resultKeineGelenkwelle


t = Test()
testResult = t.start(q1_mrl_E)

if testResult.bool:
	testResult = t.start(q1_mrl_M)

if testResult.bool:
	testResult = t.start(q1_mrl_AA)

if testResult.bool:
	testResult = t.start(q1_mrl_SB)

if testResult.bool:
	testResult = t.start(q1_mrl_L)

if testResult.bool:
	testResult = t.start(q1_mrl_GW)