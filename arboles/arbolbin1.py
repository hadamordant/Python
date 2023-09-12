class ArbolB:
    def __init__(self, etiqueta, izq=None, der=None):
        self.etiqueta = etiqueta
        self.izq = izq
        self.der = der


def preorden(a):
    if a != None:
        print(a.etiqueta)
        preorden(a.izq)
        preorden(a.der)

if __name__ == "__main__":
    D = ArbolB("D")
    E = ArbolB("E")
    C = ArbolB("C", D, E)
    B = ArbolB("B")
    A = ArbolB("A", B, C)
    preorden(A)
    
        
