#TAF 2 Détermine la saison correspondant à un mois donné (saisie d'un numéro de mois, affichage de la saison).

print ("Détermine la saison correspondant à un mois donné (saisie d'un numéro de mois, affichage de la saison).")
mois = int(input("Entrez le numero du mois à verifier (Ex: 1=Janvier, 2=fevrier...) :"))

if mois == 12 or mois == 1 or mois == 2: print("Saison : HIVER ")
elif mois == 3 or mois == 4 or mois == 5: print("Saison : PRINTEMPS")
elif mois == 6 or mois == 7 or mois == 8: print("Saison : ETE")
elif mois == 9 or mois == 10 or mois == 11: print("Saison : AUTOMNE")
else: print("CE MOIS N'EXISTE PAS VEILLER SAISIR UN NOMBRE COMPRIS ENTRE 1 à 12")