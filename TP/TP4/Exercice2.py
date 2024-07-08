import numpy as np

#Exercice 2
angle_x_degrees = 50
angle_y_degrees = 30
angle_z_degrees = 60
#Convertir les angles en radians
angle_x_radians = np.radians(angle_x_degrees)
angle_y_radians = np.radians(angle_y_degrees)
angle_z_radians = np.radians(angle_z_degrees)

#Calculer les matrices de rotation pour chaque axe
R_x = np.array([[1, 0, 0],[0, np.cos(angle_x_radians), -np.sin(angle_x_radians)],[0, np.sin(angle_x_radians), np.cos(angle_x_radians)]])

R_y = np.array([[np.cos(angle_y_radians), 0, np.sin(angle_y_radians)],
                [0, 1, 0],
                [-np.sin(angle_y_radians), 0, np.cos(angle_y_radians)]])

R_z = np.array([[np.cos(angle_z_radians), -np.sin(angle_z_radians), 0],
                [np.sin(angle_z_radians), np.cos(angle_z_radians), 0],
                [0, 0, 1]])

# 4. Multiplier les matrices de rotation pour obtenir R
R = R_z @ R_y @ R_x

# 5. Définir le vecteur de translation
t = np.array([4, 5, 10])

# 6. Construire la matrice de transformation M
M = np.eye(4)  # Créer une matrice identité 4x4
M[:3, :3] = R  # Remplacer la sous-matrice 3x3 supérieure gauche par R
M[:3, 3] = t  # Remplacer la dernière colonne (sauf la dernière ligne) par t

print("Matrice de transformation M :")
print(M)