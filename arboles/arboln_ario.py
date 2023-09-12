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
    #Asignar el apuntador al nodo actual
	actual = A
	
	#Agregar hijos
	actual.agregarHijo(ArbolN("B"))
	actual.agregarHijo(ArbolN("C"))
	#Ahora A tiene como hijos: [0] = B, [1] = C
	print("Nodo actual: %s"%(actual.etiqueta))
	print("Hijos: ")
	for hijo in actual.hijos:
		print(hijo.etiqueta)
	#Desplazar "actual" hacia C (bajar)
	actual = actual.hijos[1]
	#Agregar hijos a C
	actual.agregarHijo(ArbolN("D"))
	actual.agregarHijo(ArbolN("E"))
	actual.agregarHijo(ArbolN("F"))
	print("Nodo actual: %s"%(actual.etiqueta))
	print("Hijos: ")
	for hijo in actual.hijos:
		print(hijo.etiqueta)
    #Desplazar "actual" hacia arriba
	actual = actual.padre
	print("Nodo actual: %s"%(actual.etiqueta))
	print("Hijos: ")
	for hijo in actual.hijos:
		print(hijo.etiqueta)
	print("Recorrido en preorden")
	preorden(actual)
