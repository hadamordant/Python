class ArbolN:
    def __init__(self, etiqueta, hijos=None):
        self.etiqueta = etiqueta
        self.hijos = hijos
        self.padre = None
    def agregarHijo(self, hijo):
        if self.hijos == None:
            self.hijos = []
        hijo.padre = self
        self.hijos.append(hijo)
        
    def esHoja(self):
        return self.hijos == None or self.hijos == []

    
        
def preorden(a):
    if a != None:
        print(a.etiqueta)
        if a.hijos != None:
            for hijo in a.hijos:
                preorden(hijo)

if __name__ == "__main__":
    A = ArbolN("A")
    B = ArbolN("B")
    C = ArbolN("C")
    D = ArbolN("D")
    E = ArbolN("E")
    F = ArbolN("F")

    A.agregarHijo(B)
    A.agregarHijo(C)
    C.agregarHijo(D)
    C.agregarHijo(E)
    C.agregarHijo(F)

    preorden(A)
