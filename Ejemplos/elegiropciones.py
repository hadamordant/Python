if __name__ == '__main__':
    x = input ("""Eliga una de las siguientes conversiones:
    (1) Segundos - Minutos
    (2) Minutos - Segundos
    (3) Minutos - Horas
    (4) Horas - Minutos

    Opcion: """)


    if x == "1":
        A=int (input ("ingrese valor en segundos: "))
        B=A/60.0
        print (A,"segundos =" ,B ,"minutos")

    elif x == "2":
        A=int (input ("ingrese valor en minutos: "))
        B=A*60
        print (A, "minutos =", B ,"segundos")

    elif x == "3":
        A=int (input ("ingrese valor en minutos: "))
        B=A/60.0
        print (A, "minutos =",B ,"horas")

    elif x == "4":
        A=int (input ("ingrese valor en horas: "))
        B=A*60
        print (A, "horas =", B ,"minutos")

    else:
        input("por favor ingrese una opcion valida")


    input()
