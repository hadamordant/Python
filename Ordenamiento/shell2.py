def shellSort(Nuevo):
    n = len(V)
    for i in range(n):
        temp = V[i]["cedula"]
        j = i-1
        b = False
        #Comparar con todos los elementos anteriores
        #o hasta conseguir un elemento mayor que el auxiliar
        #(en este caso, que el ordenamiento es ascendente)
        while b == False and j >= 0:
            if temp < V[j]["cedula"]:
                #Desplazar los elementos
                V[j+1] = V[j]
                j = j-1
            else:
                b = True
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
    
    shellSort(Nuevo)
    for registro in Registros:
        print("Cedula: ", registro["cedula"])
        print("Nombre: ", registro["nombre"])
        print("Apellido: ", registro["apellido"])
        print("Compra de Productos:")
    print()
