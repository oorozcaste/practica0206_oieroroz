def crear_tabla(x):
    """el parametro de entrada es un numero, y lo 
       que devulve la funcion es una archivo que contiene
       la tabla de multiplicar de ese numero"""
    file = open(f"tabla-{x}","w")
    for i in range(1,11):
         w = (i * x)
         h = (f"{i} x {x} = {w}")
         file.write(h +"\n")
zembakia = int(input("dime un numero del 1 al 10: "))
crear_tabla(zembakia)