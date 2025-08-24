# Taff 3 Calcule la somme des entiers de 1 à `n`, où `n` est fourni par l'utilisateur.

print("ce programme Calcule la somme des entiers de 1 à `n`,")
n = int(input("Entrez le numero un entier positif : "))
som=0
for i in range(n+1): 
    som = som + i
    print ("la somme des entiers de 1 à", n, "est :" ,som)