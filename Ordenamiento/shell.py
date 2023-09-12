def shellSort(V):
    n = len(V)
    for i in range(n):
        temp = V[i]
        j = i-1
        b = False
        #Comparar con todos los elementos anteriores
        #o hasta conseguir un elemento mayor que el auxiliar
        #(en este caso, que el ordenamiento es ascendente)
        while b == False and j >= 0:
            if temp < V[j]:
                #Desplazar los elementos
                V[j+1] = V[j]
                j = j-1
            else:
                b = True
        V[j+1] = temp

if __name__ == "__main__":
    V = [5, 7, 0, 2, 3, 1]
    print("Arreglo sin ordenar: ")
    print(V)
    shellSort(V)
    print("Arreglo ordenado: ")
    print(V)
