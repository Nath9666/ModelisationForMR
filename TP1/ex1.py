import numpy as np
import polyscope as ps

# Initialiser Polyscope
ps.init()

# Générer les coordonnées des sommets du cube
vertices = np.array([
    [0, 0, 0], # 0
    [1, 0, 0], # 1
    [1, 1, 0], # 2
    [0, 1, 0], # 3
    [0, 0, 1], # 4
    [1, 0, 1], # 5
    [1, 1, 1], # 6
    [0, 1, 1], # 7
    [0.5, 0.5, 0.5] # 8
])

# Générer les indices des arêtes du cube
edges = np.array([
    [0, 1], [1, 8], [8, 0],  # Faces avant
    [1, 2], [2, 8], [8, 1],  # Faces avant
    [2, 3], [3, 8], [8, 2],  # Faces avant
    [3, 0], [0, 8], [8, 3],  # Faces avant
    [4, 5], [5, 8], [8, 4],  # Faces arrière
    [5, 6], [6, 8], [8, 5],  # Faces arrière
    [6, 7], [7, 8], [8, 6],  # Faces arrière
    [7, 4], [4, 8], [8, 7],  # Faces arrière
    [0, 1], [1, 5], [5, 0],  # Face bas
    [1, 5], [5, 4], [4, 1],  # Face bas ajoutée
    [4, 7], [7, 3], [3, 4],  # Face bas
    [2, 3], [3, 7], [7, 2],  # Face haut
    [0, 3], [3, 7], [7, 0],  # Face gauche
    [1, 2], [2, 6], [6, 1]   # Face droite
])

# Ajouter le cube à Polyscope
ps_curve = ps.register_curve_network("My Cube", vertices, edges)

# Afficher le cube
ps.show()