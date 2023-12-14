def buscarlinea(x,m):
    """"el parametro de entrada son dos numeros n y m
        y lo que devuelve por pantalla la función 
        es la linea m de la tabla de multiplicar de n"""
    import os
    y = (f"tabla-{x}")
    if os.path.isfile(y) == True:
         z = open(y,"r")
         tabla = z.readlines()
         return print(tabla[m-1])
    else:
         return print("no existe tal fichero")
n = input("de la tabla de que numero quieres sacar la linea:")
m = int(input("que linea quieres sacar de esa tabla: "))
buscarlinea(n,m)