def buscarlinea(x,m):
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