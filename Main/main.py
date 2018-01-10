import sys, os, webbrowser
from machine import Machine

sys.path.insert(0, os.path.join(os.getcwd(),'QATree/'))
from questions_MRL import *

sys.path.insert(0, os.path.join(os.getcwd(),'Definitions/'))
from definitions import Definitions 

#sys.path.insert(0, os.path.join(os.getcwd(),'productClasses/'))

"""
Create A Machine, called Product for clarity reasons
	Machine will contain all information about:
		Parts
		Directives that apply
"""
Product = Machine()

"""
Load several known definitions
definitions can either be printed as txt, or displayed as html

Idea is, that user can look at definitions and decide if they apply
	#TODO: (machine parts should be able to softly activate definitions)
"""
defs = Definitions()
machineDef_txt, machineDef_html = defs.maschine()



