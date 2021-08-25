
A = input("Cartas Alejandra: ")
R = input("Cartas Raquel: ")
S = input("Cartas Repartidor: ")

P_A = 1
P_R = 1
C = ""

if (len(A) < 3) or (len(A) > 6) or (len(R) < 3) or (len(R) > 6):
    print("Por favor solo digite entre 3 y 6 caracteres")

else:    
    for i in range(0, len(S), 1):
        
        if A.find(S[i]) >=0:    
            P_A += 1
        if R.find(S[i]) >=0:
            P_R += 1

        if P_A > P_R:
            C += "A"
        if P_A < P_R:
            C += "R"
        if P_A == P_R:
            C += "+"
        
print(C)       


