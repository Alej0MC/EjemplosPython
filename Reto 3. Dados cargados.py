#Reto 3: Dados cargados

D = input("Por favor digite el resultado de los datos en orden, separado por espacio: ")
bef=0
count=1
R1 = ""
R2 =""
for i in range(0, len(D), 2):
    if D[i]==bef:
        count+=1
    else:
        R1 = R1 + D[i] + " "
        if i>0:
            R2 = R2 + str(count) + " "
        count=1    
    bef=D[i]

if D[i] == D[i-2]:
    R2 = R2 + str(count)
else:
    R2 = R2 + "1"

print(R1)
print(R2)