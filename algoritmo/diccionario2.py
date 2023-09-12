if __name__=="__main__":
    registros=[]
    nuevo={}
    nuevo["Cedula"]="19843767"
    nuevo["Nombre"]="Jose"
    nuevo["Apellido"]="Pereira"
    registros.append(nuevo)
    nuevo={}
    nuevo["Cedula"]="29535767"
    nuevo["Nombre"]="Jose"
    nuevo["Apellido"]="Mendes"
    print(nuevo)
    print(nuevo["Cedula"])
    print(nuevo["Nombre"])
    print(nuevo["Apellido"])
    registros.append(nuevo)
    print(registros)
    for fila in registros:
        print(fila)
