import sys, os, webbrowser
from pprint import pprint as print 
from machine import Machine

sys.path.insert(0, os.path.join(os.getcwd(),'QATree/'))
from questions_MRL import *

sys.path.insert(0, os.path.join(os.getcwd(),'Definitions/'))
from definitions import Definitions 

sys.path.insert(0, os.path.join(os.getcwd(),'saveLoad/'))
from configurator import Configurator
from jsonParser import Parser

sys.path.insert(0, os.path.join(os.getcwd(),'logic/'))
from logicUnit import LOGIC

#sys.path.insert(0, os.path.join(os.getcwd(),'productClasses/'))

"""
Create A Machine, called Product for clarity reasons
	Machine will contain all information about:
		Parts
		Directives that apply
"""
Product = Machine()
Logic = LOGIC(Product)

"""
Load several known definitions
definitions can either be printed as txt, or displayed as html

Idea is, that user can look at definitions and decide if they apply
	#TODO: (machine parts should be able to softly activate definitions)
"""
defs = Definitions()

machineDef_txt, machineDef_html = defs.maschine()
ausweAusr_txt, ausweAusr_html = defs.ausweAusr()
sichBaut_txt, sichBaut_html = defs.sichBaut()
lastMit_txt, lastMit_html = defs.lastMit()
ketten_txt, ketten_html = defs.ketten()
abnGel_txt, abnGel_html = defs.abnGel()
unvMasch_txt, unvMasch_html = defs.unvMasch()




"""
load json
"""
jsonPath = 'json/_exampleMachine.json'
parser = Parser()
data = parser.parse(jsonPath)

"""
add data to Product
"""
configurator = Configurator(Product)
configurator.configure(data)

# generate html header
Product.addDescription()


# test MRL
Logic.checkMRL()
Logic.checkNSR()


# Print response
Product.printResponse()