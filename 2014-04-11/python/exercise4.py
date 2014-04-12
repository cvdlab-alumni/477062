from pyplasm import *
from exercise3 import *
'''-------------------------------HOMEWORK2-ESERCIZIO4--------------------------------------------'''
'''NOTE: non sono disegnate tutte le finestre del progetto originale in quanto
i tempi di elaborazione sono notevoli '''
'''----------------------------------------------------------------------------------'''

#############################################################
'''-------------alberi------------------ '''
#############################################################
domain2D = PROD([INTERVALS(2*PI)(32), INTERVALS(1)(3)])
v = MAP(disk2D)(domain2D)
tronco = COLOR(colortronco)(PROD([v, Q(4)]))
alb = CYLINDER ([2,3])(3)
alb = COLOR(coloralbero)(MAP([S2,S3,S1])(alb))
albero = STRUCT([alb,T([1,2,3])([0,1.5,-5])(tronco)])
albero = T([1,2,3])([7,-5,5])(albero)
alberi = [T(1)(4), albero]
alberi = STRUCT(NN(3)(alberi))
alberiA = [T(2)(4), alberi]
'''-------------foresta alberi------------------ '''
foresta = T([1,2])([112,50])(STRUCT(NN(20)(alberiA)))
foresta1 = T([1,2])([100,-150])(STRUCT(NN(20)(alberiA)))
foresta3 = T([1,2])([-50,-150])(STRUCT(NN(20)(alberiA)))

castelloCompleto = STRUCT([foresta,foresta3,foresta1,collegamenti])
#############################################################
VIEW(castelloCompleto)