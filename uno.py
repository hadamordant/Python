import os

crtms4  = 4   # Identifica la carta de tipo +4
crtsrep = 7   # Cantidad de cartas a repartir por jugador
ct      = 108 # Cantidad de cartas totales del juego
crest   = 0   # Cantidad de cartas restantes en el juego
za=1
zb=1
z=1
zm=1
colores = 4

print (" Juego de cartas UNO")

pj= input('comprobar teoria de conteo (s/n): ')

os.system('cls')

while pj == 's':
    nj=int(input('Indicar la cantidad de jugadores a validar (de 2 a 10): '))
    if (nj>=2) and (nj<=10):
        cnj = int( nj / 2)

        print ("\n Menu de Opciones del 1 al 5\n") 
        print ("1)Numero de formas distintas de distribucion de las (2) cartas (+2) Azul, (2) pierde el  turno amarilla o 2 cambio de sentido de cada color ") 
        print ("2)Numero de formas diferentes de salir las (4) cartas (+4) durante el juego solo a:",cnj ,"jugadores de", nj )
        print ("3)posibles distintas formas de posiciones de ganaadore  para ", nj ,"jugadores ")
        print ("4)Numero de Variaciones de los 3 primeros puestos de ganadores (Solo cuando hay mas de 3 jugadores) ")
		
        preg = int(input('indique el numero de su opcion : '))
        if preg == 1 :
            ca = 2*2
            cb= 2 * colores
            c = ca + cb
            print (" EL Numero de combinaciones posibles de las (2) cartas (+2) Azul, (2) pierde el  turno amarilla o 2 cambio de sentido de cada color es : ", c ) 
        if preg == 2 :
            pfs = crtms4 * cnj
            print ("la Probabilidad de que ha ",cnj , "jugadores le salgan las (4) cartas (+4) es: ", pfs)
        if  preg == 3:
            ##zb=1
            while z <= nj:
                zb = zb * z
                z = z + 1
            print ("posibles distintas formas de pociciones de ganadores  segun #jugador : ", zb)
        if preg == 4 :
            k = nj - 3
            if nj >= 3:
                if nj == 3:
                    while z <= nj:
                        za = za * z
                        z = z + 1
                elif nj == 4:
                    za = 4*3
                elif nj > 4:
                    while nj > k:
                        za= za * nj
                        nj = nj - 1
                        
                print ("el Numero de Variaciones de los 3 primeros es de: ", za)    
            else :
                print ("el Numero de jugadores es menor a 3  (debe ser min 3 jugadores): ")  
				
    else:
        print ("La cantidad de jugadores debe ser de 2 a 10")
		
    pj= input('comprobar teoria de conteo (s/n): ')
    za=1
