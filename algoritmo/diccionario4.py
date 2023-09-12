if __name__=="__main__":
    registros=[]
    for  k in range (2):
     nuevo={}
     nuevo["Cedula"]="19843767"
     nuevo["Nombre"]="Jose"
     nuevo["Apellido"]="Pereira"
     registros.append(nuevo)
    for fila in registros:
      for clave in fila:
        print(clave,fila[clave],sep="-")
