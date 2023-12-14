pib = open("tabla_pib.tsv","r")
pib_1 = pib.split("\n")
pais = input("introduze las iniciales del pais: ")
linea =(F"CLV10_EUR_HAB,B1GQ,CLV10_EUR_HAB,B1GQ,{pais}")
print(pib_1.split(" "))
for i in range(1,len(pib_1)):
    linea_pais = i.split(())
