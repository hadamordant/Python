class TestOrdenamiento:
    def __init__(self):
        #Constructor. Genera una lista nueva.'''
        self.lista = [4, 1, 5, 25, 2, 7, 0, -10, -100]
 
    def ordenarMayorAMenor(self):
       # Ordena la lista de mayor a menor.'''
        cmp = lambda x,y: self.__cmpMayorMenor(x, y)
        self.lista.sort(cmp)
 
    def mostrar(self):
        print(self.lista)
 
    def __cmpMayorMenor(self, x, y):
        #Comparador. Este método define la forma en la que se compararán
        #   dos elementos de la lista. En este caso se comparan de mayor a
        #   menor.'''
        if x < y:
            return -1
        elif x == y:
            return 0
        else:
            return 1
        try:
            import sys
            import testordenamiento
 
 
if __name__ == '__main__':
    # Primero generamos la lista y la mostramos (desordenada)
    ord = testordenamiento.TestOrdenamiento()
    ord.mostrar()
     
    # Luego la ordenamos y la volvemos a mostrar
    ord.ordenar()
    ord.mostrar()
 
    return 0
