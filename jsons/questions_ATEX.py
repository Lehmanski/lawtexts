from productClasses_ATEX import *
from ATEXExceptionList import ATEXExceptions
from questions import Question, Result, Test 


"""
Results
"""
F = Result('ATEX trifft nicht zu', False)


"""
Anwendbarkeit ATEX
"""

q1_atex = Question('Handelt es sich bei dem Produkt um eines der Folgenden Erzeugnisse?')
q1_atex.text += ATEXExceptions


q2_atex = Question('Handelt es sich um ein Gerät zur Verwendung im medizinischen Bereich?')

q1_atex.posChild = F 
q1_atex.negChild = q2_atex
