if __name__=="__main__":
    registros=[]
    for  k in range (1):
     nuevo={}
     nuevo["Cedula"]=input("Cedula:\n")
     nuevo["Nombre"]=input("Nombre:\n")
     nuevo["Apellido"]=input("Apellido:\n")
     Materia={}
     Materia["Codigo"]="Aes"
     Materia["Descripcion"]="Algoritmo y Estructuras"
     nuevo["Materia"]=Materia
     registros.append(nuevo)
    for fila in registros:
     print("Cedula:"+fila["Cedula"])
     print("Nombre:"+fila["Nombre"])
     print("Apellido:"+fila["Apellido"])
     print("Materia")
     print("Codigo:"+fila["Materia"]["Codigo"])
     print("Descripcion:"+fila["Materia"]["Descripcion"])
     

     
