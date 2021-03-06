import sys, os, webbrowser
from pprint import pprint as print 
from _machine import Machine

sys.path.insert(0, os.path.join(os.getcwd(),'QATree/'))
from questions_MRL import *

sys.path.insert(0, os.path.join(os.getcwd(),'Definitions/'))
from definitions import Definitions 

sys.path.insert(0, os.path.join(os.getcwd(),'saveLoad/'))
from configurator import Configurator
from jsonParser import Parser

sys.path.insert(0, os.path.join(os.getcwd(),'logic/'))
from _logicUnit import LOGIC

from _printer import Printer


#TODO: anwendbar auf/von 
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
load json
"""
jsonPath = 'json/__exampleMachine.json'
parser = Parser()
data = parser.parse(jsonPath)

"""
add data to Product
"""
configurator = Configurator(Product)
configurator.configure(data)

Logic.checkMachineFirstLevel()
Logic.checkMachineComponents()


Logic.finalize()
print(Logic.HTML_Results)


