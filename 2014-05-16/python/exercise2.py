'''***********************HOMEWORK3:Esercizio2*********************************'''
"""importo di librerie"""
from pyplasm import *
import os,sys
sys.path.insert(0, '/Users/baljinderjit/Desktop/GraficaComputazionaleProgetti/lar-cc/lib/py')
from larcc import *
from sysml import *
from exercise1 import *
'''***********************************************************'''
#VIEW(STRUCT(MKPOLS(master)))

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
master = assemblyDiagramInit([5,5,9])([[.2,4,.2,4,.2],[0.2,4,0.2,2,.2],[0.5,4,.2,4,.2,4,.2,4,.2]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)


toMerge = 55
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  
VIEW(STRUCT([hpc,cell]))     

# 


master = diagram2cell(diagram,master,toMerge)   
VIEW(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

