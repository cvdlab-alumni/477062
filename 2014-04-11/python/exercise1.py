'''-------------------------------HOMEWORK2-ESERCIZIO1--------------------------------------------'''
'''NOTE: non sono disegnate tutte le finestre del progetto originale in quanto
i tempi di elaborazione sono notevoli '''
'''----------------------------------------------------------------------------------'''

from pyplasm import *
#######################################################################
'''----colori------'''
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]
#######################################################################
colorePratointorno = rgb([190, 237, 174])
coloreStradaesterna = rgb([116,119,114])
colorporta = rgb([178, 231, 137])
colorEdificio = rgb([216, 180, 141])
colortriangolo =  Color4f([0.9, 0.3, 0.7])
colorecortile = Color4f([1, 0.8, 0.7])
coloreColonne =  Color4f([1, 0.8, 0.7])
#######################################################################
pavimentoa = CYLINDER ([20,0.1])(50)
pavimento = COLOR(coloreColonne)(T([1,2])([-.5,-1])(pavimentoa))
cortilecentralepieno1=CYLINDER ([3.5,8])(8)
cortilecentralepieno2=CYLINDER ([3,8])(8)
cortilecentrale2D = STRUCT([cortilecentralepieno1,cortilecentralepieno2])
'''--------------------------ambiente----------------------------------------'''
#######################################################################
#######################################################################
pavimentob = CYLINDER ([30,0.1])(50)
pavimento1 = COLOR(GREEN)(T([1,2])([-.5,-1])(pavimentob))
a = STRUCT([pavimento,pavimento1])
stradaEsterna = COLOR(coloreStradaesterna)(DIFFERENCE([a,pavimento]))

pavimentoc = CYLINDER ([15,0.1])(50)
base2 = T([1,2])([-.5,-1])(pavimentoc)

pavimentod = CYLINDER ([5,0.1])(50)
base3 = T([1,2])([-.5,-1])(pavimentod)
stradaEsterna1 = COLOR(colorePratointorno)(DIFFERENCE([base2,base3]))
############################sabbia###########################################
############################sabbia###########################################
baseNera = T([1,2])([-.4,-.2])(COLOR(RED)(CYLINDER ([5.8,.1])(30)))
############################sabbia###########################################
############################sabbia###########################################

p1 = CYLINDER ([25,0.1])(50)
pa1 = T([1,2])([-.5,-1])(p1)

p2 = CYLINDER ([15,0.1])(50)
pa2 = T([1,2])([-.5,-1])(p2)
stradaEsterna2 = COLOR(colorecortile)(DIFFERENCE([pa1,pa2]))
intornoCastello = STRUCT([stradaEsterna,stradaEsterna1,stradaEsterna2,baseNera])
#######################################################################
#######################################################################
#######################################################################
'''------------------------------------------------------------------'''
#######################################################################
'''colonne esterne'''
'''colonna n 1 esterna con plinto'''
#######################################################################
colonna1=CYLINDER ([2,9])(8)
colonna1b=CYLINDER ([1,9])(8)
cerchio1=COLOR(BLACK)((SKELETON(1)(CYLINDER([0.5,0])(50))))
plinto1=CYLINDER ([2.3,.5])(8)

esagono1 = STRUCT([colonna1b,colonna1,cerchio1,plinto1])
#######################################################################
'''colonna n 2 esterna con plinto'''
#######################################################################

colonna2=CYLINDER ([2,9])(8)
colonna2b=CYLINDER ([1,9])(8)
cerchio2=COLOR(BLACK)((SKELETON(1)(CYLINDER([0.5,0])(50))))
plinto2=CYLINDER ([2.3,.5])(8)

esagono2 = STRUCT([colonna2b,colonna2,cerchio2,plinto2])
#######################################################################
'''colonna n 3 esterna con plinto'''
#######################################################################
colonna3=CYLINDER ([2,9])(8)
colonna3b=CYLINDER ([1,9])(8)
cerchio3=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto3=CYLINDER ([2.3,.5])(8)

esagono3 = STRUCT([colonna3b,colonna3,cerchio3,plinto3])
#######################################################################
'''colonna n 4 esterna con plinto'''
#######################################################################

colonna4=CYLINDER ([2,9])(8)
colonna4b=CYLINDER ([1,9])(8)
cerchio4=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto4=CYLINDER ([2.3,.5])(8)

esagono4 = STRUCT([colonna4b,colonna4,cerchio4,plinto4])

#######################################################################
'''colonna n 5 esterna con plinto'''
#######################################################################

colonna5=CYLINDER ([2,9])(8)
colonna5b=CYLINDER ([1,9])(8)
cerchio5=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto5=CYLINDER ([2.3,.5])(8)

esagono5 = STRUCT([colonna5b,colonna5,cerchio5,plinto5])

#######################################################################
'''colonna n 6 esterna con plinto'''
#######################################################################

colonna6=CYLINDER ([2,9])(8)
colonna6b=CYLINDER ([1,9])(8)
cerchio6=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto6=CYLINDER ([2.3,.5])(8)

esagono6 = STRUCT([colonna6b,colonna6,cerchio6,plinto6])

#######################################################################
'''colonna n 7 esterna con plinto'''
#######################################################################
colonna7=CYLINDER ([2,9])(8)
colonna7b=CYLINDER ([1,9])(8)
cerchio7=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto7=CYLINDER ([2.3,.5])(8)

esagono7 = STRUCT([colonna7b,colonna7,cerchio7,plinto7])

#######################################################################
'''colonna n 8 esterna con plinto'''
#######################################################################
colonna8=CYLINDER ([2,9])(8)
colonna8b=CYLINDER ([1,9])(8)
cerchio8=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto8=CYLINDER ([2.3,.5])(8)

esagono8 = STRUCT([colonna8b,colonna8,cerchio8,plinto8])

#######################################################################
'''traslo le colonne esterne sulle posizioni corrette del building'''
#######################################################################
colonneesterne1 = STRUCT([T(1)(9)(esagono1)])
colonneesterne2 = STRUCT([T([1,2])([6.3,6.3])(esagono2)])
colonneesterne3 = STRUCT([T([1,2])([0.1,9])(esagono3)])
colonneesterne4 = STRUCT([T([1,2])([-6.09,6.5])(esagono4)])
colonneesterne5 = STRUCT([T([1,2])([-8.9,0.1])(esagono5)])
colonneesterne6 = STRUCT([T([1,2])([-6.2,-6.5])(esagono6)])
colonneesterne7 = STRUCT([T([1,2])([0.1,-9])(esagono7)])
colonneesterne8 = STRUCT([T([1,2])([6.5,-6.2])(esagono8)])

colonneesterne = STRUCT([colonneesterne1,colonneesterne2,
	colonneesterne3,colonneesterne4,colonneesterne5,
	colonneesterne6,colonneesterne7,colonneesterne8])
#######################################################################
'''---------------internocolonne--------------------------------'''
#######################################################################
spaziosale=CYLINDER ([7,8])(8)
spaziosale1b=CYLINDER ([6.5,8])(8)
salespazio = STRUCT([spaziosale,spaziosale1b])
cortile=COLOR(colorecortile)(DIFFERENCE([salespazio, cortilecentrale2D]))
cortilepiano1=COLOR(colorecortile)(DIFFERENCE([salespazio, cortilecentrale2D]))
######################################################################

'''--------collegamenti tra colonne interne ed esterne----------'''
#######################################################################
piano0 = COLOR(colorEdificio)(STRUCT([cortilecentrale2D,colonneesterne,colonneesterne]))
piano1 = COLOR(colorEdificio)(STRUCT([cortilecentrale2D,colonneesterne1,colonneesterne]))
#######################################################################
#######################################################################
'''------definisco scale--------'''
#######################################################################
a = 0.5 
b = 3.2/15
p = [[0,0],[a,0.2],[a,0.1+b],[0,0.1+a]];
c = [[1,2,3,4]];
sca = MKPOL([p,c,None]);
sca1 = PROD([sca,Q(1)]);
sca2 = STRUCT(NN(14)([sca1,T([1,2])([a,b])]));
sca3 = MAP([S3,S1,S2])(sca2);
# sca4 = T([1,2,3])([0.5,2.3,-0.2])(sca3);
sca4 = T([1,2,3])([0.5,2.2,-0.2])(sca3);
scala=COLOR(colorEdificio)(ROTATE([1,2])(3)(sca4))

solid_model_3D = SKELETON(1)(STRUCT([piano0,T(3)(9)(piano1),intornoCastello,
	T([1,2])([5,15])(scala)]))
#VIEW(solid_model_3D)

