def shellSort(V):
    n = len(V)
    for i in range(n):
        temp = V[i]
        j = i-1
        b = False
        
        while b == False and j >= 0:
            if temp < V[j]:
                #Desplazar los elementos
                V[j+1] = V[j]
                j = j-1
            else:
                b = True
        V[j+1] = temp
        
if __name__ == '__main__':
    #Inicializar arreglo vacio
    Registros = []
    V = []

    #inicializar diccionario1
    Nuevo = {}
    
    #llenar cada uno de los campos del diccionario
    Nuevo["cedula"] = 16052570
    Nuevo["nombre"] = "Romina"
    Nuevo["apellido"] = "Betancourt"

    #crear el arreglo interno, que contendra tambien elementos tipo diccionario
    Productos = []
    #diccionario que corresponde a cada producto 
    ProductoNuevo = {}
    ProductoNuevo["codigo"] = "ACET001"
    ProductoNuevo["descripcion"] = "Removedor Esmalte Valmy"
    #agregar el diccionario creado al arreglo "Productos"
    Productos.append(ProductoNuevo)

    ProductoNuevo = {}

    ProductoNuevo["codigo"] = "HAR001"
    ProductoNuevo["descripcion"] = "Harina Pan"
    #agregar el diccionario creado al arreglo "Productos"
    Productos.append(ProductoNuevo)

    Nuevo["Productos"] = Productos

    Registros.append(Nuevo)

    #inicializar diccionario2
    Nuevo = {}
    #llenar cada uno de los campos del diccionario
    Nuevo["cedula"] = 18895842
    Nuevo["nombre"] = "Adolfo"
    Nuevo["apellido"] = "Simeone"

    #crear el arreglo interno, que contendra tambien elementos tipo diccionario
    Productos = []
    #diccionario que corresponde a cada producto
    ProductoNuevo = {}
    ProductoNuevo["codigo"] = "ATAMEL01"
    ProductoNuevo["descripcion"] = "Atamel 500 mg"
    #agregar el diccionario creado arreglo "Productos" 
    Productos.append(ProductoNuevo)

    ProductoNuevo = {}
    ProductoNuevo["codigo"] = "PAPELT001"
    ProductoNuevo["descripcion"] = "Papel Toalet Limpiolin"
    #agregar el diccionario creado al arreglo "Productos"
    Productos.append(ProductoNuevo)

    Nuevo["Productos"] = Productos

    Registros.append(Nuevo)

     #inicializar diccionario3
    Nuevo = {}
    #llenar cada uno de los campos del diccionario
    Nuevo["cedula"] = 24061947
    Nuevo["nombre"] = "Xiomara"
    Nuevo["apellido"] = "Rodríguez"

    #crear el arreglo interno, que contendra tambien elementos tipo diccionario
    Productos = []
    #diccionario que corresponde a cada producto
    ProductoNuevo = {}
    ProductoNuevo["codigo"] = "PAPELT002"
    ProductoNuevo["descripcion"] = "Papel Toalet Suciolin"
     #agregar el diccionario creado al arreglo "Productos"
    Productos.append(ProductoNuevo)

    ProductoNuevo = {}
    ProductoNuevo["codigo"] = "XANAX01"
    ProductoNuevo["descripcion"] = "Xanax 10 mg"
    #agregar el diccionario creado al arreglo "Productos"
    Productos.append(ProductoNuevo)

    Nuevo["Productos"] = Productos

    Registros.append(Nuevo)

    #inicializar diccionario4
    Nuevo = {}
    #llenar cada uno de los campos del diccionario
    Nuevo["cedula"] = 80254147
    Nuevo["nombre"] = "Xim"
    Nuevo["apellido"] = "Chang"

    #crear el arreglo interno, que contendra tambien elementos tipo diccionario
    Productos = []
    #diccionario que corresponde a cada producto
    ProductoNuevo = {}
    ProductoNuevo["codigo"] = "ARROZ01"
    ProductoNuevo["descripcion"] = "Arroz Mary"
     #agregar el diccionario creado al arreglo "Productos"
    Productos.append(ProductoNuevo)

    ProductoNuevo = {}
    ProductoNuevo["codigo"] = "CARAOTA01"
    ProductoNuevo["descripcion"] = "Caraota La Lucha"
    #agregar el diccionario creado al arreglo "Productos"
    Productos.append(ProductoNuevo)

    Nuevo["Productos"] = Productos

    Registros.append(Nuevo)
    
    print("         SISTEMA BIOMÉTRICO DE COMPRAS PRODUCTOS NECESARIOS")
    print("               L A    M A M A   D E   C H A V E Z"    )
    print("Los siguientes venezolanos no podrán comprar hasta el 01/12/2021")
    print()
    print("-----------------------------------------------------------------")

    shellSort(V) #llamada al ordenamiento shell
    
    for V in Registros:
        print("Cedula: ", V["cedula"])
        print("Nombre: ", V["nombre"])
        print("Apellido: ", V["apellido"])
        print("Compra de Productos:")
        for Productos in V["Productos"]:
            print("    Codigo: ", Productos["codigo"], "Descripcion: ", Productos["descripcion"])
        print()
        print("-----------------------------------------------------------------")

    
