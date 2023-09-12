#Ordenamiento por Seleccion
def selectionSort(V):
    n = len(V)    
    for i in range(n-1):
        minimo = i
        for j in range(i+1, n):
            #La diferencia con respecto a Bubble Sort es que el intercambio
            #no se realiza aca, sino que se almacena la posicion del menor
            if V[j]["Cedula"]< V[minimo]["Cedula"]:
                minimo = j
        #Al finalizar el ciclo de "j" se realiza el intercambio
        temp = V[minimo]
        V[minimo] = V[i]
        V[i] = temp

if __name__ == "__main__":
    registros=[]
    nuevo={}
    nuevo["Cedula"]="19843767"
    nuevo["Nombre"]="Jose"
    nuevo["Apellido"]="Pereira"
    nuevo["Cedula"]="09843767"
    nuevo["Nombre"]="Jose"
    nuevo["Apellido"]="Pereira"
    print(nuevo)
    print(nuevo["Cedula"])
    print(nuevo["Nombre"])
    print(nuevo["Apellido"])
    registros.append(nuevo)
    
   

