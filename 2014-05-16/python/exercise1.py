'''***********************HOMEWORK3:Esercizio1*********************************'''
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

DRAW = COMP([VIEW,STRUCT,MKPOLS])
master = assemblyDiagramInit([5,5,2])([[0.05,1,.05,1,0.05],[0.05,1,.05,1,0.05],[.05,1]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,1)
VIEW(hpc)
toRemove = [13,17,33,37]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
DRAW(master)



