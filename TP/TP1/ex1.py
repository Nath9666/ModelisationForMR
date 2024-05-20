import numpy as np
import polyscope as ps
import uuid

def random_name():
    return str(uuid.uuid4())

def mesh_cube():
    vertices = np.array([
        [0, 0, 0], # 0
        [1, 0, 0], # 1
        [1, 1, 0], # 2
        [0, 1, 0], # 3
        [0, 0, 1], # 4
        [1, 0, 1], # 5
        [1, 1, 1], # 6
        [0, 1, 1], # 7
    ])

    edges = np.array([
        [0, 1, 2, 3], # Face inférieure
        [4, 5, 6, 7], # Face supérieure
        [0, 1, 5, 4], # Face avant
        [1, 2, 6, 5], # Face droite
        [2, 3, 7, 6], # Face arrière
        [3, 0, 4, 7]  # Face gauche
    ])
    
    # Générer un nom aléatoire
    name = random_name()

    # Ajouter un cube à Polyscope
    ps_mesh = ps.register_surface_mesh(name, vertices, edges)
    return ps_mesh, vertices, edges

def main():
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
        [0, 1], [1, 2], [2, 3], [3, 0], [0,2], # Face inférieure
        [4, 5], [5, 6], [6, 7], [7, 4], [4,6],  # Face supérieure
        # Ajouter les arêtes verticales
        [0, 4], [1, 5], [2, 6], [3, 7], [8, 0],
        [8, 1], [8, 2], [8, 3], [8, 4], [8, 5],
        [8, 6], [8, 7],
        # Ajouter les arêtes diagonales
        [0, 5], [1, 6], [2, 7], [3, 4]
    ])

    # Ajouter le cube à Polyscope
    ps_curve = ps.register_curve_network("My Cube", vertices, edges)

    mesh_cube()

    # Afficher le cube
    ps.show()