import OBJ_File as obj
import numpy as np
import polyscope as ps
import ex2

# Fonction pour vérifier si une arête est partagée avec un autre triangle dans le maillage
def est_arête_partagée(triangle, point1, point2, M):
    for autre_triangle in M:
        # Ignorer le même triangle
        if autre_triangle == triangle:
            continue
        # Si l'arête est partagée avec un autre triangle, retourner True
        if (point1 in autre_triangle) and (point2 in autre_triangle):
            return True
    return False

# Charger le fichier OBJ
def main():
    obj_file = obj.load_obj("common-3d-test-models-master\\data\\suzanne.obj")
    my_points = obj_file.only_coordinates()
    verts = my_points
    faces = obj_file.only_faces()

    # Appliquer la fonction extraireBord sur les faces pour obtenir le bord
    bord = ex2.ExtraireBord((verts, faces))

    # Convertir le bord en un tableau numpy
    bord_np = np.array(bord)

    # Initialiser polyscope
    ps.init()

    # Enregistrer le maillage
    ps.register_surface_mesh("my mesh", verts, faces, smooth_shade=True)

    # Ajouter les lignes représentant le bord
    ps.register_curve_network("bord", verts, bord_np, enabled=True, color=(0.0, 0.0, 0.0))

    # Afficher le maillage dans l'interface 3D
    ps.show()