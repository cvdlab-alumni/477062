#Homework3
#Baljinder jit	477062
from pyplasm import *
import os,sys
sys.path.insert(0, '/Users/baljinderjit/Desktop/GraficaComputazionaleProgetti/lar-cc/lib/py')
from larcc import *
from sysml import *
'''-----------------definizioni funzioni------------------'''
'''----colori------'''
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]
'''***********************************************************'''
colorePalazzo = rgb([222,212,185])
coloreRampa = rgb([160,160,160])
coloreAsseMacchina = rgb([121,121,121])
coloreRuoteMacchina = rgb([71,71,71])
coloreMacchina = rgb([49,56,148])
coloreGiardino = rgb([5,138,0])
coloreBalcone = rgb([5,138,0])
colorePaloScale = rgb([135, 131, 131])
coloreScale = rgb([240, 208, 180])
coloreTronco = rgb([102,51,0])
'''***********************************************************'''
def eliminaCelle(toRemove, diagram):
	V,CV = diagram
	return V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

def visualizzaModello(model):
	return STRUCT(MKPOLS(model))

def scheletroModello(master):
	V,CV = master
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	return  cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#master = eliminaCelle((toRemove, diagram))
def eliminaCelle(toRemove, diagram):
	V,CV = diagram
	return V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

def visualizzaCella(toMerge, master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
	return STRUCT([hpc,cell])

'''-------------------------------------------------------'''
master = assemblyDiagramInit([3,5,2])([[.2,10,.2],[0.2,5,0.2,3,.2],[0.2,4]])
V,CV = master
#creo muro tra soggiorno e camera
diagram = assemblyDiagramInit([3,1,1])([[4,.2,5],[1],[1]])
master = diagram2cell(diagram,master,13)
#creo muro tra cucina e bagno
diagram = assemblyDiagramInit([3,1,1])([[6.2,.2,4],[1],[1]])
master = diagram2cell(diagram,master,16)
#finestra della camera
diagram = assemblyDiagramInit([4,1,3])([[.5,0.6,1.5,1],[1],[2,2,1]])
master = diagram2cell(diagram,master,11)
toRemove = [37]
master = eliminaCelle(toRemove,master)
#porta soggiorno: ingresso
diagram = assemblyDiagramInit([3,1,2])([[2.5,2,.5],[1],[2,1]])
master = diagram2cell(diagram,master,39)
diagram = assemblyDiagramInit([3,1,1])([[2.5,2,.5],[1],[1]])
master = diagram2cell(diagram,master,38)
toRemove = [44,49]
master = eliminaCelle(toRemove,master)
#finestra soggiorno
diagram = assemblyDiagramInit([3,1,2])([[.5,1,.5],[1],[2,1]])
master = diagram2cell(diagram,master,39)
diagram = assemblyDiagramInit([3,1,2])([[.5,1,.5],[1],[3,.5]])
master = diagram2cell(diagram,master,39)
toRemove = [50,55]
master = eliminaCelle(toRemove,master)
#finestra bagno
diagram = assemblyDiagramInit([1,3,3])([[1],[1,1,.5],[1,2,.5]])
master = diagram2cell(diagram,master,24)
toRemove = [60]
master = eliminaCelle(toRemove,master)
#porta soggiorno camera
diagram = assemblyDiagramInit([1,3,2])([[1],[2,1,.5],[2,1]])
master = diagram2cell(diagram,master,27)
toRemove = [65]
master = eliminaCelle(toRemove,master)
#porta bagno
diagram = assemblyDiagramInit([3,1,2])([[2.5,.5,1],[1],[2,1]])
master = diagram2cell(diagram,master,13)
toRemove = [69]
master = eliminaCelle(toRemove,master)
#raffinatura in cucina
diagram = assemblyDiagramInit([4,2,2])([[1.5,1,2,3],[.5,1],[2,1]])
master = diagram2cell(diagram,master,27)
toRemove = [77,78,81,82,83,84,85,86]
master = eliminaCelle(toRemove,master)
#porta cucina
diagram = assemblyDiagramInit([3,2,1])([[7.1,1.5,.5],[.5,1],[1]])
master = diagram2cell(diagram,master,66)
toRemove = [80,81]
master = eliminaCelle(toRemove,master)
#elimino volume stanze
toRemove = [25,26,28]
master = eliminaCelle(toRemove,master)
#raffinatura in cucina
toRemove = [69,70]
master = eliminaCelle(toRemove,master)


#VIEW(scheletroModello(master))
#VIEW(visualizzaModello(master))