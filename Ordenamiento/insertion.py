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
    V = [5, 7, 0, 2, 3, 1]
    print("Arreglo sin ordenar: ")
    print(V)
    insertionSort(V)
    print("Arreglo ordenado: ")
    print(V)
