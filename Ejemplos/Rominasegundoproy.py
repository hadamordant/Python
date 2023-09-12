#1-Referente a la Pila
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

#2- Referente a la Cola
class Cola:
    #Constructor
    def __init__(self, num):
        self.num = num
        self.siguiente = None
        self.anterior = None

#Recorrer la cola desde el primero hasta el ultimo
def visualizar(cola):
    aux = cola
    while aux != None:
        print(aux.num)
        aux = aux.siguiente

#Insertar nuevo elemento
def insertar(primero, ultimo):
    num = int(input("Valor a insertar: "))
    nuevo = Cola(num)
    #si la cola esta vacia...
    if primero == None:
        #el nuevo elemento sera primero y ultimo a la vez
        primero = nuevo
        ultimo = nuevo
    else:
        #a partir del segundo elemento que se inserte, cada elemento insertado
        #pasará a ser el último
        ultimo.siguiente = nuevo
        nuevo.anterior = ultimo
        ultimo = nuevo

    #retornar los mismos parametros recibidos es una forma de implementar el paso por referencia        
    return primero, ultimo

#Al extraer de una cola, siempre se extrae el primer elemento
def extraer(primero, ultimo):
    if primero != None:
        primero = primero.siguiente
        if primero != None:
            primero.anterior = None
    return primero, ultimo

#3- Referente a la Lista
class Lista:
    #Constructor
    def __init__(self, num):
        self.num = num
        self.siguiente = None

#Insertar en la lista
def insertar(lista):
    num = int(input("valor a insertar: "))
    nuevo = Lista(num)
    #Si la lista esta vacia...
    if lista==None:
        #la cabecera es el nuevo elemento
        lista = nuevo        
    else:
        if lista.num > nuevo.num:
            nuevo.siguiente = lista
            lista = nuevo
        else:            
            aux = lista
            encontrado = False
            nodo = None
            while aux.siguiente != None and not encontrado:
                nodo = aux
                if aux.siguiente.num > nuevo.num:
                    encontrado = True                
                aux = aux.siguiente
            if encontrado:
                if nodo != None:
                    nodo.siguiente = nuevo
                    nuevo.siguiente = aux
                else:
                    aux.siguiente = nuevo
            else:
                aux.siguiente = nuevo
                
    return lista

#Recorrer la lista
def visualizar(lista):
    aux=lista
    while aux!=None:
        print(aux.num)
        aux=aux.siguiente

#eliminar un elemento buscado en la lista
def extraer(lista, num):
    aux = lista
    encontrado = False
    nodo = None
    #si el elemento a buscar se encuentra en la cabecera
    if lista.num == num:
        lista = lista.siguiente
        return lista
    #si no se encuentra en la cabecera
    while aux.siguiente != None and not encontrado:
        #almacenar el elemento anterior al buscado
        nodo = aux
        #si se encuentra el elemento buscado
        if aux.siguiente.num == num:
            encontrado = True
            
        #aqui se desplaza al siguiente elemento de la lista
        aux = aux.siguiente

        
    if encontrado:
        #validar que el elemento encontrado no este vacio
        if aux != None:            
            nodo.siguiente = aux.siguiente
            aux = None        
        
    return lista

#cuerpo principal del programa
if __name__ == '__main__':
    print("         SISTEMA DE PILAS Y COLAS (NO LAS QUE HACES PARA COMPRAR EN LOS SUPERMERCADOS)       ")
    print("               "    )
    print("                 Romina Betancourt, Algoritmos y Estructuras II                             ")
    print()
    print("-----------------------------------------------------------------")
    x = input ("""Eliga una de las siguientes actividades:
    (1) Trabajar con Pilas
    (2) Trabajar con Colas
    (3) Trabajar con Listas

    Opcion: """)


    if x == "1":
        #inicializar el primer y el ultimo elemento como vacio
        pila = None
        primero = None
        ultimo = None
        i=1
        for i in range(1,5):
            visualizar(pila)
            pila = insertar(pila)
        print("----------")
        print("--Se extrae el primer elemento de la pila--")
        visualizar(pila)

    elif x == "2":
        #inicializar el primer y el ultimo elemento como vacio
        primero = None
        ultimo = None
        i=1
        #ciclo para insertar elementos
        for i in range(1,5):
            visualizar(primero)
            cola = insertar(primero)
        y = input ("""Ahora se extraeran elementos para insertarse en pilas y listas, escoja sólo una:
           (1) Extraer Primer Elemento
           (2) Extraer Segundo Elemento
           (3) Extraer Tercero Elemento
           (4) Extraer Cuarto Elemento
           (5) No Extraer Ningún Elemento
        Opcion: """)
        if y == "1":
            print("Extraer el elemento 1")
            primero = extraer(1, ultimo)
            visualizar(primero)
        elif y == "2":
            print("Extraer el elemento 2")
            primero = extraer(2, ultimo)
            visualizar(primero)
        elif y == "3":
            print("Extraer el elemento 3")
            primero = extraer(3, ultimo)
            visualizar(primero)
        elif y == "4":
            print("Extraer el elemento 4")
            primero = extraer(4, ultimo)
            visualizar(primero)
        elif y == "5":
            print("No Extraer Ningún Elemento")
            visualizar(primero)

    elif x == "3":
        lista = None
        i=1
        for i in range(1,5):
            lista = insertar(lista)
            visualizar(lista)
        y = input ("""Ahora se extraeran elementos para insertarse en pilas y colas, escoja sólo una:
           (1) Extraer Primer Elemento
           (2) Extraer Segundo Elemento
           (3) Extraer Tercero Elemento
           (4) Extraer Cuarto Elemento
           (5) No Extraer Ningún Elemento
        Opcion: """)
        if y == "1":
            print("Extraer el elemento 1")
            lista = extraer(lista, 1)
            visualizar(lista)
        elif y == "2":
            print("Extraer el elemento 2")
            lista = extraer(lista, 3)
            visualizar(lista)
        elif y == "3":
            print("Extraer el elemento 3")
            lista = extraer(lista, 3)
            visualizar(lista)
        elif y == "4":
            print("Extraer el elemento 4")
            lista = extraer(lista, 4)
            visualizar(lista)
        elif y == "5":
            print("No Extraer Ningún Elemento")
            visualizar(lista)

    else:
        input("por favor ingrese una opcion valida: 1, 2, 3 ò 4")

    input()
