import numpy as np
from Exercice2 import M

#Exercice 3
# Point A dans le repère local
A_local = np.array([3, 2, 0, 1])

# Appliquer la matrice de transformation M à A_local pour obtenir A_global
A_global = M @ A_local

print("Position du point A dans le repère global :")
print(A_global[:3])  # Afficher seulement les coordonnées x, y, z