'''---------------------------------------------------------------------------'''
'''NOTE: tipo di struttura selta per l homework e' risultata abbastanza complessa in 
quanto sono necessarie rotazioni su misura per cui il primo e di conseguenza anche 
gli  altri esercizi sono stati realizzati con il grande sfrozo di far combaciare le
metriche senza alcun risultato'''
'''-------------------------HOMEWORK:ESERCIZIO2-------------------------------'''
'''Define, with names north, south, east, and west, at least 4 models 2D of 
vertical enclosures (including the hollows), and add them (by embedding in the 
	appropriate vertical planes) to the STRUCT of the 2.5D two_and_half_model producing
a single mock_up_3D assembly.'''
from pyplasm import *
'''----colori------'''
colornord = Color4f([0.6, 0.5, 0.2])
colorsud = Color4f([0.1, 0.2, 0.4])
colorest= Color4f([0.7, 0.7, 0.7])
colorwest= Color4f([0.7, 0.7, 0.7])
colore1 = Color4f([0.2, 0.2, 0.5])
colore2 = Color4f([0.8, 0.7, 0.9])
colore3 = Color4f([0.9, 0.7, 0.2])
colore4 = Color4f([0.6, 0.5, 0.2])
colorporta = Color4f([0.1, 0.9, 0.9])
colortriangolo =  Color4f([0.9, 0.3, 0.7])
colorepavimento =  Color4f([0.5, 1, 0.5])
colorecortile = Color4f([1, 0.8, 0.7])
coloreColonne =  Color4f([1, 0.8, 0.7])


'''--------------'''

pavimento0=QUOTE([20,20])
pavimento0a=QUOTE([20,20])
p=INSR(PROD)([pavimento0,pavimento0a,Q(0.6)])
pavimento = COLOR(colorepavimento)(T([1,2])([-20,-20])(p))

cortilecentralepieno1=CYLINDER ([3.5,8])(8)
cortilecentralepieno2=CYLINDER ([3,8])(8)
cortilecentrale2D = COLOR(GREEN)(STRUCT([cortilecentralepieno1,cortilecentralepieno2]))
'''colonne esterne'''
colonna1=CYLINDER ([2.5,9])(8)
colonna1b=CYLINDER ([2,9])(8)
cerchio1=COLOR(BLACK)((SKELETON(1)(CYLINDER([0.5,0])(50))))
plinto1=CYLINDER ([3,1])(8)

esagono1 = STRUCT([colonna1b,colonna1,cerchio1,plinto1])

colonna2=CYLINDER ([2.5,9])(8)
colonna2b=CYLINDER ([2,9])(8)
cerchio2=COLOR(BLACK)((SKELETON(1)(CYLINDER([0.5,0])(50))))
plinto2=CYLINDER ([3,1])(8)

esagono2 = STRUCT([colonna2b,colonna2,cerchio2,plinto2])

colonna3=CYLINDER ([2.5,9])(8)
colonna3b=CYLINDER ([2,9])(8)
cerchio3=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto3=CYLINDER ([3,1])(8)

esagono3 = STRUCT([colonna3b,colonna3,cerchio3,plinto3])

colonna4=CYLINDER ([2.5,9])(8)
colonna4b=CYLINDER ([2,9])(8)
cerchio4=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto4=CYLINDER ([3,1])(8)

esagono4 = STRUCT([colonna4b,colonna4,cerchio4,plinto4])

colonna5=CYLINDER ([2.5,9])(8)
colonna5b=CYLINDER ([2,9])(8)
cerchio5=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto5=CYLINDER ([3,1])(8)

esagono5 = STRUCT([colonna5b,colonna5,cerchio5,plinto5])


colonna6=CYLINDER ([2.5,9])(8)
colonna6b=CYLINDER ([2,9])(8)
cerchio6=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto6=CYLINDER ([3,1])(8)

esagono6 = STRUCT([colonna6b,colonna6,cerchio6,plinto6])

colonna7=CYLINDER ([2.5,9])(8)
colonna7b=CYLINDER ([2,9])(8)
cerchio7=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto7=CYLINDER ([3,1])(8)

esagono7 = STRUCT([colonna7b,colonna7,cerchio7,plinto7])


colonna8=CYLINDER ([2.5,9])(8)
colonna8b=CYLINDER ([2,9])(8)
cerchio8=COLOR(BLACK)(SKELETON(1)(CYLINDER([0.5,0])(50)))
plinto8=CYLINDER ([3,1])(8)

esagono8 = STRUCT([colonna8b,colonna8,cerchio8,plinto8])


colonneesterne1 = STRUCT([T(1)(9)(esagono1)])
colonneesterne2 = STRUCT([T([1,2])([6.3,6.3])(esagono2)])
colonneesterne3 = STRUCT([T([1,2])([0.1,9])(esagono3)])
colonneesterne4 = STRUCT([T([1,2])([-6.09,6.5])(esagono4)])
colonneesterne5 = STRUCT([T([1,2])([-8.9,0.1])(esagono5)])
colonneesterne6 = STRUCT([T([1,2])([-6.2,-6.5])(esagono6)])
colonneesterne7 = STRUCT([T([1,2])([0.1,-9])(esagono7)])
colonneesterne8 = STRUCT([T([1,2])([6.5,-6.2])(esagono8)])


colonneesterne = COLOR(coloreColonne)(STRUCT([colonneesterne1,colonneesterne2,
	colonneesterne3,colonneesterne4,colonneesterne5,
	colonneesterne6,colonneesterne7,colonneesterne8]))
'''---------------internocolonne--------------------------------'''
spaziosale=CYLINDER ([7,8])(8)
spaziosale1b=CYLINDER ([6.5,8])(8)
salespazio = STRUCT([spaziosale,spaziosale1b])
cortile=COLOR(colorecortile)(DIFFERENCE([salespazio, cortilecentrale2D]))
'''--------collegamenti tra colonne interne ed esterne----------'''
piano0 = STRUCT([cortile,colonneesterne1,colonneesterne,cortile])
piano1 = piano0
#VIEW(STRUCT([piano0,pavimento]))

'''------------------------------nord---------------------------------'''

vistaFronte1 = [[0,0],[0,12],[1,16],[2,16],[3,12],[3,0]]
fronte1 = SKELETON(1)(JOIN(AA(MK)(vistaFronte1)))
vistaFronte2 = [[6,0],[6,10],[6,12],[7,16],[8,16],[9,12],[9,0]]
fronte2 = SKELETON(1)(JOIN(AA(MK)(vistaFronte2)))
vistaFronte3 = [[3,0],[3,6],[6,6],[6.0]]
fronte3 = SKELETON(1)(JOIN(AA(MK)(vistaFronte3)))
#arco triangolo
vistaFronte4 = [[3,4],[4.5,6],[6,4]]
fronte4 = COLOR(colortriangolo)(SKELETON(1)(JOIN(AA(MK)(vistaFronte4))))
#porta
door = SKELETON(1)(COLOR(colorporta)(CUBOID([1,3])))
#colonne fronte
vistaFronte5 = [[7,0],[7,8]]
fronte5 = SKELETON(1)(JOIN(AA(MK)(vistaFronte5)))

vistaFronte6 = [[8,0],[8,8]]
fronte6 = SKELETON(1)(JOIN(AA(MK)(vistaFronte6)))

vistaFronte7 = [[1,0],[1,8]]
fronte7 = SKELETON(1)(JOIN(AA(MK)(vistaFronte7)))

vistaFronte8 = [[2,0],[2,8]]
fronte8 = SKELETON(1)(JOIN(AA(MK)(vistaFronte8)))


prospettiva1 = [[0,0],[0,6],[0,6],[-.5,7],[-1,7],[-2,6],[-2,0],[0,0]]
prospettiva1a = SKELETON(1)(JOIN(AA(MK)(prospettiva1)))

prospettiva2 = [[0,0],[0,6],[0,6],[-.5,7],[-1,7],[-2,6],[-2,0],[0,0]]
prospettiva2a = SKELETON(1)(JOIN(AA(MK)(prospettiva2)))
prospettiva2a=T(1)(11)(prospettiva2a)
nord = COLOR(colornord)(STRUCT([fronte1,fronte2,fronte3,fronte4,
fronte5,fronte6,fronte7,fronte8, prospettiva1a,T(1)(4)(door),
prospettiva2a]))
'''------------------------------sud---------------------------------'''


vistaFronte1S = [[0,0],[0,6],[1,8],[2,8],[3,6],[3,0]]
fronte1S = SKELETON(1)(JOIN(AA(MK)(vistaFronte1S)))
vistaFronte2S = [[6,0],[6,5],[6,6],[7,8],[8,8],[9,6],[9,0]]
fronte2S = SKELETON(1)(JOIN(AA(MK)(vistaFronte2S)))
vistaFronte3S = [[3,0],[3,6],[6,6],[6.0]]
fronte3S = SKELETON(1)(JOIN(AA(MK)(vistaFronte3S)))
#colonne fronte
vistaFronte5S = [[7,0],[7,8]]
fronte5S = SKELETON(1)(JOIN(AA(MK)(vistaFronte5S)))

vistaFronte6S = [[8,0],[8,8]]
fronte6S = SKELETON(1)(JOIN(AA(MK)(vistaFronte6S)))

vistaFronte7S = [[1,0],[1,8]]
fronte7S = SKELETON(1)(JOIN(AA(MK)(vistaFronte7S)))

vistaFronte8S = [[2,0],[2,8]]
fronte8S = SKELETON(1)(JOIN(AA(MK)(vistaFronte8S)))

sud = COLOR(colorsud)(STRUCT([fronte1S,fronte2S,fronte3S,
fronte5S,fronte6S,fronte7S,fronte8S]))
#VIEW(sud)

'''------------------------------est---------------------------------'''


vistaFronte1E = [[0,0],[0,6],[1,8],[2,8],[3,6],[3,0]]
fronte1E = SKELETON(1)(JOIN(AA(MK)(vistaFronte1E)))
vistaFronte2E = [[6,0],[6,5],[6,6],[7,8],[8,8],[9,6],[9,0]]
fronte2E = SKELETON(1)(JOIN(AA(MK)(vistaFronte2E)))
vistaFronte3E = [[3,0],[3,6],[6,6],[6.0]]
fronte3E = SKELETON(1)(JOIN(AA(MK)(vistaFronte3E)))
#colonne fronte
vistaFronte5E = [[7,0],[7,8]]
fronte5E = SKELETON(1)(JOIN(AA(MK)(vistaFronte5E)))

vistaFronte6E = [[8,0],[8,8]]
fronte6E = SKELETON(1)(JOIN(AA(MK)(vistaFronte6E)))

vistaFronte7E = [[1,0],[1,8]]
fronte7E = SKELETON(1)(JOIN(AA(MK)(vistaFronte7E)))

vistaFronte8E = [[2,0],[2,8]]
fronte8E = SKELETON(1)(JOIN(AA(MK)(vistaFronte8E)))

est = COLOR(colorest)(STRUCT([fronte1E,fronte2E,fronte3E,
fronte5E,fronte6E,fronte7E,fronte8E]))
#VIEW(est)
'''------------------------------west---------------------------------'''


vistaFronte1W = [[0,0],[0,6],[1,8],[2,8],[3,6],[3,0]]
fronte1W = SKELETON(1)(JOIN(AA(MK)(vistaFronte1W)))
vistaFronte2W = [[6,0],[6,5],[6,6],[7,8],[8,8],[9,6],[9,0]]
fronte2W = SKELETON(1)(JOIN(AA(MK)(vistaFronte2W)))
vistaFronte3W = [[3,0],[3,6],[6,6],[6.0]]
fronte3W = SKELETON(1)(JOIN(AA(MK)(vistaFronte3W)))
#colonne fronte
vistaFronte5W = [[7,0],[7,8]]
fronte5W = SKELETON(1)(JOIN(AA(MK)(vistaFronte5W)))

vistaFronte6W = [[8,0],[8,8]]
fronte6W = SKELETON(1)(JOIN(AA(MK)(vistaFronte6W)))

vistaFronte7W = [[1,0],[1,8]]
fronte7W = SKELETON(1)(JOIN(AA(MK)(vistaFronte7W)))

vistaFronte8W = [[2,0],[2,8]]
fronte8W = SKELETON(1)(JOIN(AA(MK)(vistaFronte8W)))

west = COLOR(colorwest)(STRUCT([fronte1W,fronte2W,fronte3W,
fronte5W,fronte6W,fronte7W,fronte8W]))
#VIEW(west)

'''two_and_half_model'''
piani = STRUCT([piano0,T(3)(8)(piano1)])
davanti=STRUCT([piani,nord,sud])

#porto la y su z
nord1 = T(1)(1.5)(PROD([nord, Q(1)]))
nord=T([1,2])([10,10])(MAP([S1,S3,S2])(nord1))
# c = T([1,2,3])([5,5,0])(a)
# d=ROTATE([1,2])(2)(c)
sud1 = T(1)(1.5)(PROD([sud, Q(1)]))
sud = T([1,2])([20,20])(MAP([S1,S3,S2])(sud1))
#porto la y su z
est1 = T(1)(1.5)(PROD([est, Q(1)]))
est = T([1,2])([30,-20])(MAP([S1,S3,S2])(est1))
#porto la y su z
west1 = T(1)(1.5)(PROD([west, Q(1)]))
west = T([1,2])([-20,-20])(MAP([S1,S3,S2])(west1))

#porto la y su z
latiEsagono1 = T(1)(1.5)(PROD([west1, Q(1)]))
copriStruttura1 = T([1,2])([-10,-20])(MAP([S1,S3,S2])(latiEsagono1))

latiEsagono2 = T(1)(1.5)(PROD([west1, Q(1)]))
copriStruttura2 = T([1,2])([-10,-10])(MAP([S1,S3,S2])(latiEsagono2))
latiEsagono3 = T(1)(1.5)(PROD([west1, Q(1)]))
copriStruttura3 = T([1,2])([-20,-10])(MAP([S1,S3,S2])(latiEsagono3))
mock_up_3D = STRUCT([piano0,pavimento])
mock_up_3D=SKELETON(1)(mock_up_3D)
VIEW(mock_up_3D)
