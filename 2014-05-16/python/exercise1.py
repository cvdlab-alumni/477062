'''----------------------HW3:esercizio1------------------'''
'''----------------------importo di librerie----------------------'''
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
coloreTronco = rgb([102,51,0])
'''***********************************************************'''

Dom1D = INTERVALS(1)(10)
Bezier = BEZIER(S1)
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

def generaAlbero(coordinate):
	x,y,z = coordinate
	def generaAlbero0(dimesioni):
		r,h = dimesioni
		tronco = larCylinder(r,h)([32,1])
		albero = larSphere(r*4)()
		tronco = COLOR(coloreTronco)(STRUCT(MKPOLS(tronco)))
		albero = COLOR(coloreGiardino)(STRUCT(MKPOLS(albero)))
		return T([1,2,3])([x,y,z])(STRUCT([tronco,T(3)(h+r)(albero)]))
	return generaAlbero0

def generaNuvola():
	Nuv1 = [[1.62, 4], [1.75, 4.66], [2.01, 4.54], [2.32, 4.67]]
	Nuv1 = MAP(Bezier(Nuv1))(Dom1D)
	Nuv2 = [[1.62, 4], [0.05, 4.08], [0.43, 2.14], [2.16, 2.42]]
	Nuv2 = MAP(Bezier(Nuv2))(Dom1D)
	Nuv3 = [[2.85, 2.12], [2.57, 2.01], [2.22, 2.2], [2.16, 2.42]]
	Nuv3 = MAP(Bezier(Nuv3))(Dom1D)
	Nuv4 = [[2.85, 2.12], [2.81, 1.83], [4.36, 1.39], [4.76, 2.49]]
	Nuv4 = MAP(Bezier(Nuv4))(Dom1D)
	Nuv5 = [[5.51, 2.83], [5.52, 2.44], [5.14, 2.15], [4.76, 2.49]]
	Nuv5 = MAP(Bezier(Nuv5))(Dom1D)
	Nuv6 = [[5.51, 2.83], [6.84, 2.86], [6.6, 4.01], [5.67, 4.19]]
	Nuv6 = MAP(Bezier(Nuv6))(Dom1D)
	Nuv7 = [[4.31, 4.79], [5.12, 5.87], [6.1, 4.75], [5.67, 4.19]]
	Nuv7 = MAP(Bezier(Nuv7))(Dom1D)
	Nuv8 = [[4.31, 4.79], [4.42, 4.99], [3.68, 5.2], [3.67, 4.8]]
	Nuv8 = MAP(Bezier(Nuv8))(Dom1D)
	Nuv9 = [[2.32, 4.67], [2.65, 5.42], [3.24, 5.63], [3.67, 4.8]]
	Nuv9 = MAP(Bezier(Nuv9))(Dom1D)
	nuovola = STRUCT([Nuv1,Nuv2,Nuv3,Nuv4,Nuv5,Nuv6,Nuv7,Nuv8,Nuv9])
	nuovola = SOLIDIFY(nuovola)
	return MATERIAL([1,1,1,0, 0,0,0,0.2, 0,0,0,0, 0,0,0,0, 50])(nuovola)
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
VIEW(scheletroModello(master))
VIEW(visualizzaModello(master))