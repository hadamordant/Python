class ArbolB:
    def __init__(self, etiqueta, izq=None, der=None):
        self.etiqueta = etiqueta        
        self.izq = izq
        self.der = der
        self.padre = None
        if izq != None:
            izq.padre = self
        if der != None:
            der.padre = self

    def setIzq(self, izq):
        self.izq = izq
        izq.padre = self

    def setDer(self, der):
        self.der = der
        der.padre = self

def preorden(a):
    if a != None:
        print(a.etiqueta)
        preorden(a.izq)
        preorden(a.der)

if __name__ == "__main__":
    D = ArbolB("D")
    E = ArbolB("E")
    C = ArbolB("C")
    C.setIzq(D)
    C.setDer(E)
    B = ArbolB("B")
    A = ArbolB("A")
    A.setIzq(B)
    A.setDer(C)
    preorden(A)
    
        
