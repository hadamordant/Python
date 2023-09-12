if __name__=="__main__":
    registros=[]
    nuevo={}
    nuevo["Cedula"]="19843767"
    nuevo["Nombre"]="Jose"
    nuevo["Apellido"]="Pereira"
    registros.append(nuevo)
    nuevo={}
    nuevo["Cedula"]="17890555"
    nuevo["Nombre"]="Jose"
    nuevo["Apellido"]="Mens"
    registros.append(nuevo)
    for fila in registros:
      for clave in fila:
        print(sorted(clave,fila[clave],sep="-"))
