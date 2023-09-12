if __name__=="__main__":
    registros=[]
    for  k in range (1):
     nuevo={}
     nuevo["Cedula"]=input("Cedula:\n")
     nuevo["Nombre"]=input("Nombre:\n")
     nuevo["Apellido"]=input("Apellido:\n")
     materias=[]
     Materia={}
     Materia["Codigo"]="Aes"
     Materia["Descripcion"]="Algoritmo y Estructuras"
     materias.append(Materia)
     nuevo["Materia"]=materias
     registros.append(nuevo)
    for fila in registros:
     print("Cedula:"+fila["Cedula"])
     print("Nombre:"+fila["Nombre"])
     print("Apellido:"+fila["Apellido"])
     print("Materia")
     for Materia in fila["Materia"]:
         print(Materia["Codigo"])
         print(Materia["Descripcion"])
     input()
