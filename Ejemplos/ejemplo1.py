
if __name__ == '__main__':
    #Arreglo inicializado
    A = [3, 6, 2, 4, 6]
    n = len(A)
    print("utilizando in range(n)")
    for i in range(n):
        print(A[i])

    print("utilizando in range(a,b)")
    for i in range(0, n):
        print(A[i])
        
    print("utilizando for in")
    for var in A:
        print(var)
        
