def mergeSort(V, n):
    #Deben haber al menos 2 elementos en el arreglo
    if n>2:
        #tomar una mitad del arreglo
        a1 = V[0: n//2]
        #tomar la otra mitad
        a2 = V[n//2:n]
        #cada mitad del arreglo se dividirá nuevamente en 2 partes
        mergeSort(a1, len(a1))
        mergeSort(a2, len(a2))
        #finalmente, quedarán N arreglos de 1 elemento, a partir de los cuales
        #se volverá a armar el arreglo original, pero con los elementos en orden
        merge(a1, a2, V, n)

def merge(a1, a2, V, n):    
    i=j=k=0
    #Se comparan elementos de a1 con a2, es decir, de una mitad con respecto
    #a la otra, e ir agregando los elementos en orden en el arreglo V
    while i<n//2 and j<n-n//2:
        if a1[i] < a2[j]:
            V[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            V[k] = a2[j]
            j = j + 1
            k = k + 1

    #Copiar en el arreglo V los elementos que no se agregaron en el ciclo anterior
    while i<n//2:
        V[k] = a1[i]
        i = i + 1
        k = k + 1

    while j<n-n//2:
        V[k] = a2[j]
        j = j + 1
        k = k + 1
    
if __name__ == "__main__":
    V = [5, 7, 0, 2, 3, 1]
    print("Arreglo sin ordenar: ")
    print(V)
    mergeSort(V, len(V))
    print("Arreglo ordenado: ")
    print(V)
