def quickSort(V, izq, der):
    i = izq
    j = der
    pivote = V[(izq+der)//2]
    while i<=j:
        while V[i]< pivote:
            i = i + 1
        while V[j] > pivote:
            j = j - 1
        if i <= j:            
            temp = V[i]
            V[i] = V[j]
            V[j] = temp
            i = i+1
            j = j-1

    if j > izq:
        quickSort(V, izq, j)
    if i < der:
        quickSort(V, i, der)
    

if __name__ == "__main__":
    V = [5, 7, 0, 2, 3, 1]
    print("Arreglo sin ordenar: ")
    print(V)
    quickSort(V, 0, len(V)-1)
    print("Arreglo ordenado: ")
    print(V)
