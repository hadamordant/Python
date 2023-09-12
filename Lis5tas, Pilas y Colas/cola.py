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

#cuerpo principal del programa
if __name__ == "__main__":
    #inicializar el primer y el ultimo elemento como vacio
    primero = None
    ultimo = None
    i=1
    #ciclo para insertar elementos
    for i in range(1,4):
        [primero , ultimo] = insertar(primero, ultimo)
        i=i+1
    
    print("Extraer un elemento")
    [primero, ultimo] = extraer(primero, ultimo)
    visualizar(primero)
    
    
