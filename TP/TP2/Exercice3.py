import numpy as np
from Exercice1 import *
from Exercice2 import *

def butterfly_subdivision(mesh, iterations=1):
    vertices, faces = mesh
    for _ in range(iterations):
        # Créer un dictionnaire pour stocker les voisins de chaque sommet
        neighbors = {i: set() for i in range(len(vertices))}
        for face in faces:
            for i in range(3):
                neighbors[face[i]].add(face[(i+1)%3])
                neighbors[face[i]].add(face[(i+2)%3])

        # Ajouter de nouveaux points au milieu de chaque arête
        edge_points = {}
        new_vertices = list(vertices)
        for face in faces:
            for i in range(3):
                point1, point2 = sorted([face[i], face[(i+1)%3]])
                if (point1, point2) not in edge_points:
                    new_point = (vertices[point1] + vertices[point2]) / 2
                    edge_points[(point1, point2)] = len(new_vertices)
                    new_vertices.append(new_point)

        # Mettre à jour la position des points existants
        for vertex in range(len(vertices)):
            n = len(neighbors[vertex])
            if n > 3: # Point intérieur
                beta = 1/n * (5/8 - (3/8 + 1/4 * np.cos(2*np.pi/n))**2)
                new_vertices[vertex] = (1 - n*beta)*vertices[vertex] + beta*sum(new_vertices[neighbor] for neighbor in neighbors[vertex])
            else: # Point sur le bord
                new_vertices[vertex] = 3/4 * vertices[vertex] + 1/8 * sum(new_vertices[neighbor] for neighbor in neighbors[vertex])

        # Relier tous les points ensemble
        new_faces = []
        for face in faces:
            points = [edge_points[tuple(sorted([face[i], face[(i+1)%3]]))] for i in range(3)]
            new_faces.append([face[0], points[0], points[2]])
            new_faces.append([face[1], points[1], points[0]])
            new_faces.append([face[2], points[2], points[1]])
            new_faces.append(points)

        vertices = np.array(new_vertices)
        faces = np.array(new_faces)

    mesh = (vertices, faces)
    return mesh

if __name__ == '__main__':
    mesh = generate_cube_hole_mesh()
    mesh = transform_quad_to_tri(mesh)
    ex1.Visualize3DMesh(mesh[0], mesh[1])
    for i in range(5): # Changez ce nombre pour le nombre d'itérations que vous voulez
        print(f"Iteration {i+1}")
        new_mesh = loop_subdivision(mesh, 1)
        ex1.Visualize3DMesh(new_mesh[0], new_mesh[1])
        mesh = new_mesh