#Reto 1. Plan de vacunación

def vacunacion(C):
    P=2*C+4
    V=int((C+P)/5)

    if V <= 20:
        A = "uno"
    elif V >= 21 and V <=30:
        A = "dos"
    elif V >= 31 and V <=50:
        A = "tres"
    elif V >50:
        A = "cuatro"

    cadena = "\n" + str(C) + " " + str(P) + " " + str(V) + "\n" + "\n" + A
    return(cadena)


C=int(input("Número de cajas: "))

print(vacunacion(C))