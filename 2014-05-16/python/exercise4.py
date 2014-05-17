'''***********************HOMEWORK3:Esercizio4*********************************'''
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
def diagram2cell(diagram,master,cell):
	mat = diagram2cellMatrix(diagram)(master,cell)
	diagram =larApply(mat)(diagram)
	V1,CV1 = master
	CV1 = [x for y,x in enumerate(CV1) if y != cell]
	V,CV1,CV2,n12 = vertexSieve((V1,CV1),diagram)
	CV = CV1+CV2
	master = V, CV
	return master
'''***********************************************************'''
