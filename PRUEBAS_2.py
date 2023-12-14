pib = open("tabla_pib.tsv","r")
texto= pib.read()
pib_1 = texto.split("\n")
pais = input("dame las iniciales:")
pais = pais.upper()
y = (F"CLV10_EUR_HAB,B1GQ,{pais}")
definitiva = []
año = 2000
for i in pib_1:
    z = i.split()
    if z[0] == y:
        x = (z[1:])
        for j in x:
            h = (f"{j} es el pib correspondiente al año {año}")
            definitiva.append(h)
            año = año + 1
        print(definitiva)