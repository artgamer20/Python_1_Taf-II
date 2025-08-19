#equation du second degré
print("ce programme resout une equation dans R ")
a = int(input("entrez la valeur de a :")) 
b = int(input("entrez la valeur de b :")) 
c = int(input("entrez la valeur de c :")) 

# verification de a > o
if a== 0 :
    print("impossible")
else: 
    # delta = b2 - 4ac
    delta = b*b - 4*a*c
    print("delta = ",delta)

    # verification vec delta et cas de figure 
    if delta > 0 :  # si deta > 0 : deux solution x1 et x2
        x1 = (-b - delta**0.5) / (2*a) # delta ** 0.5 = Racine carré de delta . 
        x2 = (-b + delta**0.5) / (2*a) # delta ** 0.5 on lit delta puissance 0.5
        print("Deux solutions \n x1 =",x1, "\n x2 = ",x2)

    elif delta == 0 : # si delta == 0 une solution x
        x = -b / (2*a)
        print("Une solutions x =",x)

    else: # si delta < 0 pas de solution
        print("delta < 0 donc pas de solution")