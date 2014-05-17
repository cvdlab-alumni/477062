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
master = assemblyDiagramInit([5,5,3])([[.2,4,.2,4,.2],[0.2,4,0.2,2.,.2],[0.5,4,0.5]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
#elimino il volume ai volumi in particolare lascio solo pareti
########################################
toRemove = [19,49,25,55]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)
#visualizzo tutte le celle per individuare le celle da eliminare
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#prendo la parete frontale indentificata dalla cella 16 per fare la finestra
toMerge = 16
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella 16 la finestra
diagram = assemblyDiagramInit([3,1,3])([[1,1,1],[.2],[2.5,3,3]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#visualizzo tutte le celle per individuare la finestra da eliminare come cella
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la finestra
toRemove = [74]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#faccio al porta di ingresso identificata dalla cella 43
toMerge = 43
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensione le misure della finestra nella celle 43
diagram = assemblyDiagramInit([3,1,2])([[.5,1,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la cella 79 ce ottengo la porta principale
toRemove = [79]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#visulalizzo celle per fare la seconda finestra
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#seleziono la cella 64 per fare la finestra
toMerge = 64
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
# VIEW(STRUCT([hpc,cell]))
#dimensiono le misure della mistra dalla cella 64
diagram = assemblyDiagramInit([1,3,3])([[.2],[1,.5,.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la cella della finestra
toRemove = [85]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
######fine porte e finestrepareti esterne############
'''-------------------inizio porte interne---------------'''
#visulizzo le celle per individuare la cella su cui costruire la porta interna
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 31
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[0,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [92]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)


