# Deux variables

#   Un nombre
longueur = 5                    # Valeur de longueur (un entier)
print(longueur)

#   Une fonction
calcul = lambda x: 2*x-1        # Valeur de calcul (une fonction)
print(calcul(longueur))         # Valeur de l'appel à la fonction calcule

# Types
print(type(longueur))
print(type(calcul))
print(type(calcul(longueur)))

#   Nouvelles affectations
longueur = longueur+1
calcul = lambda x,y: 2*x+y
print(longueur)
print(calcul(longueur,3))