def insertionSort(V):
    n = len(V)
    #A partir del segundo elemento
    for i in range(1, n):
        temp = V[i]
        j=i-1
        #Se compara con todos los anteriores
        while j>=0 and V[j]>temp:
            #Desplazar los elementos del arreglo
            V[j+1] = V[j]
            j = j-1

        V[j+1] = temp

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
    
    for V in Registros:
        
        print("Cedula: ", V["cedula"])
        print("Nombre: ", V["nombre"])
        print("Apellido: ", V["apellido"])
        print("Compra de Productos:")
    print()
