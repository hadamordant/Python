if __name__ == '__main__':
    n = int(input("cantidad de filas: "))
    m = int(input("cantidad de columnas: "))
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            valor = int(input("A[%i][%i]: "%(i,j)))
            fila.append(valor)
        matriz.append(fila)

    for i in range(n):
        for valor in fila:
            print("%5i"%(valor), end=" ")
        print()
