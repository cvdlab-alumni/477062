from exercise1 import *
Dom1D = INTERVALS(1)(24)
Bezier = BEZIER(S1)
'''----colori------'''
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]
'''***********************************************************'''
colorePalazzo = rgb([222,212,185])
'''***********************************************************'''
appartamento1 = master
master = assemblyDiagramInit([8,3,9])([[2.5,6,0.2,3,.2,9,.5,4],[4,8,8],[.5,4,.2,4,.2,4,.2,4,3]])
#elimio celle inutili
toRemove = [1,28,55,82,109,136,192,193,194,195,196,197,203,204,205,206,211,212,213,214,215]
master = eliminaCelle(toRemove,master)
toRemove = [1,2,3,4,5,6,7,79,80,27,28,29,131,132,133,53,54,105,106]
master = eliminaCelle(toRemove,master)
toRemove = [2,11,12,13,14,15,16,17,18,86,87,88,89,140,67,141,43,91,175,151,152,153,154,142,143,144,145]
master = eliminaCelle(toRemove,master)
toRemove = [131,132,133,134,135,136]
master = eliminaCelle(toRemove,master)
#taglio i balconi west discesa-1
diagram = assemblyDiagramInit([1,3,2])([[1],[.1,1,.1],[1,2]])
master = diagram2cell(diagram,master,5)
diagram = assemblyDiagramInit([1,3,2])([[1],[.1,1,.1],[1,2]])
master = diagram2cell(diagram,master,6)
diagram = assemblyDiagramInit([1,3,2])([[1],[.1,1,.1],[2,1.5]])
master = diagram2cell(diagram,master,6)
toRemove = [2,3,4,5,149,143,154,140,141,146,147,152,153,144,145,150,151,156,157]
master = eliminaCelle(toRemove,master)
#tagli celle balconi dietro
diagram = assemblyDiagramInit([2,1,2])([[1,2],[1],[1,2]])
master = diagram2cell(diagram,master,4)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[.1,2]])
master = diagram2cell(diagram,master,49)
diagram = assemblyDiagramInit([2,1,2])([[2,.5],[1],[1,2]])
master = diagram2cell(diagram,master,90)
#elimino confine piano
toRemove = [4,49,90]
master = eliminaCelle(toRemove,master)
diagram = assemblyDiagramInit([2,1,2])([[1,2],[1],[1,2]])
master = diagram2cell(diagram,master,4)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[.1,2]])
master = diagram2cell(diagram,master,47)
diagram = assemblyDiagramInit([2,1,2])([[2,.5],[1],[1,2]])
master = diagram2cell(diagram,master,86)
diagram = assemblyDiagramInit([2,1,2])([[1,2],[1],[1,2]])
master = diagram2cell(diagram,master,4)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[.1,2]])
master = diagram2cell(diagram,master,46)
diagram = assemblyDiagramInit([2,1,2])([[2,.5],[1],[1,2]])
master = diagram2cell(diagram,master,84)
#rimuovo celle balconi dietro
toRemove = [127,128,130,132,134,135,136,137,138,140,142,144,145,146,147,148,150,152,154,155,156]
master = eliminaCelle(toRemove,master)
#taglio celle per balconi davanti #elimino confine piano 0 e 1
toRemove = [112,97,17]
master = eliminaCelle(toRemove,master)
#taglio balconi davanti
diagram = assemblyDiagramInit([3,2,2])([[.5,3,.5],[.6,2],[1,2]])
master = diagram2cell(diagram,master,96)
diagram = assemblyDiagramInit([3,2,2])([[.5,3,.5],[.6,2],[1,2]])
master = diagram2cell(diagram,master,17)
diagram = assemblyDiagramInit([3,2,2])([[.5,3,.5],[.6,2],[1,2]])
master = diagram2cell(diagram,master,96)
diagram = assemblyDiagramInit([3,2,2])([[.5,3,.5],[.6,2],[1,2]])
master = diagram2cell(diagram,master,18)
#elimio balconi
toRemove = [137,138,139,140,135,136,131,132,129,130,134,149,150,151,152,143,147,
148,141,142,143,144,146,161,162,163,164,159,160,158,155,156,153,154,94,173,174,
175,176,17,171,172,167,168,165,166,170]
master = eliminaCelle(toRemove,master)
#balcone ultimo piano
diagram = assemblyDiagramInit([3,2,2])([[.5,3,.5],[.6,2],[1,1]])
master = diagram2cell(diagram,master,17)
toRemove = [138,139,140,141,136,137,134,132,133,130,131]
master = eliminaCelle(toRemove,master)
#giardino piano 0
diagram = assemblyDiagramInit([2,2,2])([[3,.1],[3,.1],[1,1]])
master = diagram2cell(diagram,master,91)
diagram = assemblyDiagramInit([2,2,2])([[3,.1],[3,.1],[1,1]])
master = diagram2cell(diagram,master,16)
toRemove = [134,136,132,130,142,144,138,140]
master = eliminaCelle(toRemove,master)
#ultimo piano senza balcone
diagram = assemblyDiagramInit([1,3,1])([[1],[1,.1,3],[1]])
master = diagram2cell(diagram,master,90)
toRemove = [138]
master = eliminaCelle(toRemove,master)
#piccoli balconi dietro
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,114)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,115)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,115)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,116)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,116)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,117)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,114)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,114)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,114)
toRemove = [129,141,131,133,143,135,137,145,139]
master = eliminaCelle(toRemove,master)
#taglio celle sepatatore balconi
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,55)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,17)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,55)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,18)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,18)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,53)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,17)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,51)
toRemove = [132,142,136,138,130,144,134,140]
master = eliminaCelle(toRemove,master)
#taglio muro davanti tra 2 piani
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,34)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,67)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,66)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,33)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,64)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,32)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,62)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,31)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,60)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,39)
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,30)
#tettuccio ingresso principale
diagram = assemblyDiagramInit([1,2,1])([[1],[1,2],[1]])
master = diagram2cell(diagram,master,43)
toRemove = [129,131,135,139,143,149,147,141,137,133,127]
master = eliminaCelle(toRemove,master)
toRemove = [74,75,76,77,71,72,108]
master = eliminaCelle(toRemove,master)
palazzo = master
'''----------------------piano1-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,15,.2],[.2,15,.2],[0.2,4]])
V,CV = master
#porta
diagram = assemblyDiagramInit([1,3,2])([[1],[10,1,1],[2,1]])
master = diagram2cell(diagram,master,15)
toRemove = [19]
master = eliminaCelle(toRemove,master)
#faccio le camere nell'appartamento1#parete tra bagno 2 camere
diagram = assemblyDiagramInit([3,1,1])([[2,.1,2],[1],[1]])
master = diagram2cell(diagram,master,9)
#parete tra camere
diagram = assemblyDiagramInit([1,3,1])([[1],[3,.1,2],[1]])
master = diagram2cell(diagram,master,21)
#parete in corridio
diagram = assemblyDiagramInit([3,5,1])([[1,.1,1],[4,.2,2,.2,3],[1]])
master = diagram2cell(diagram,master,22)
#porta bagno
diagram = assemblyDiagramInit([3,1,2])([[1,1,1],[1],[2,1]])
master = diagram2cell(diagram,master,26)
#porta cucina
diagram = assemblyDiagramInit([3,1,2])([[1,1,1],[1],[2,1]])
master = diagram2cell(diagram,master,35)
#porte camere
diagram = assemblyDiagramInit([1,6,2])([[1],[4.4,1,1,1,1,1],[2,1]])
master = diagram2cell(diagram,master,21)
#finestra bagno cucina
diagram = assemblyDiagramInit([5,1,3])([[6,1,1.5,1,.5],[1],[1,2,1]])
master = diagram2cell(diagram,master,7)
#finestra camera1
diagram = assemblyDiagramInit([1,3,3])([[1],[5,.5,1],[1,2,1]])
master = diagram2cell(diagram,master,3)
#finestra camera2
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.5,3],[1]])
master = diagram2cell(diagram,master,75)
#finestra camera2
diagram = assemblyDiagramInit([3,1,3])([[2,1,8],[1],[1,2,1]])
master = diagram2cell(diagram,master,8)
#porta balcone
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.5,3],[1]])
master = diagram2cell(diagram,master,73)
#elimino tutte le finstre porte create
toRemove = [33,29,22,23,24,27,31,21,30,18,20,42,36,54,48,62,68,81,93,75,86,87]
master = eliminaCelle(toRemove,master)
#porta balcone
diagram = assemblyDiagramInit([3,1,1])([[3.5,2,5.5],[1],[1]])
master = diagram2cell(diagram,master,44)
#elimino finestra sopra garage grande
toRemove = [73]
master = eliminaCelle(toRemove,master)
#porta balcone
'''-------------------finePiano1--------------------'''
piano1 = master
'''----------------------piano2-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,15,.2],[.2,15,.2],[0.2,4]])
V,CV = master
#porta
diagram = assemblyDiagramInit([1,3,2])([[1],[10,1,1],[2,1]])
master = diagram2cell(diagram,master,3)
toRemove = [19]
master = eliminaCelle(toRemove,master)
#faccio le camere nell'appartamento1
diagram = assemblyDiagramInit([3,1,1])([[2,.1,2],[1],[1]])
master = diagram2cell(diagram,master,8)
#parete tra camere
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.1,2],[1]])
master = diagram2cell(diagram,master,23)
#parete tra cucina e bagno
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.1,2],[1]])
master = diagram2cell(diagram,master,23)
#porte
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.1,2],[1]])
master = diagram2cell(diagram,master,22)
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.1,2],[1]])
master = diagram2cell(diagram,master,27)
diagram = assemblyDiagramInit([1,3,2])([[1],[1,1,1],[2,1]])
master = diagram2cell(diagram,master,29)
diagram = assemblyDiagramInit([1,3,2])([[1],[1,1,1],[2,1]])
master = diagram2cell(diagram,master,30)
diagram = assemblyDiagramInit([3,1,1])([[2,.1,2],[1],[1]])
master = diagram2cell(diagram,master,21)
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.1,2],[1]])
master = diagram2cell(diagram,master,41)
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.1,2],[1]])
master = diagram2cell(diagram,master,41)
diagram = assemblyDiagramInit([1,3,2])([[1],[2,1,2],[2,1]])
master = diagram2cell(diagram,master,45)
diagram = assemblyDiagramInit([1,3,2])([[1],[3,1,1.5],[2,1]])
master = diagram2cell(diagram,master,46)
diagram = assemblyDiagramInit([1,3,2])([[1],[2,1,2],[2,1]])
master = diagram2cell(diagram,master,27)
#finestre
diagram = assemblyDiagramInit([3,1,3])([[1,1,2],[1],[1,2,1]])
master = diagram2cell(diagram,master,6)
diagram = assemblyDiagramInit([3,1,1])([[1,1,1],[1],[1]])
master = diagram2cell(diagram,master,63)
diagram = assemblyDiagramInit([3,1,1])([[1,1,1],[1],[1]])
master = diagram2cell(diagram,master,65)
diagram = assemblyDiagramInit([5,1,1])([[1,1,2,1,1],[1],[1]])
master = diagram2cell(diagram,master,67)
diagram = assemblyDiagramInit([1,3,1])([[1],[1,1,2],[1]])
master = diagram2cell(diagram,master,12)
diagram = assemblyDiagramInit([1,3,3])([[1],[1.5,1,1.5],[1,2,1]])
master = diagram2cell(diagram,master,78)
diagram = assemblyDiagramInit([1,3,3])([[1],[1.5,1,1.5],[1,2,1]])
master = diagram2cell(diagram,master,78)
diagram = assemblyDiagramInit([1,5,3])([[1],[1,.5,1,.5,1],[1,2,1]])
master = diagram2cell(diagram,master,78)
diagram = assemblyDiagramInit([3,1,1])([[1,1,1],[1],[1]])
master = diagram2cell(diagram,master,63)
diagram = assemblyDiagramInit([3,1,1])([[4,4,8],[1],[1]])
master = diagram2cell(diagram,master,8)
diagram = assemblyDiagramInit([3,1,2])([[1,1,1],[1],[2,1]])
master = diagram2cell(diagram,master,113)
#elimino volumi e porte
toRemove = [40,37,38,19,20,22,44,50,56,33,27,116,98,104,89,80,72,74,69,110,66]
master = eliminaCelle(toRemove,master)
'''-------------------finePiano2--------------------'''
piano2 = master
'''-------------------------------------------------'''
'''----------------------garageGrande-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,4,.2],[0.2,4]])
V,CV = master
#porta garage grande
diagram = assemblyDiagramInit([3,1,2])([[1,3,1],[1],[3,1]])
master = diagram2cell(diagram,master,7)
toRemove = [8,19]
master = eliminaCelle(toRemove,master)
garage1 = master
'''----------------------fineGarageGrande-----------------------'''
garage1 = master
'''----------------------GaragePiccolo-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,4,.2],[0.2,4]])
V,CV = master
#porta garage piccolo
diagram = assemblyDiagramInit([1,3,2])([[1],[1,2,1],[2,1]])
master = diagram2cell(diagram,master,3)
toRemove = [8,19]
master = eliminaCelle(toRemove,master)
garage2 = master
'''----------------------fineGaragePiccolo-----------------------'''
'''----------------------GarageEst-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,4,.2],[0.2,4]])
V,CV = master
#porta garage piccolo
diagram = assemblyDiagramInit([3,1,2])([[1,2,1],[1],[2,1]])
master = diagram2cell(diagram,master,11)
diagram = assemblyDiagramInit([3,1,3])([[1,1,1],[1],[1.5,2,1.5]])
master = diagram2cell(diagram,master,7)
toRemove = [8,18,26]
master = eliminaCelle(toRemove,master)
garage3 = master
'''----------------------fineGarageEst-----------------------'''
'''----------------------balconeWest-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,2,.2],[.2,4,.2],[0.2,1.5]])
V,CV = master
toRemove = [9,15]
master = eliminaCelle(toRemove,master)
balconeWest = master
'''----------------------fineBalconeWest-----------------------'''
'''----------------------BalconeDietro-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,2,.2],[0.2,1.5]])
V,CV = master
toRemove = [9,11]
master = eliminaCelle(toRemove,master)
balconeDietro = master
'''----------------------fineBalconeDietro-----------------------'''
'''----------------------BalconeDavanti-----------------------'''
#diagramma principale
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,2,.2],[0.2,1.5]])
V,CV = master
toRemove = [7,9]
master = eliminaCelle(toRemove,master)
balconeDavanti = master

'''----------------------fineBalconeDavanti-----------------------'''
#mappo balcone laterale west
palazzo = diagram2cell(balconeWest,palazzo,85)
palazzo = diagram2cell(balconeWest,palazzo,85)
palazzo = diagram2cell(balconeWest,palazzo,85)
#mappo balcone  dietro
palazzo = diagram2cell(balconeDietro,palazzo,99)
palazzo = diagram2cell(balconeDietro,palazzo,100)
palazzo = diagram2cell(balconeDietro,palazzo,102)

palazzo = diagram2cell(balconeDietro,palazzo,99)
palazzo = diagram2cell(balconeDietro,palazzo,99)
palazzo = diagram2cell(balconeDietro,palazzo,99)
#mappo balcone  davanti
palazzo = diagram2cell(balconeDavanti,palazzo,85)
palazzo = diagram2cell(balconeDavanti,palazzo,86)

palazzo = diagram2cell(balconeDavanti,palazzo,85)
palazzo = diagram2cell(balconeDavanti,palazzo,85)
palazzo = diagram2cell(balconeDavanti,palazzo,85)
#mappo piano -1 sul palazzo
palazzo = diagram2cell(appartamento1,palazzo,59)
#mappo garage grande
palazzo = diagram2cell(garage1,palazzo,5)
#mappo piano 1 sul palazzo
palazzo = diagram2cell(piano1,palazzo,6)
palazzo = diagram2cell(piano1,palazzo,7)
palazzo = diagram2cell(piano1,palazzo,8)
#mappo piano 2 sul palazzo
palazzo = diagram2cell(piano2,palazzo,56)
palazzo = diagram2cell(piano2,palazzo,57)
palazzo = diagram2cell(piano2,palazzo,58)
#mappo garage piccolo -1
palazzo = diagram2cell(garage2,palazzo,67)
#mappo garage piccolo 1
palazzo = diagram2cell(garage3,palazzo,71)
#VIEW(visulizzaModello(palazzo))
###############################################
'''----------------------BEZIER------------------------------'''
#nuvola
Nuv1 = [[1.62, 4], [1.75, 4.66], [2.01, 4.54], [2.32, 4.67]]
Nuv1 = MAP(Bezier(Nuv1))(Dom1D)
########################################
Nuv2 = [[1.62, 4], [0.05, 4.08], [0.43, 2.14], [2.16, 2.42]]
Nuv2 = MAP(Bezier(Nuv2))(Dom1D)
########################################
Nuv3 = [[2.85, 2.12], [2.57, 2.01], [2.22, 2.2], [2.16, 2.42]]
Nuv3 = MAP(Bezier(Nuv3))(Dom1D)
########################################
Nuv4 = [[2.85, 2.12], [2.81, 1.83], [4.36, 1.39], [4.76, 2.49]]
Nuv4 = MAP(Bezier(Nuv4))(Dom1D)
########################################
Nuv5 = [[5.51, 2.83], [5.52, 2.44], [5.14, 2.15], [4.76, 2.49]]
Nuv5 = MAP(Bezier(Nuv5))(Dom1D)
########################################
Nuv6 = [[5.51, 2.83], [6.84, 2.86], [6.6, 4.01], [5.67, 4.19]]
Nuv6 = MAP(Bezier(Nuv6))(Dom1D)
########################################
Nuv7 = [[4.31, 4.79], [5.12, 5.87], [6.1, 4.75], [5.67, 4.19]]
Nuv7 = MAP(Bezier(Nuv7))(Dom1D)
########################################
Nuv8 = [[4.31, 4.79], [4.42, 4.99], [3.68, 5.2], [3.67, 4.8]]
Nuv8 = MAP(Bezier(Nuv8))(Dom1D)
########################################
Nuv9 = [[2.32, 4.67], [2.65, 5.42], [3.24, 5.63], [3.67, 4.8]]
Nuv9 = MAP(Bezier(Nuv9))(Dom1D)
########################################
nuovola = STRUCT([Nuv1,Nuv2,Nuv3,Nuv4,Nuv5,Nuv6,Nuv7,Nuv8,Nuv9])
nuovola = SOLIDIFY(nuovola)
#nuovola = PROD([nuovola, Q(.5)])
#nuovola = MAP([S1,S3,S2])(nuovola)
nuovola = T([1,2,3])([10,5,30])(nuovola)
nuovola = MATERIAL([1,1,1,0, 0,0,0,0.2, 0,0,0,0, 0,0,0,0, 50])(nuovola)
#palazzo = STRUCT(MKPOLS(palazzo))
#ciao = STRUCT([palazzo,nuovola])
#VIEW(ciao)
'''-------------------------------------------------------------'''
palazzo = COLOR(colorePalazzo)(STRUCT(MKPOLS(palazzo)))

VIEW(palazzo)
#VIEW(scheletroModello(palazzo))

