'''-------------------------------ESERCIZIO1--------------------------------------------'''
'''NOTE: tipo di struttura selta per l homework e' risultata abbastanza complessa per 
svolgere il secondo esercizio per cui sono stati realizzati in 2.5D i 4 modelli principali: nord, sud
est e west che non si e' riusciti a costruire un pianta unica in 3D . Inoltre il progetto scelto e'
 stato estremamente semplificato ripetto all'originale per la complessita' '''
from pyplasm import *

'''----colori------'''
color1 = Color4f([0.6, 0.3, 0.2])
color2 = Color4f([0.3, 0.6, 0.5])


'''-------scale-------'''
dom2D = PROD([INTERVALS(2*PI)(20), INTERVALS(1)(1)])
scale=SKELETON(1)(dom2D)
'''--------------'''
pavimento0 = CYLINDER ([20,0.1])(50)
pavimento1 = CYLINDER ([21,0.1])(50)
pavimento2 = STRUCT([pavimento0,pavimento1])
pavimento = T([1,2])([-.5,-1])(pavimento2)
pavimento = COLOR(color1)(SKELETON(1)(pavimento))


cortilecentralepieno1=SKELETON(1)(CYLINDER ([3.5,0])(8))
cortilecentralepieno2=SKELETON(1)(CYLINDER ([3,0])(8))
cortilecentrale2D = COLOR(GREEN)(STRUCT([cortilecentralepieno1,cortilecentralepieno2]))

'''colonne esterne'''
colonna1=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna1b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio1=COLOR(BLACK)((SKELETON(1)(CYLINDER([0.5,0])(50))))

esagono1 = STRUCT([colonna1b,colonna1,cerchio1])

colonna2=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna2b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio2=COLOR(BLACK)((SKELETON(1)(CYLINDER([0.5,0])(50))))
esagono2 = STRUCT([colonna2b,colonna2,cerchio2])

colonna3=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna3b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio3=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))

esagono3 = STRUCT([colonna3b,colonna3,cerchio3])

colonna4=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna4b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio4=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))

esagono4 = STRUCT([colonna4b,colonna4,cerchio4])

colonna5=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna5b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio5=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))

esagono5 = STRUCT([colonna5b,colonna5,cerchio5])


colonna6=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna6b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio6=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
esagono6 = STRUCT([colonna6b,colonna6,cerchio6])

'''-----------------------'''
colonna7=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna7b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio7=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
esagono7 = STRUCT([colonna7b,colonna7,cerchio7])


colonna8=SKELETON(1)(CYLINDER ([2.5,0])(8))
colonna8b=SKELETON(1)(CYLINDER ([2,0])(8))
cerchio8=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))

esagono8 = STRUCT([colonna8b,colonna8,cerchio8])

colonneesterne1 = STRUCT([T(1)(9)(esagono1)])
colonneesterne2 = STRUCT([T([1,2])([6.3,6.3])(esagono2)])
colonneesterne3 = STRUCT([T([1,2])([0.1,9])(esagono3)])
colonneesterne4 = STRUCT([T([1,2])([-6.09,6.5])(esagono4)])
colonneesterne5 = STRUCT([T([1,2])([-8.9,0.1])(esagono5)])
colonneesterne6 = STRUCT([T([1,2])([-6.2,-6.5])(esagono6)])
colonneesterne7 = STRUCT([T([1,2])([0.1,-9])(esagono7)])
colonneesterne8 = STRUCT([T([1,2])([6.5,-6.2])(esagono8)])

colonneesterne = COLOR(RED)(STRUCT([colonneesterne1,colonneesterne2,
	colonneesterne3,colonneesterne4,colonneesterne5,
	colonneesterne6,colonneesterne7,colonneesterne8]))
'''---------------internocolonne--------------------------------'''
spaziosale=SKELETON(1)(CYLINDER ([7,0])(8))
spaziosale1b=SKELETON(1)(CYLINDER ([6.5,0])(8))
salespazio = STRUCT([spaziosale,spaziosale1b])

'''--------collegamenti tra colonne interne ed esterne----------'''
piano0 = STRUCT([cortilecentrale2D,salespazio,colonneesterne1,colonneesterne])
#VIEW(STRUCT([piano0]))

'''two_and_half_model'''
scala=COLOR(color2)(ROTATE([1,2])(7.5)(scale))
two_and_half_model = STRUCT([piano0,pavimento,T([1,2])([3.5,7])(scala)])
VIEW(two_and_half_model)
