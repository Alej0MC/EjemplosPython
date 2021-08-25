#Reto 4: Orden Restaurante
import json

D=input("Indique lista de platos disponibles")
P=input("Indique su pedido")

Lista=json.loads(D)
Lista_llaves =list(Lista.keys())

Pedido=P.split(' ')
valor=0
Disponible = ""

for i in Pedido:
    if i in Lista_llaves:
        Disponible += i + " "
        valor += Lista[i]

print(valor)
print(Disponible)