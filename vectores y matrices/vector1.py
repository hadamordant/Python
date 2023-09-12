def maximo(A):
    valor = A[0]
    posicion=0
    for i in range(len(A)):
        
        if A[i]>valor:
            valor = A[i]
            posicion = i
    return valor,posicion

if __name__ == '__main__':
    n = int(input("longitud del vector: "))
    A=[]
    for i in range(n):
        num = int(input("A[%i]: "%(i)))
        A.append(num)
    
    [valor,posicion]=maximo(A)
    print("mayor valor: %i"%(valor))
    print("posision: %i"%(posicion))
    
