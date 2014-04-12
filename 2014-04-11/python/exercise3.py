'''-------------------------------HOMEWORK2-ESERCIZIO3--------------------------------------------'''
'''NOTE: non sono disegnate tutte le finestre del progetto originale in quanto
i tempi di elaborazione sono notevoli '''
'''----------------------------------------------------------------------------------'''

from pyplasm import *
from exercise2 import *

#############################################################
colorwindow = rgb([166, 161, 122])
colorbuilding = rgb([216, 180, 141])
colorPorta = rgb([76, 132, 197])
colorstrade = rgb([132, 141, 143])
colorGiardino = rgb([45, 140, 4])
colorStradePrincipali = rgb([50, 53, 49])
coloralbero = rgb([77, 255, 0])
colortronco = rgb([199, 197, 136])
colorMuraConfine = rgb([109, 128, 198])
colorSpartiStrada = rgb([232, 232, 232])
colortronco = rgb([199, 197, 136])
colorbase = rgb([112, 217, 246])

#############################################################
'''------------------definizioni funioni------------------ '''
#############################################################
def sphere1(p): 
	return [COS(p[0]), SIN(p[0])]
#############################################################
def domain(n): 
	return INTERVALS(2*PI)(n)
#############################################################
def disk2D(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]
#############################################################
'''albero'''
#############################################################
domain2D = PROD([INTERVALS(2*PI)(32), INTERVALS(1)(3)])
v=MAP(disk2D)(domain2D)
tronco = COLOR(colortronco)(PROD([v, Q(4)]))
#colonnA1 = STRUCT(10*[colonna,T(1)(4)])
alb = CYLINDER ([2,3])(3)
alb = COLOR(coloralbero)(MAP([S2,S3,S1])(alb))
albero = STRUCT([alb,T([1,2,3])([0,1.5,-5])(tronco)])
albero = T([1,2,3])([7,-5,5])(albero)
#############################################################
'''lampioni'''
#############################################################
palo = CYLINDER([0.2,1.5])(40)
palla = T(3)(2)((SPHERE(0.5)([20,20])))
h1 = STRUCT([palo,palla])
lampioni1 =T([1,2])([7,-1])(h1)
lampioni2 =T([1,2])([7,-10])(h1)
lampioni3 =T([1,2])([7,-8])(h1)
lampioni = STRUCT([lampioni1,lampioni2,lampioni3])
#############################################################
'''base'''
#############################################################
basei1 = COLOR(colorbase)(T([1,2,3])([-85,-180,-5])((CUBOID([370,360,.01]))))

#############################################################
'''palazzo'''
#############################################################
building1 = COLOR(colorbuilding)(CUBOID([4,4,10]))
#############################################################
'''finestre'''
#############################################################
window1top = COLOR(colorwindow)(T([1,2,3])([2.5,0,7])(CUBOID([1,0.1,2])))
window2top = COLOR(colorwindow)(T([1,2,3])([.5,0,7])(CUBOID([1,0.1,2])))
window1down = COLOR(colorwindow)(T([1,2,3])([2.5,0,3])(CUBOID([1,0.1,2])))
window2down = COLOR(colorwindow)(T([1,2,3])([.5,0,3])(CUBOID([1,0.1,2])))
#############################################################
'''porta'''
#############################################################
door= COLOR(colorPorta)(T([1,2,3])([1.5,0,0])(CUBOID([1,0.1,2])))
#############################################################
'''strada'''
#############################################################
st1 = T([1,2])([1.5,-10])((CUBOID([1,10,0.05])))
st1Principale = T([1,2])([1.5,-10])((CUBOID([10,1,0.05])))
strada  = COLOR(colorstrade)(STRUCT([st1,st1Principale]))
giardino = COLOR(colorGiardino)(T([1,2])([1.5,-9])((CUBOID([10,9,0.05]))))
#############################################################
'''spazio vuoto tra un palazzo e altro'''
#############################################################
vuoto1 = COLOR(BLACK)(CUBOID([10,4,.1]))
#############################################################
'''vicinato Completo'''
#############################################################
palazzo1=STRUCT([lampioni,albero,vuoto1,giardino,strada,window1top,window2top,window1down,window2down,door,building1])

#############################################################
'''replica vicinato'''
#############################################################
palazzi = STRUCT(10*[palazzo1,T(1)(10)])
pala = [T(1)(10), palazzo1]
palazziVicini = STRUCT(NN(10)(pala))
build = [T(2)(14), palazziVicini]
neighbourhood = STRUCT(NN(5)(build))
#############################################################
'''spazio vuoto tra strada principale e ultimo palazzo'''
#############################################################
vuoto2 = T([1,2])([110,14])(COLOR(BLACK)(CUBOID([1.5,4,.1])))
vuoto3 = T([1,2])([110,28])(COLOR(BLACK)(CUBOID([1.5,4,.1])))
vuoto4 = T([1,2])([110,42])(COLOR(BLACK)(CUBOID([1.5,4,.1])))
vuoto5 = T([1,2])([110,56])(COLOR(BLACK)(CUBOID([1.5,4,.1])))
vuoto6 = T([1,2])([110,70])(COLOR(BLACK)(CUBOID([1.5,4,.1])))
spaziVuoti  =STRUCT([vuoto2,vuoto3,vuoto4,vuoto5,vuoto6])
#############################################################
'''strada main'''
#############################################################
st1main = COLOR(colorStradePrincipali)(T([1,2])([1.5,-10])((CUBOID([4,70,0.05]))))
vista = STRUCT([neighbourhood,T([1,2])([110,14])(st1main),spaziVuoti])
#############################################################
'''strada main2'''
#############################################################
st1main2 = COLOR(colorStradePrincipali)(T([1,2])([7.5,4])((CUBOID([4,70,0.05]))))
#############################################################
'''vicinato'''
#############################################################
vistaPalazzi = STRUCT([vista,st1main2])
vicinato = T([1,2])([0,40])(vistaPalazzi)
#############################################################
'''confini model'''
#############################################################
confine1 = T([1,2,3])([-100,-200,-5])((CUBOID([400,400,10])))
confine2 = T([1,2,3])([-85,-180,-5])((CUBOID([370,360,10])))
confine = DIFFERENCE([confine1,confine2])
#############################################################
'''porta e finestre per le mura di confine'''
#############################################################
portaMuraIntorno1 = T([1,2,3])([283,-6,-5])(COLOR(RED)(T([1,2,3])([1.5,0,0])(CUBOID([16,7,8]))))
portaMuraIntorno2 = T([1,2,3])([283,-80,-3])(COLOR(RED)(T([1,2,3])([1.5,0,0])(CUBOID([16,5,5]))))
portaMuraIntorno3 = T([1,2,3])([283,80,-3])(COLOR(RED)(T([1,2,3])([1.5,0,0])(CUBOID([16,5,5]))))
portaMuraIntorno4 = T([1,2,3])([283,-120,-3])(COLOR(RED)(T([1,2,3])([1.5,0,0])(CUBOID([16,5,5]))))
portaMuraIntorno5 = T([1,2,3])([283,120,-3])(COLOR(RED)(T([1,2,3])([1.5,0,0])(CUBOID([16,5,5]))))
porta = DIFFERENCE([confine,portaMuraIntorno1])
porta = DIFFERENCE([porta,portaMuraIntorno2])
porta = DIFFERENCE([porta,portaMuraIntorno3])
porta = DIFFERENCE([porta,portaMuraIntorno4])
porta = DIFFERENCE([porta,portaMuraIntorno5])
porte = T(3)(4)(COLOR(colorMuraConfine)(porta))
compl_Vista = STRUCT([modelloCompleto1,porte,vicinato,intornoCastello])
#############################################################
'''strade per castello '''
#############################################################
stradaCastelloCase1 = COLOR(colorStradePrincipali)(T([1,2])([111.5,-25])((CUBOID([4,70,0.05]))))
stradaCastelloCase2 = COLOR(colorStradePrincipali)(T([1,2])([11,-25])((CUBOID([380,5,0.05]))))
spartiStrada = COLOR(GREEN)(T([1,2,3])([30,-23,.1])((CUBOID([400,1,1]))))
#############################################################
'''lampioni stradali '''
#############################################################
luce = [T(1)(15), h1]
luceStrada = STRUCT(NN(25)(luce))
luceStrada1 = T([1,2])([0,-5])(STRUCT(NN(25)(luce)))
luceStradaPrincipale = T([1,2])([0,-20])(STRUCT([luceStrada,luceStrada1]))
#############################################################
stradePrincipali = T([1,2])([0,20])(STRUCT([luceStradaPrincipale,spartiStrada,stradaCastelloCase1,stradaCastelloCase2]))
#############################################################
collegamenti = STRUCT([stradePrincipali,compl_Vista,basei1])
VIEW(collegamenti)