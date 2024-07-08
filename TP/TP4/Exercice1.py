import numpy as np

#Exercice 1
angle_degrees = 50
# Convertir l'angle en radians
angle_radians = np.radians(angle_degrees)
#Calculer les éléments de la matrice de rotation
cos_theta = np.cos(angle_radians)
sin_theta = np.sin(angle_radians)
#Créer la matrice de rotation
rotation_matrix_x = np.array([[1, 0, 0],[0, cos_theta, -sin_theta],[0, sin_theta, cos_theta]])
print("Matrice de rotation autour de l'axe X pour un angle de 50 degrés :")
print(rotation_matrix_x)