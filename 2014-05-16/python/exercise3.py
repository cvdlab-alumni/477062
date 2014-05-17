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
'''***********************************************************'''
DRAW = COMP([VIEW,STRUCT,MKPOLS])
master = assemblyDiagramInit([5,5,2])([[.2,4,.2,4,.2],[0.2,4,0.2,2,.2],[0.5,4]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
########################################################################################
toRemove = [13,17,33]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#lavoro per fare il muro tra cucina e bagno
toMerge = 34
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la finestra
diagram = assemblyDiagramInit([3,1,1])([[1,.1,3],[.2],[1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e bagno ed elimino i volumi del bagno e cucina
toRemove = [25,46,48]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#finito tutte le pareti interne ed esterne
#visualizzo tutte le celle per individuare le celle da eliminare
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#prendo la parete frontale indentificata dalla cella  per fare la finestra1
toMerge = 11
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la finestra1
diagram = assemblyDiagramInit([3,1,3])([[1,1,1],[.2],[2.5,3,3]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#visualizzo tutte le celle per individuare la finestra da eliminare come cella
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la finestra1
toRemove = [49]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#faccio al porta di ingresso identificata dalla cella
toMerge = 27
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensione le misure della porta nella celle
diagram = assemblyDiagramInit([3,1,2])([[.5,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la cella  cosi ottengo la porta principale
toRemove = [54]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#visulalizzo celle per fare la seconda finestra
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#seleziono la cella  per fare la finestra2
toMerge = 40
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono le misure della finestra2 dalla cella
diagram = assemblyDiagramInit([1,3,3])([[.2],[1,.5,.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la cella della finestra2
toRemove = [60]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
######fine porte e finestrepareti esterne############
'''-------------------inizio porte interne---------------'''
#visulizzo le celle per individuare la cella su cui costruire la porta interna
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#-----------parete tra salone e camera---------------
#seleziono la cella per fare la porta interna tra salone e camera
toMerge = 20
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[0,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [67]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#-----------parete tra salone e bagno---------------
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toMerge = 28
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,2])([[.6,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la cella per fare le porta tra salone e bagno
toRemove = [72]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#-----------parete tra salone e cucina---------------
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#rimuovo la parete per fare la porta della cucina
toRemove = [70]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)

