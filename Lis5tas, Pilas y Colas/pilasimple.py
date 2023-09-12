class Pila:
    #Constructor
    def __init__(self, num):
        self.num = num
        self.siguiente = None

#Recorrer la pila
def visualizar(pila):
    aux=pila
    while aux!=None:
        print(aux.num)
        aux=aux.siguiente

#Insertar un nuevo elemento en la pila
def insertar(pila):
    num = int(input("valor a insertar: "))
    nuevo = Pila(num)
    #Si la pila esta vacia...
    if pila == None:
        #El elemento nuevo se asigna directamente como cabecera
        pila = nuevo
    else:
        #sino, el elemento nuevo desplaza a la cabecera
        nuevo.siguiente = pila
        pila = nuevo
    return pila

#Al extraer de la pila, se extrae el primer elemento
def extraer(pila):
    if pila != None:
        aux = pila.siguiente
        del(pila)
        pila = aux
    return pila

if __name__ == "__main__":
    pila = None
    pila = insertar(pila)
    print("----------")
    visualizar(pila)
    pila = insertar(pila)
    print("----------")
    visualizar(pila)
    pila = insertar(pila)
    print("----------")
    visualizar(pila)
    pila = insertar(pila)
    print("----------")
    visualizar(pila)
    pila = extraer(pila)
    print("--Se extrae un elemento de la pila--")
    visualizar(pila)
    
