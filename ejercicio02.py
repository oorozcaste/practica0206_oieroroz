def buscar_ficher0(x):
    """el parametro de entrada es un numero(str)
       y lo que devuelve por pantalla la función 
       es la tabla de multiplicar de ese numero 
       (si existe), si no existe lo dira. """
    import os
    y = (f"tabla-{x}")
    if os.path.isfile(y) == True:
         z = open(y,"r")
         tabla = z.read()
         return print(tabla)
    else:
         return print("no existe tal fichero")

c = input("un numero: ")
buscar_ficher0(c)
    
