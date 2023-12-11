n = int(input("nuemero: "))

for i in range (1,n * 2,2):
    for j in range(i ,0,-2):
        print(j,end=" ")
    print("")