#Ordenamiento por Seleccion
def selectionSort(V):
    n = len(V)    
    for i in range(n-1):
        minimo = i
        for j in range(i+1, n):
            #La diferencia con respecto a Bubble Sort es que el intercambio
            #no se realiza aca, sino que se almacena la posicion del menor
            if V[j["cedula"]]< V[minimo]["cedula"]:
                minimo = j
        #Al finalizar el ciclo de "j" se realiza el intercambio
        temp = V[minimo]
        V[minimo] = V[i]
        V[i] = temp

if __name__ == "__main__":
     #Inicializar arreglo vacio
    Registros = []
    V = []
    #inicializar diccionario1
    Nuevo = {}
    #llenar cada uno de los campos del diccionario
    Nuevo["cedula"] = 2
    Nuevo["nombre"] = "Romina"
    Nuevo["apellido"] = "Betancourt"
    Registros.append(Nuevo)

    #inicializar diccionario3
    Nuevo = {}
    #llenar cada uno de los campos del diccionario
    Nuevo["cedula"] = 1
    Nuevo["nombre"] = "Xiomara"
    Nuevo["apellido"] = "Rodríguez"
    
    Registros.append(Nuevo)
    
    for Nuevo in Registros:
        
        print("Cedula: ", Nuevo["cedula"])
        print("Nombre: ", Nuevo["nombre"])
        print("Apellido: ", Nuevo["apellido"])
        print("Compra de Productos:")
    print()
    
   

