if __name__=="__main__":
    registros=[]
    for  k in range (2):
     nuevo={}
     nuevo["Cedula"]=input("Cedula:\n")
     nuevo["Nombre"]=input("Nombre:\n")
     nuevo["Apellido"]=input("Apellido:\n")
     registros.append(nuevo)
    for fila in registros:
      for clave in fila:
        print(clave,fila[clave],sep="-")
