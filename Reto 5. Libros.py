#Reto 5 Libros

#Función 1
A = ["Universo","La María","La Biblia","Herón","Universo","La Biblia","Cosmos","La María"]
Lista = []

def titulos(A):
    for i in range(0,len(A),1):
        if A[i] not in Lista:
            Lista.append(A[i])
    return Lista

#Función 2
L = [2, 0, 5, 1, 3]
M = ["Universo","La María","La Biblia","Universo","Herón","Universo","La Biblia","Cosmos"]
N = "Universo"
Lista2 = []

def faltante(L,M,N):
    for i in L:
        if M[i] == N:
            Lista2.append(i)
    return Lista2

#Función 3
L1 = ["Universo","La María","Herón","La Odisea","La Biblia","Cosmos"]
L2 = ["El Mio Cid","Universo","Cosmos","La Odisea","Historia"]
Lista3 = []

def teFaltan(L1,L2):
    for i in range(0,len(L1),1):
        if L1[i] not in L2:
            Lista3.append(L1[i])
    return Lista3

#Función 4
L1 = ["Universo","La María","Herón","La Odisea","La Biblia","Cosmos"]
L2 = ["El Mio Cid","Universo","Cosmos","La Odisea","Historia"]
faltanteL1 =[]
faltanteL2 =[]
Faltan = 0

def interlibros(L1,L2):
    for i in range(0,len(L1),1):
        if L1[i] not in L2:
            faltanteL2.append(L1[i])
    
    for i in range(0,len(L2),1):
        if L2[i] not in L1:
            faltanteL1.append(L2[i])
    Faltan = min(len(faltanteL1),len(faltanteL2))
    return Faltan

print(titulos(A))
print(faltante(L,M,N))
print(teFaltan(L1,L2))
print(interlibros(L1,L2))