'''***********************HOMEWORK3:Esercizio3*********************************'''
"""importo di librerie"""
from pyplasm import *
from scipy import *
import os,sys
sys.path.insert(0, '/Users/baljinderjit/Desktop/GraficaComputazionaleProgetti/lar-cc/lib/py')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *
'''***********************************************************'''
from larcc import *
DRAW = COMP([VIEW,STRUCT,MKPOLS])
def mergingNumberingElimination(diagramHole,diagram,toMerge,toRemove):
	diagramHole = diagramHole[0],[cell for k,cell in enumerate(diagramHole[1]) if not (k in toRemove)]
	toMerge = list(sort(toMerge))
	iteratore = range(len(toMerge))
	for i in iteratore:
		elementMerge = toMerge[i]-i
		diagram = diagram2cell(diagramHole,diagram,elementMerge)
	return diagram



