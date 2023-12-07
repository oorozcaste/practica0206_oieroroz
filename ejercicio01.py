def crear_tabla(x):
    file = open(f"tabla del {x}","w")
    for i in range(1,10):
         w = (i * x)
         h = (f"{i} x {x} = {w}")
         file.write(h +"\n")
zembakia = int(input("dime un numero del 1 al 10: "))
crear_tabla(zembakia)