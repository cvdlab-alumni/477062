from exercise1 import *
from random import randint
'''***********************************************************'''
appartamento1 = master
master = assemblyDiagramInit([8,3,9])([[4,6,0.2,3,.2,9,.5,4],[4,8,8],[.5,4,.2,4,.2,4,.2,4,2]])
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
master = diagram2cell(diagram,master,6)
diagram = assemblyDiagramInit([1,3,2])([[1],[.1,1,.1],[4,2]])
master = diagram2cell(diagram,master,6)
toRemove = [2,3,4,5,143,149,155,140,141,146,147,152,153,144,145,150,151,156,157]
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
diagram = assemblyDiagramInit([2,1,2])([[1,2],[1],[1.6,1]])
master = diagram2cell(diagram,master,4)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[.1,2]])
master = diagram2cell(diagram,master,46)
diagram = assemblyDiagramInit([2,1,2])([[2,.5],[1],[1.6,1]])
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
master = diagram2cell(diagram,master,17)
master = diagram2cell(diagram,master,96)
master = diagram2cell(diagram,master,18)
#elimio balconi
toRemove = [137,138,139,140,135,136,131,132,129,130,134,149,150,151,152,143,147,148,141,142,143,144,
146,161,162,163,164,159,160,158,155,156,153,154,94,173,174,175,176,17,171,172,167,168,165,166,170]
master = eliminaCelle(toRemove,master)
#balcone ultimo piano
diagram = assemblyDiagramInit([3,2,2])([[.5,3,.5],[.6,2],[4,2]])
master = diagram2cell(diagram,master,17)
toRemove = [140,141,136,137,132,133,138,139,135,130,131]
master = eliminaCelle(toRemove,master)
#giardino piano 0
diagram = assemblyDiagramInit([2,2,2])([[3,.1],[3,.1],[1,1]])
master = diagram2cell(diagram,master,91)
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
master = diagram2cell(diagram,master,115)
master = diagram2cell(diagram,master,115)
master = diagram2cell(diagram,master,116)
master = diagram2cell(diagram,master,116)
master = diagram2cell(diagram,master,117)
master = diagram2cell(diagram,master,114)
master = diagram2cell(diagram,master,114)
master = diagram2cell(diagram,master,114)
toRemove = [129,141,131,133,143,135,137,145,139]
master = eliminaCelle(toRemove,master)
#taglio celle sepatatore balconi
diagram = assemblyDiagramInit([1,2,1])([[1],[1,1],[1]])
master = diagram2cell(diagram,master,55)
master = diagram2cell(diagram,master,17)
master = diagram2cell(diagram,master,55)
master = diagram2cell(diagram,master,18)
master = diagram2cell(diagram,master,18)
master = diagram2cell(diagram,master,53)
master = diagram2cell(diagram,master,17)
master = diagram2cell(diagram,master,51)
toRemove = [132,142,136,138,130,144,134,140]
master = eliminaCelle(toRemove,master)
#taglio muro davanti tra 2 piani
diagram = assemblyDiagramInit([1,2,1])([[1],[1,3],[1]])
master = diagram2cell(diagram,master,34)
master = diagram2cell(diagram,master,67)
master = diagram2cell(diagram,master,66)
master = diagram2cell(diagram,master,33)
master = diagram2cell(diagram,master,64)
master = diagram2cell(diagram,master,32)
master = diagram2cell(diagram,master,62)
master = diagram2cell(diagram,master,31)
master = diagram2cell(diagram,master,60)
master = diagram2cell(diagram,master,39)
master = diagram2cell(diagram,master,30)
#tettuccio ingresso principale
diagram = assemblyDiagramInit([1,2,1])([[1],[1,2],[1]])
master = diagram2cell(diagram,master,43)
toRemove = [129,131,135,139,143,149,147,141,137,133,127]
master = eliminaCelle(toRemove,master)
toRemove = [74,75,76,77,71,72,108]
master = eliminaCelle(toRemove,master)
#taglio pareti tra balconi dietro
toRemove = [108,109,110,111,112,113,114,115,116,117,118,]
master = eliminaCelle(toRemove,master)
palazzo = master
'''----------------------piano1-----------------------'''
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
piano1 = master
'''-------------------piano2---------------------'''
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
master = diagram2cell(diagram,master,27)
diagram = assemblyDiagramInit([1,3,2])([[1],[1,1,1],[2,1]])
master = diagram2cell(diagram,master,29)
master = diagram2cell(diagram,master,30)
diagram = assemblyDiagramInit([3,1,1])([[2,.1,2],[1],[1]])
master = diagram2cell(diagram,master,21)
diagram = assemblyDiagramInit([1,3,1])([[1],[2,.1,2],[1]])
master = diagram2cell(diagram,master,41)
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
master = diagram2cell(diagram,master,65)
diagram = assemblyDiagramInit([5,1,1])([[1,1,2,1,1],[1],[1]])
master = diagram2cell(diagram,master,67)
diagram = assemblyDiagramInit([1,3,1])([[1],[1,1,2],[1]])
master = diagram2cell(diagram,master,12)
diagram = assemblyDiagramInit([1,3,3])([[1],[1.5,1,1.5],[1,2,1]])
master = diagram2cell(diagram,master,78)
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
piano2 = master
'''-------------------garageGrande------------------'''
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,4,.2],[0.2,4]])
V,CV = master
#porta garage grande
diagram = assemblyDiagramInit([3,1,2])([[1,3,1],[1],[3,1]])
master = diagram2cell(diagram,master,7)
toRemove = [8,19]
master = eliminaCelle(toRemove,master)
garage1 = master
'''-------------------GaragePiccolo-----------------------'''
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,4,.2],[0.2,4]])
V,CV = master
#porta garage piccolo
diagram = assemblyDiagramInit([1,3,2])([[1],[1,2,1],[2,1]])
master = diagram2cell(diagram,master,3)
toRemove = [8,19]
master = eliminaCelle(toRemove,master)
garage2 = master
'''----------------------GarageEst-----------------------'''
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
'''----------------------balconeWest-----------------------'''
master = assemblyDiagramInit([3,3,2])([[.2,2,.2],[.2,4,.2],[0.2,1.5]])
V,CV = master
toRemove = [9,15]
master = eliminaCelle(toRemove,master)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[3,.1]])
master = diagram2cell(diagram,master,3)
master = diagram2cell(diagram,master,4)
master = diagram2cell(diagram,master,1)
master = diagram2cell(diagram,master,4)
master = diagram2cell(diagram,master,6)
master = diagram2cell(diagram,master,7)
master = diagram2cell(diagram,master,9)
diagram = assemblyDiagramInit([1,23,1])([[1],[.3,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5],[1]])
master = diagram2cell(diagram,master,9)
diagram = assemblyDiagramInit([11,1,1])([[.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5],[1],[1]])
master = diagram2cell(diagram,master,16)
master = diagram2cell(diagram,master,14)
toRemove = [53,51,49,47,45,43,42,40,38,36,34,32,30,28,26,24,22,20,54,56,58,60,62,64]
master = eliminaCelle(toRemove,master)
balconeWest = master
'''----------------------BalconeDietro-----------------------'''
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,2,.2],[0.2,1.5]])
V,CV = master
toRemove = [9,11]
master = eliminaCelle(toRemove,master)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[3,.1]])
master = diagram2cell(diagram,master,7)
master = diagram2cell(diagram,master,1)
master = diagram2cell(diagram,master,9)
master = diagram2cell(diagram,master,10)
master = diagram2cell(diagram,master,11)
master = diagram2cell(diagram,master,2)
master = diagram2cell(diagram,master,3)
diagram = assemblyDiagramInit([25,1,1])([[.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5],[1],[1]])
master = diagram2cell(diagram,master,9)
diagram = assemblyDiagramInit([1,13,1])([[1],[.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5],[1]])
master = diagram2cell(diagram,master,14)
master = diagram2cell(diagram,master,17)
toRemove = [70,68,66,64,62,60,58,20,22,24,26,28,30,32,34,36,38,40,42,44,45,47,49,51,53,55,57]
master = eliminaCelle(toRemove,master)
balconeDietro = master
'''--------BalconeDavanti------------------'''
master = assemblyDiagramInit([3,3,2])([[.2,4,.2],[.2,2,.2],[0.2,1.5]])
V,CV = master
toRemove = [7,9]
master = eliminaCelle(toRemove,master)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[3,.1]])
master = diagram2cell(diagram,master,9)
master = diagram2cell(diagram,master,5)
master = diagram2cell(diagram,master,3)
master = diagram2cell(diagram,master,1)
master = diagram2cell(diagram,master,11)
master = diagram2cell(diagram,master,9)
master = diagram2cell(diagram,master,7)
diagram = assemblyDiagramInit([25,1,1])([[.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5],[1],[1]])
master = diagram2cell(diagram,master,9)
diagram = assemblyDiagramInit([1,13,1])([[1],[.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5],[1]])
master = diagram2cell(diagram,master,18)
master = diagram2cell(diagram,master,12)
toRemove = [45,47,49,51,53,55,57,20,22,24,26,28,30,32,34,36,38,40,42,44,58,60,62,64,66,68,70]
master = eliminaCelle(toRemove,master)
balconeDavanti = master
'''-----------Ingresso---------------------'''
diagram = assemblyDiagramInit([1,3,2])([[1],[.1,2,2],[1,1]])
palazzo = diagram2cell(diagram,palazzo,42)
toRemove = [125,123]
palazzo = eliminaCelle(toRemove,palazzo)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[1,1]])
palazzo = diagram2cell(diagram,palazzo,55)
palazzo = diagram2cell(diagram,palazzo,29)
diagram = assemblyDiagramInit([3,1,1])([[.5,2,.5],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,118)
diagram = assemblyDiagramInit([3,1,2])([[.5,2,.5],[1],[.5,1]])
palazzo = diagram2cell(diagram,palazzo,118)
diagram = assemblyDiagramInit([2,1,1])([[.1,3],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,94)
toRemove = [90,133,120,122,117,128,124,110,111,109,108,107,106,104,105,115,112]
palazzo = eliminaCelle(toRemove,palazzo)
'''-----------ScaleIngresso----------------'''
#scale ingresso#creolo spazio per le scale
diagram = assemblyDiagramInit([3,1,1])([[1,3,1],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,106)
toRemove = [116,118]
palazzo = eliminaCelle(toRemove,palazzo)
#faccio le scale a parte
master = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.1,8,.1],[.1,4]])
V,CV = master
diagram = assemblyDiagramInit([1,9,8])([[1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]])
master = diagram2cell(diagram,master,9)
toRemove = [24,32,40,48,56,64,72,80,23,31,39,47,55,63,71,22,30,38,46,54,62,53,45,37,29,21,44,36,28,20,19,27,35,26,18,17]
master = eliminaCelle(toRemove,master)
#ringhiere scale di ingresso
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[4,.1]])
master = diagram2cell(diagram,master,3)
master = diagram2cell(diagram,master,13)
diagram = assemblyDiagramInit([1,29,1])([[1],[.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,
	.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5,.1,.5],[1]])
master = diagram2cell(diagram,master,51)
master = diagram2cell(diagram,master,52)
toRemove = [53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,6]
master = eliminaCelle(toRemove,master)
scaleIngresso = master
'''-----------FineScaleIngresso----------------'''
'''-----------ultimo piano divisioni-----------'''
diagram = assemblyDiagramInit([1,3,1])([[1],[3,.1,4],[1]])
palazzo = diagram2cell(diagram,palazzo,37)
palazzo = diagram2cell(diagram,palazzo,25)
palazzo = diagram2cell(diagram,palazzo,48)
#balcone davanti ultimo piano sinitro
diagram = assemblyDiagramInit([3,1,2])([[.5,3,.5],[1],[1.5,1]])
palazzo = diagram2cell(diagram,palazzo,93)
toRemove = [126,127,122,123,125]
palazzo = eliminaCelle(toRemove,palazzo)
#ingresso ultimo piano#e divisione ultimo piano
diagram = assemblyDiagramInit([1,3,2])([[1],[10,3,2],[2,1]])
palazzo = diagram2cell(diagram,palazzo,121)
diagram = assemblyDiagramInit([2,3,1])([[10,.5],[.5,10,.5],[1]])
palazzo = diagram2cell(diagram,palazzo,60)
diagram = assemblyDiagramInit([2,3,1])([[.5,10],[.5,10,.5],[1]])
palazzo = diagram2cell(diagram,palazzo,12)
diagram = assemblyDiagramInit([1,2,1])([[1],[.5,4],[1]])
palazzo = diagram2cell(diagram,palazzo,111)
palazzo = diagram2cell(diagram,palazzo,116)
palazzo = diagram2cell(diagram,palazzo,113)
toRemove = [124,133,140,136,138]
palazzo = eliminaCelle(toRemove,palazzo)
#creo i muri ultimo piano
diagram = assemblyDiagramInit([7,1,2])([[2,1,2,1,2,1,2],[1],[2,1]])
palazzo = diagram2cell(diagram,palazzo,123)
palazzo = diagram2cell(diagram,palazzo,123)
diagram = assemblyDiagramInit([1,7,2])([[1],[2,1,2,1,2,1,2],[2,1]])
palazzo = diagram2cell(diagram,palazzo,127)
diagram = assemblyDiagramInit([7,1,2])([[2,1,2,1,2,1,2],[1],[2,1]])
palazzo = diagram2cell(diagram,palazzo,128)
palazzo = diagram2cell(diagram,palazzo,128)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[2,1]])
palazzo = diagram2cell(diagram,palazzo,124)
#parte alta muri ultimo piano
toRemove = [201,157,155,153,151,149,147,145,131,133,135,137,139,141,143,173,175,177,
179,181,183,185,159,161,163,165,167,169,171,187,189,191,193,195,197,199]
palazzo = eliminaCelle(toRemove,palazzo)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[2,1]])
palazzo = diagram2cell(diagram,palazzo,127)
toRemove = [141,139,137,162,160,158,148,146,144,153,155,166,130,132,134]
palazzo = eliminaCelle(toRemove,palazzo)
#colonne ultimo piano
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[2,1]])
palazzo = diagram2cell(diagram,palazzo,127)
palazzo = diagram2cell(diagram,palazzo,127)
palazzo = diagram2cell(diagram,palazzo,124)
palazzo = diagram2cell(diagram,palazzo,123)
palazzo = diagram2cell(diagram,palazzo,123)
palazzo = diagram2cell(diagram,palazzo,123)
toRemove = [151,153,149,147,155,157]
palazzo = eliminaCelle(toRemove,palazzo)
#taglio balconi west
diagram = assemblyDiagramInit([2,1,1])([[1,2],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,77)
palazzo = diagram2cell(diagram,palazzo,77)
palazzo = diagram2cell(diagram,palazzo,77)
toRemove = [149,151,153]
palazzo = eliminaCelle(toRemove,palazzo)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[4,.2]])
palazzo = diagram2cell(diagram,palazzo,11)
diagram = assemblyDiagramInit([1,1,2])([[1],[1],[4,.2]])
palazzo = diagram2cell(diagram,palazzo,57)
'''--------FineStrutturaEsterna--------'''
#mappo balcone laterale west
palazzo = diagram2cell(balconeWest,palazzo,147)
palazzo = diagram2cell(balconeWest,palazzo,147)
palazzo = diagram2cell(balconeWest,palazzo,147)
#mappo balcone  dietro
palazzo = diagram2cell(balconeDietro,palazzo,86)
palazzo = diagram2cell(balconeDietro,palazzo,87)
palazzo = diagram2cell(balconeDietro,palazzo,88)
palazzo = diagram2cell(balconeDietro,palazzo,86)
palazzo = diagram2cell(balconeDietro,palazzo,86)
palazzo = diagram2cell(balconeDietro,palazzo,86)
#mappo balcone  davanti
palazzo = diagram2cell(balconeDavanti,palazzo,75)
palazzo = diagram2cell(balconeDavanti,palazzo,76)
palazzo = diagram2cell(balconeDavanti,palazzo,103)
palazzo = diagram2cell(balconeDavanti,palazzo,75)
palazzo = diagram2cell(balconeDavanti,palazzo,75)
palazzo = diagram2cell(balconeDavanti,palazzo,75)
#scale ingresso
palazzo = diagram2cell(scaleIngresso,palazzo,94)
#mappo piano -1 sul palazzo
palazzo = diagram2cell(appartamento1,palazzo,51)
#mappo garage grande
palazzo = diagram2cell(garage1,palazzo,5)
#mappo piano 1 sul palazzo sopra garage grande
palazzo = diagram2cell(piano1,palazzo,6)
palazzo = diagram2cell(piano1,palazzo,7)
palazzo = diagram2cell(piano1,palazzo,130)
#mappo piano 2 sul palazzo
palazzo = diagram2cell(piano2,palazzo,49)
palazzo = diagram2cell(piano2,palazzo,50)
palazzo = diagram2cell(piano2,palazzo,129)
#mappo garage piccolo -1
palazzo = diagram2cell(garage2,palazzo,59)
#mappo garage piccolo 1
palazzo = diagram2cell(garage3,palazzo,63)
'''----------------------BEZIER------------------------------'''
nuvola1 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola2 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola3 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola4 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola5 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola6 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola7 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola8 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola9 = T([1,2,3])([ randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola10 = T([1,2,3])([randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola11 = T([1,2,3])([randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola12 = T([1,2,3])([randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola13 = T([1,2,3])([randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvola14 = T([1,2,3])([randint(1,50), randint(0,36), randint(30,33)])(generaNuvola())
nuvole = STRUCT([nuvola1,nuvola2,nuvola3,nuvola4,nuvola5,nuvola6,
	nuvola7,nuvola8,nuvola9,nuvola10,nuvola11,nuvola12,nuvola13,
	nuvola14])
#rampa laterale
puntitriangolo  = [[[0,4],[0,20],[6,20],[0,4]]]
triangolo = STRUCT(AA(POLYLINE)(puntitriangolo))
rampa = SOLIDIFY(triangolo)
rampa = PROD([rampa,Q(4)])
rampa = MAP([S3,S2,S1])(rampa)
rampa = T([1,2,3])([0,0,.5])(rampa)
rampa = COLOR(coloreRampa)(rampa)
#rampa
puntitriangolo  = [[[0,2],[0,10],[1.8,10],[0,2]]]
triangolo = STRUCT(AA(POLYLINE)(puntitriangolo))
rampaGarage = SOLIDIFY(triangolo)
rampaGarage = PROD([rampaGarage,Q(4)])
rampaGarage = MAP([S3,S2,S1])(rampaGarage)
rampaGarage = T([1,2,3])([22.9,10,4.7])(rampaGarage)
rampaGarage = COLOR(coloreRampa)(rampaGarage)
'''---------------------Macchina-----------------------'''
Al0 = [[3.02, 2.4], [2.71, 2.42], [2.12, 2.34], [1.19, 2.43]]
Al0 = MAP(Bezier(Al0))(Dom1D)
Al1 = [[3.02, 2.4], [2.73, 3.05], [3.79, 3.22], [3.65, 2.46]]
Al1 = MAP(Bezier(Al1))(Dom1D)
Al2 = [[3.78, 3.01], [4, 2.44], [4.01, 2.46], [3.65, 2.46]]
Al2 = MAP(Bezier(Al2))(Dom1D)
Al3 = [[3.78, 3.01], [3.34, 3.22], [2.87, 3.1], [2.55, 3.18]]
Al3 = MAP(Bezier(Al3))(Dom1D)
Al4 = [[1.63, 3.31], [2.23, 3.39], [2.25, 3.28], [2.55, 3.18]]
Al4 = MAP(Bezier(Al4))(Dom1D)
Al5 = [[1.63, 3.31], [1.34, 3.26], [1.21, 3.1], [1.1, 3.08]]
Al5 = COLOR(GREEN)(MAP(Bezier(Al5))(Dom1D))
Al6 = [[0.11, 2.59], [0.3, 2.76], [0.54, 3.01], [1.1, 3.08]]
Al6 = COLOR(RED)(MAP(Bezier(Al6))(Dom1D))
Al7 = [[0.11, 2.59], [0.14, 2.58], [0.26, 2.54], [0.11, 2.44]]
Al7 = MAP(Bezier(Al7))(Dom1D)
Al8 = [[0.63, 2.38], [0.42, 2.34], [0.23, 2.43], [0.11, 2.44]]
Al8 = MAP(Bezier(Al8))(Dom1D)
Al9 = [[0.63, 2.38], [0.38, 3.08], [1.34, 3.12], [1.19, 2.43]]
Al9 = MAP(Bezier(Al9))(Dom1D)
vistalaterale = STRUCT([Al0,Al1,Al2,Al3,Al4,Al5,Al6,Al7,Al8,Al9])
vistalaterale = SOLIDIFY(vistalaterale)
vistaCompelta = PROD([vistalaterale,Q(1.5)])
macchina = vistaCompelta
macchina = COLOR(coloreMacchina)(MAP([S1,S3,S2])(macchina))
#asse1
semiAsse1 = CYLINDER ([.2,1.1])(35)
semiAsse1 = T([1,2,3])([.9,.11,.2])(semiAsse1)
semiAsse2 = T([1,2,3])([2.4,-.01,0])(semiAsse1)
asseCompleto = STRUCT([semiAsse1,semiAsse2])
asseCompleto = COLOR(coloreAsseMacchina)(T([1,2,3])([0,0,2.5])(MAP([S1,S3,S2])(asseCompleto)))
#ruota1
ruota1 = CYLINDER ([.3,.2])(35)
ruota1 = T([1,2,3])([.9,.1,0])(ruota1)
ruota2 = T([1,2,3])([0,0,1.3])(ruota1)
ruoteAvanti  =STRUCT([ruota1,ruota2])
ruoteDietro = T([1,2,3])([2.4,.03,0])(ruoteAvanti)
#ruote compelte
ruoteComplete = T([1,2,3])([0,2.5,0])(STRUCT([ruoteAvanti,ruoteDietro]))
ruoteComplete = COLOR(coloreRuoteMacchina)(MAP([S1,S3,S2])(ruoteComplete))
#macchina completa piano -1
macchinaCompleta1 = T([1,2,3])([4,1,-1.8])(STRUCT([macchina,ruoteComplete,asseCompleto]))
#macchina completa piano 1
macchinaCompleta2 = T([1,2,3])([15,21,6])(macchinaCompleta1)
macchinaCompleta3 = T(1)(8)(macchinaCompleta1)
macchinaCompleta4 = T(1)(-9)(macchinaCompleta2)
macchinaCompleta5 = T(1)(-18)(macchinaCompleta2)
macchinaCompleta6 = T(1)(8)(macchinaCompleta2)
macchinaCompleta7 = T(1)(18)(macchinaCompleta2)
insiemeMacchine = STRUCT([macchinaCompleta1,macchinaCompleta2,macchinaCompleta3,
	macchinaCompleta4,macchinaCompleta5,macchinaCompleta6,macchinaCompleta7])
'''------------Strada-----------------'''
strada = CUBOID([50,6,6.5])
strada = COLOR(coloreRampa)(T([1,2,3])([0,20,0])(strada))
'''------------giardino---------------'''
giardino = CUBOID([50,10,6.5])
giardino = COLOR(coloreGiardino)(T([1,2,3])([0,26,0])(giardino))
giardinoEst = CUBOID([23.1,20,6.5])
giardinoEst = COLOR(coloreGiardino)(T([1,2,3])([26.9,0,0])(giardinoEst))
'''------------Alberi-----------------'''
albero1 = generaAlbero([4,30,6])([.5,7])
albero2 = generaAlbero([14,30,6])([.5,7])
albero3 = generaAlbero([24,30,6])([.5,7])
albero4 = generaAlbero([34,30,6])([.5,7])
albero5 = generaAlbero([44,30,6])([.5,7])
alberi = STRUCT([albero1,albero2,albero3,albero4,albero5])
'''----------------------------------'''
palazzo = COLOR(colorePalazzo)(STRUCT(MKPOLS(palazzo)))
palazzo = STRUCT([palazzo,nuvole,rampa,rampaGarage,insiemeMacchine,strada,giardino,giardinoEst,alberi])
VIEW(palazzo)