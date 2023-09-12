#Para utilizar numeros aleatorios
from random import randrange

#subprograma que determina el maximo valor en un arreglo, y su posicion
def maximo(V):
    #maximo valor
    valor = V[0]
    #posicion
    p = 0
    #la funcion len() determina la longitud de un arreglo
    n = len(V)
    for i in range(n):
        if V[i] > valor:            
            valor = V[i]
            p = i
    #retornar 2 valores
    return valor, p
if __name__ == '__main__':
    #Ingresar valor de "n" por teclado, y convertirlo a entero
    #ya que input() por defecto retorna una cadena
    n = int(input('Longitud del arreglo: '))
    V = []
    for i in range(n):
        num = randrange(0, 100)
        V.append(num)
    [valor, p] = maximo(V)
    print("Recorrido usando: for i in range(n)")
    for i in range(n):
        print(V[i], end=" ")
    print()
    print("Recorrido usando: for item in V")
    for item in V:
        print(item, end=" ")
    print()
    print("Maximo valor: %i"%(valor), "Posicion: %i"%(p+1), sep="\n")
