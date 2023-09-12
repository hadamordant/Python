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

if __name__=="__main__":
    lista = None
    lista = insertar(lista)
    visualizar(lista)
    lista = insertar(lista)
    visualizar(lista)
    lista = insertar(lista)
    visualizar(lista)
    lista = insertar(lista)
    visualizar(lista)
    print("extraer el elemento 3")
    lista = extraer(lista, 3)
    visualizar(lista)
