#Ordenamiento por Seleccion
def selectionSort(V):
    n = len(V)    
    for i in range(n-1):
        minimo = i
        for j in range(i+1, n):
            #La diferencia con respecto a Bubble Sort es que el intercambio
            #no se realiza aca, sino que se almacena la posicion del menor
            if V[j]< V[minimo]:
                minimo = j
        #Al finalizar el ciclo de "j" se realiza el intercambio
        temp = V[minimo]
        V[minimo] = V[i]
        V[i] = temp

if __name__ == "__main__":
    V = [5, 7, 0, 2, 3, 1]
    print("Arreglo sin ordenar: ")
    print(V)
    selectionSort(V)
    print("Arreglo ordenado: ")
    print(V)

